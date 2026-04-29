#!/usr/bin/env python3
"""Karabiner-Elements GUI Manager (zero dependencies)."""

import json
import shutil
import subprocess
import sys
import webbrowser
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

KARABINER_JSON = Path.home() / ".config" / "karabiner" / "karabiner.json"
KARABINER_CLI = "/Library/Application Support/org.pqrs/Karabiner-Elements/bin/karabiner_cli"
GUI_DIR = Path(__file__).parent
GROUP_ORDER_FILE = GUI_DIR.parent / "group-order.json"
DEFAULT_PORT = 8070

DEVICE_NAMES = {
    "global": "グローバル",
    "76:671": "Magic Keyboard",
    "1133:50503": "Logitech USB Receiver",
    "1452:599": "X8 BLE / K02",
    "9427:12427": "TENBT03 テンキー",
    "11720:36888": "8BitDo Zero 2",
    "11720:36897": "8BitDo Micro",
    "13364:": "Keychron Link-KM",
    "1390:342": "リラコン",
}

DEVICE_ORDER = [
    "global", "76:671", "13364:", "1452:599",
    "9427:12427", "11720:36888", "11720:36897", "1133:50503", "1390:342",
]


def load_group_order():
    if GROUP_ORDER_FILE.exists():
        try:
            return json.loads(GROUP_ORDER_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return list(DEVICE_ORDER)


def save_group_order(order):
    GROUP_ORDER_FILE.write_text(
        json.dumps(order, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


# ── Config I/O ──────────────────────────────────────────


def read_config():
    return json.loads(KARABINER_JSON.read_text(encoding="utf-8"))


def write_config(data):
    bak_dir = KARABINER_JSON.parent / "automatic_backups"
    bak_dir.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(KARABINER_JSON, bak_dir / f"karabiner_gui_{ts}.json")
    # Write directly to keep inode (Karabiner uses kqueue/vnode to watch)
    KARABINER_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8"
    )
    # Reformat to Karabiner's canonical format so it detects changes correctly
    subprocess.run(
        [KARABINER_CLI, "--format-json", str(KARABINER_JSON)],
        capture_output=True, timeout=5,
    )


# ── Path helpers ────────────────────────────────────────


def nav(obj, path):
    for p in path.split("."):
        obj = obj[int(p)] if p.isdigit() else obj[p]
    return obj


def nav_parent(obj, path):
    parts = path.split(".")
    for p in parts[:-1]:
        obj = obj[int(p)] if p.isdigit() else obj[p]
    k = parts[-1]
    return obj, int(k) if k.isdigit() else k


# ── Grouping ────────────────────────────────────────────


def device_key(conditions):
    for c in conditions or []:
        if c.get("type") == "device_if":
            for ident in c.get("identifiers", []):
                v = ident.get("vendor_id", "")
                p = ident.get("product_id", "")
                return f"{v}:{p}" if p else f"{v}:"
    return "global"


DEVICE_SETTING_FIELDS = (
    "pointing_motion_xy_multiplier",
    "pointing_motion_wheels_multiplier",
    "ignore_vendor_events",
)


def build_groups(config):
    pr = config["profiles"][0]
    grp = {}
    device_info = {}  # dk -> {"path": str, "settings": dict}

    def ensure(dk):
        if dk not in grp:
            grp[dk] = []

    # Complex modifications
    for ri, rule in enumerate(pr.get("complex_modifications", {}).get("rules", [])):
        rdesc = rule.get("description", "")
        enabled = rule.get("enabled", True)
        for mi, m in enumerate(rule.get("manipulators", [])):
            dk = device_key(m.get("conditions"))
            ensure(dk)
            entry = {
                "path": f"profiles.0.complex_modifications.rules.{ri}.manipulators.{mi}",
                "container": "profiles.0.complex_modifications.rules",
                "container_index": ri,
                "rule_idx": ri,
                "type": "complex",
                "enabled": enabled,
                "rule_description": rdesc,
                "description": m.get("description", ""),
                "from": m.get("from", {}),
                "to": m.get("to", []),
                "conditions": m.get("conditions", []),
            }
            for k in ("to_if_alone", "to_if_held_down", "parameters"):
                if k in m:
                    entry[k] = m[k]
            grp[dk].append(entry)

    # Device entries
    for di, dev in enumerate(pr.get("devices", [])):
        ident = dev.get("identifiers", {})
        v, p = ident.get("vendor_id"), ident.get("product_id")
        dk = f"{v}:{p}" if p else f"{v}:"
        ensure(dk)
        device_info[dk] = {
            "path": f"profiles.0.devices.{di}",
            "settings": {k: dev[k] for k in DEVICE_SETTING_FIELDS if k in dev},
        }

        for si, sm in enumerate(dev.get("simple_modifications", [])):
            grp[dk].append({
                "path": f"profiles.0.devices.{di}.simple_modifications.{si}",
                "container": f"profiles.0.devices.{di}.simple_modifications",
                "container_index": si,
                "type": "simple",
                "from": sm.get("from", {}),
                "to": sm.get("to", []),
            })

        for fi, fk in enumerate(dev.get("fn_function_keys", [])):
            grp[dk].append({
                "path": f"profiles.0.devices.{di}.fn_function_keys.{fi}",
                "container": f"profiles.0.devices.{di}.fn_function_keys",
                "container_index": fi,
                "type": "fn_key",
                "from": fk.get("from", {}),
                "to": fk.get("to", []),
            })

    # Profile fn keys
    ensure("global")
    for fi, fk in enumerate(pr.get("fn_function_keys", [])):
        grp["global"].append({
            "path": f"profiles.0.fn_function_keys.{fi}",
            "container": "profiles.0.fn_function_keys",
            "container_index": fi,
            "type": "fn_key",
            "from": fk.get("from", {}),
            "to": fk.get("to", []),
        })

    def make_entry(dk, mappings):
        entry = {"id": dk, "name": DEVICE_NAMES.get(dk, dk), "mappings": mappings}
        if dk in device_info:
            entry["device_path"] = device_info[dk]["path"]
            entry["device_settings"] = device_info[dk]["settings"]
        return entry

    out = []
    seen = set()
    for dk in load_group_order():
        mappings = grp.get(dk, [])
        out.append(make_entry(dk, mappings))
        seen.add(dk)
    for dk in sorted(grp):
        if dk not in seen and grp[dk]:
            out.append(make_entry(dk, grp[dk]))
    return out


# ── HTTP Handler ────────────────────────────────────────


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        p = urlparse(self.path).path
        if p in ("/", "/index.html"):
            self._file("index.html", "text/html")
        elif p == "/api/config":
            self._json({"groups": build_groups(read_config())})
        else:
            self.send_error(404)

    def do_POST(self):
        p = urlparse(self.path).path
        b = self._body()
        handlers = {
            "/api/save": self._save,
            "/api/add": self._add,
            "/api/delete": self._delete,
            "/api/reorder": self._reorder,
            "/api/reorder-groups": self._reorder_groups,
            "/api/save-doc": self._save_doc,
        }
        h = handlers.get(p)
        if h:
            try:
                h(b)
            except Exception as e:
                import traceback
                traceback.print_exc()
                self._json({"ok": False, "msg": str(e)})
        else:
            self.send_error(404)

    def _save(self, body):
        changes = body.get("changes", [])
        if not changes:
            return self._json({"ok": True, "n": 0})
        cfg = read_config()
        for ch in changes:
            target = nav(cfg, ch["path"])
            for k, v in ch["updates"].items():
                target[k] = v
        write_config(cfg)
        self._json({"ok": True, "n": len(changes)})

    def _add(self, body):
        cfg = read_config()
        pr = cfg["profiles"][0]
        gid = body["group_id"]
        mtype = body["type"]
        data = body["data"]

        if mtype == "simple":
            dev = self._find_dev(pr, gid) or self._create_dev(pr, gid)
            if not dev:
                return self._json({"ok": False, "msg": "Invalid group_id"})
            dev.setdefault("simple_modifications", []).append(data)

        elif mtype == "fn_key":
            if gid == "global":
                pr.setdefault("fn_function_keys", []).append(data)
            else:
                dev = self._find_dev(pr, gid) or self._create_dev(pr, gid)
                if not dev:
                    return self._json({"ok": False, "msg": "Invalid group_id"})
                dev.setdefault("fn_function_keys", []).append(data)

        elif mtype == "complex":
            rules = pr.setdefault("complex_modifications", {}).setdefault("rules", [])
            conds = []
            if gid != "global":
                parts = gid.split(":")
                ident = {"vendor_id": int(parts[0])}
                if parts[1]:
                    ident["product_id"] = int(parts[1])
                conds = [{"type": "device_if", "identifiers": [ident]}]
            manip = {
                "type": "basic",
                "from": data["from"],
                "to": data["to"],
                "conditions": conds,
            }
            for k in ("to_if_alone", "to_if_held_down", "parameters"):
                if k in data:
                    manip[k] = data[k]
            rules.append({
                "description": data.get("rule_description", "Custom rule"),
                "manipulators": [manip],
            })

        write_config(cfg)
        self._json({"ok": True})

    def _delete(self, body):
        path = body["path"]
        cfg = read_config()
        parent, idx = nav_parent(cfg, path)
        if isinstance(idx, int):
            parent.pop(idx)
        else:
            del parent[idx]
        # Remove empty rule container
        if ".manipulators." in path:
            rp = path.rsplit(".manipulators.", 1)[0]
            rule = nav(cfg, rp)
            if not rule.get("manipulators"):
                rparent, ridx = nav_parent(cfg, rp)
                rparent.pop(ridx)
        write_config(cfg)
        self._json({"ok": True})

    def _reorder(self, body):
        container = body.get("container")
        from_index = int(body.get("from_index", -1))
        to_index = int(body.get("to_index", -1))
        if not container or from_index < 0 or to_index < 0:
            return self._json({"ok": False, "msg": "Invalid params"})
        cfg = read_config()
        arr = nav(cfg, container)
        if not isinstance(arr, list):
            return self._json({"ok": False, "msg": "Not an array"})
        if not (0 <= from_index < len(arr)):
            return self._json({"ok": False, "msg": "from_index out of range"})
        item = arr.pop(from_index)
        if to_index > from_index:
            to_index -= 1
        to_index = max(0, min(to_index, len(arr)))
        arr.insert(to_index, item)
        write_config(cfg)
        self._json({"ok": True})

    def _reorder_groups(self, body):
        from_index = int(body.get("from_index", -1))
        to_index = int(body.get("to_index", -1))
        cfg = read_config()
        current_groups = build_groups(cfg)
        order = [g["id"] for g in current_groups]
        if not (0 <= from_index < len(order)):
            return self._json({"ok": False, "msg": "from_index out of range"})
        item = order.pop(from_index)
        if to_index > from_index:
            to_index -= 1
        to_index = max(0, min(to_index, len(order)))
        order.insert(to_index, item)
        save_group_order(order)
        self._json({"ok": True})

    def _save_doc(self, body):
        key = body.get("key", "")
        content = body.get("content", "")
        if not key:
            return self._json({"ok": False, "msg": "No key"})
        docs_dir = GUI_DIR.parent / "docs" / "_editor"
        docs_dir.mkdir(parents=True, exist_ok=True)
        filename = key.replace("/", "__") + ".md"
        (docs_dir / filename).write_text(content, encoding="utf-8")
        self._json({"ok": True, "file": filename})

    # ── Helpers ──

    def _find_dev(self, profile, gid):
        parts = gid.split(":")
        vid = int(parts[0])
        pid = int(parts[1]) if parts[1] else None
        for d in profile.get("devices", []):
            i = d.get("identifiers", {})
            if i.get("vendor_id") == vid and (pid is None or i.get("product_id") == pid):
                return d
        return None

    def _create_dev(self, profile, gid):
        if gid == "global":
            return None
        parts = gid.split(":")
        ident = {"vendor_id": int(parts[0])}
        if parts[1]:
            ident["product_id"] = int(parts[1])
        dev = {"identifiers": ident, "ignore": False, "simple_modifications": [], "fn_function_keys": []}
        profile.setdefault("devices", []).append(dev)
        return dev

    def _file(self, name, ct):
        fp = GUI_DIR / name
        if not fp.exists():
            return self.send_error(404, f"{name} not found")
        data = fp.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", f"{ct}; charset=utf-8")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def _json(self, obj):
        data = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def _body(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n)) if n else {}

    def log_message(self, fmt, *args):
        pass


# ── Main ────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]
    no_browser = "--no-browser" in args
    port_args = [a for a in args if a != "--no-browser"]
    port = int(port_args[0]) if port_args else DEFAULT_PORT
    if not KARABINER_JSON.exists():
        sys.exit(f"Error: {KARABINER_JSON} not found")
    srv = HTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}"
    print(f"Karabiner GUI: {url}")
    if not no_browser:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n停止")
