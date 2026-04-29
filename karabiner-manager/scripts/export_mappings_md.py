#!/usr/bin/env python3
"""
karabiner.json のマッピング一覧をデバイス別 Markdown に書き出す。

既定出力: ~/.config/karabiner/karabiner-manager/mappings_by_device/
  - global.md … デバイス非依存の複合ルール + プロファイル fn キー
  - v{vendor}_p{product}.md … 各デバイス
  - _index.md … 目次
  - all.md … 上記を1ファイルに連結

第1引数で出力ディレクトリを上書き可。
"""

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, DefaultDict, Dict, List, Optional, Set, Tuple


def get_karabiner_config_path() -> Path:
    return Path.home() / ".config" / "karabiner" / "karabiner.json"


def pairs_from_conditions(conditions: Optional[List[Any]]) -> List[Tuple[str, str]]:
    if not conditions:
        return []
    out: List[Tuple[str, str]] = []
    seen: Set[Tuple[str, str]] = set()
    for c in conditions:
        if c.get("type") != "device_if":
            continue
        for ident in c.get("identifiers") or []:
            v, p = ident.get("vendor_id"), ident.get("product_id")
            if v is None and p is None:
                continue
            key = (str(v), str(p))
            if key not in seen:
                seen.add(key)
                out.append(key)
    return out


def device_note_from_ident(ident: Dict[str, Any]) -> str:
    return json.dumps(
        {k: v for k, v in sorted(ident.items()) if v is not None},
        ensure_ascii=False,
        indent=2,
    )


def collect_rows(
    profile: Dict[str, Any],
) -> Tuple[List[Dict[str, str]], DefaultDict[Tuple[str, str], List[Dict[str, str]]]]:
    pname = profile.get("name", "")
    global_rows: List[Dict[str, str]] = []
    per_device: DefaultDict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)

    for rule in profile.get("complex_modifications", {}).get("rules", []):
        group = rule.get("description", "")
        for m in rule.get("manipulators", []):
            pairs = pairs_from_conditions(m.get("conditions") or [])
            dev_parts: List[str] = []
            for c in m.get("conditions") or []:
                if c.get("type") != "device_if":
                    continue
                for ident in c.get("identifiers") or []:
                    v, p = ident.get("vendor_id", ""), ident.get("product_id", "")
                    dev_parts.append(f"vendor={v} product={p}")
            dev_note = "; ".join(dev_parts)
            vid0, pid0 = (pairs[0] if pairs else ("", ""))
            extra = {}
            for k in ("parameters", "to_if_alone", "to_if_held_down"):
                if k in m:
                    extra[k] = m[k]
            row = {
                "kind": "complex_modification",
                "profile": pname,
                "rule_group": group,
                "manipulator_note": m.get("description", ""),
                "vendor_id": vid0 if pairs else "",
                "product_id": pid0 if pairs else "",
                "device_filter": dev_note,
                "from": json.dumps(m.get("from"), ensure_ascii=False, indent=2),
                "to": json.dumps(m.get("to"), ensure_ascii=False, indent=2),
                "extra": json.dumps(extra, ensure_ascii=False, indent=2) if extra else "",
            }
            if not pairs:
                global_rows.append(row)
            else:
                for _vid, _pid in pairs:
                    per_device[(_vid, _pid)].append(dict(row))

    for dev in profile.get("devices", []):
        ident = dev.get("identifiers") or {}
        vid, pid = ident.get("vendor_id"), ident.get("product_id")
        if vid is None or pid is None:
            continue
        vs, ps = str(vid), str(pid)
        key = (vs, ps)
        dev_note = device_note_from_ident(ident)

        for sm in dev.get("simple_modifications") or []:
            per_device[key].append(
                {
                    "kind": "device_simple_modification",
                    "profile": pname,
                    "rule_group": "",
                    "manipulator_note": "",
                    "vendor_id": vs,
                    "product_id": ps,
                    "device_filter": dev_note,
                    "from": json.dumps(sm.get("from"), ensure_ascii=False, indent=2),
                    "to": json.dumps(sm.get("to"), ensure_ascii=False, indent=2),
                    "extra": "",
                }
            )
        for fk in dev.get("fn_function_keys") or []:
            per_device[key].append(
                {
                    "kind": "device_fn_function_key",
                    "profile": pname,
                    "rule_group": "",
                    "manipulator_note": "",
                    "vendor_id": vs,
                    "product_id": ps,
                    "device_filter": dev_note,
                    "from": json.dumps(fk.get("from"), ensure_ascii=False, indent=2),
                    "to": json.dumps(fk.get("to"), ensure_ascii=False, indent=2),
                    "extra": "",
                }
            )

    for fk in profile.get("fn_function_keys") or []:
        global_rows.append(
            {
                "kind": "profile_fn_function_key",
                "profile": pname,
                "rule_group": "",
                "manipulator_note": "",
                "vendor_id": "",
                "product_id": "",
                "device_filter": "",
                "from": json.dumps(fk.get("from"), ensure_ascii=False, indent=2),
                "to": json.dumps(fk.get("to"), ensure_ascii=False, indent=2),
                "extra": "",
            }
        )

    return global_rows, per_device


def row_section(idx: int, row: Dict[str, str]) -> str:
    title = row["manipulator_note"] or row["rule_group"] or row["kind"]
    lines = [
        f"### {idx}. {title}",
        "",
        f"- **種別:** `{row['kind']}`",
        f"- **プロファイル:** `{row['profile']}`",
    ]
    if row["rule_group"]:
        lines.append(f"- **ルールグループ:** {row['rule_group']}")
    if row["manipulator_note"] and row["rule_group"]:
        lines.append(f"- **マニピュレータ:** {row['manipulator_note']}")
    if row["device_filter"]:
        lines.append(f"- **デバイス条件:** {row['device_filter']}")
    lines.extend(
        [
            "",
            "**from:**",
            "",
            "```json",
            row["from"] or "null",
            "```",
            "",
            "**to:**",
            "",
            "```json",
            row["to"] or "null",
            "```",
            "",
        ]
    )
    if row.get("extra"):
        lines.extend(["**extra（parameters / to_if_alone 等）:**", "", "```json", row["extra"], "```", ""])
    lines.append("")
    return "\n".join(lines)


def device_intro_lines(vs: str, ps: str, rows: List[Dict[str, str]]) -> List[str]:
    json_ident = ""
    for r in rows:
        df = (r.get("device_filter") or "").strip()
        if df.startswith("{"):
            json_ident = df
            break
    lines = [
        f"- **vendor_id:** `{vs}`",
        f"- **product_id:** `{ps}`",
        "",
    ]
    if json_ident:
        lines.extend(["**identifiers（devices ブロック）:**", "", "```json", json_ident, "```", ""])
    else:
        cond = next(
            (r.get("device_filter") or "" for r in rows if r.get("device_filter")),
            "",
        )
        lines.append("**デバイス条件:** " + (cond or f"vendor={vs} product={ps}"))
        lines.append("")
    lines.extend(
        [
            "このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。",
            "",
            "生成: `karabiner-manager/scripts/export_mappings_md.py`",
        ]
    )
    return lines


def build_document(
    title: str,
    intro_lines: List[str],
    rows: List[Dict[str, str]],
) -> str:
    parts = [
        f"# {title}",
        "",
        *intro_lines,
        "",
        "---",
        "",
    ]
    for i, row in enumerate(rows, start=1):
        parts.append(row_section(i, row))
    return "\n".join(parts).rstrip() + "\n"


def export_markdown(config_path: Path, out_dir: Path) -> Tuple[int, List[Path]]:
    with config_path.open(encoding="utf-8") as f:
        data = json.load(f)
    profile = data["profiles"][0]
    global_rows, per_device = collect_rows(profile)

    written: List[Path] = []
    out_dir.mkdir(parents=True, exist_ok=True)

    gpath = out_dir / "global.md"
    gbody = build_document(
        "Karabiner マッピング（デバイス非依存）",
        [
            "次を含みます。",
            "",
            "- `device_if` 条件のない複合ルール",
            "- プロファイル直下の **fn_function_keys**（F1–F12）",
            "",
            "生成: `karabiner-manager/scripts/export_mappings_md.py`",
        ],
        global_rows,
    )
    gpath.write_text(gbody, encoding="utf-8")
    written.append(gpath)

    total = len(global_rows)
    sorted_keys = sorted(per_device.keys(), key=lambda x: (int(x[0]), int(x[1])))

    for vs, ps in sorted_keys:
        rows = per_device[(vs, ps)]
        fname = f"v{vs}_p{ps}.md"
        p = out_dir / fname
        body = build_document(
            f"Karabiner マッピング（vendor {vs} / product {ps}）",
            device_intro_lines(vs, ps, rows),
            rows,
        )
        p.write_text(body, encoding="utf-8")
        written.append(p)
        total += len(rows)

    idx_lines = [
        "# Karabiner マッピング一覧（インデックス）",
        "",
        "| ファイル | vendor_id | product_id | 件数 | 備考 |",
        "|----------|-----------|------------|------|------|",
        f"| [global.md](global.md) | — | — | {len(global_rows)} | デバイス非依存 + プロファイル fn キー |",
    ]
    for vs, ps in sorted_keys:
        fname = f"v{vs}_p{ps}.md"
        idx_lines.append(
            f"| [{fname}]({fname}) | {vs} | {ps} | {len(per_device[(vs, ps)])} | |"
        )
    idx_lines.extend(
        [
            "",
            f"**データ行合計:** {total}",
            "",
            "統合版: [all.md](all.md)",
            "",
            "生成: `karabiner-manager/scripts/export_mappings_md.py`",
        ]
    )
    idx_path = out_dir / "_index.md"
    idx_path.write_text("\n".join(idx_lines) + "\n", encoding="utf-8")
    written.append(idx_path)

    all_parts = [
        "# Karabiner マッピング（全件）",
        "",
        "デバイス別ファイルの連結です。目次は [_index.md](_index.md)。",
        "",
        "---",
        "",
        "## global.md",
        "",
        gbody,
        "---",
        "",
    ]
    for vs, ps in sorted_keys:
        fname = f"v{vs}_p{ps}.md"
        all_parts.append(f"## {fname}\n\n")
        all_parts.append((out_dir / fname).read_text(encoding="utf-8"))
        all_parts.append("\n---\n\n")
    all_path = out_dir / "all.md"
    all_path.write_text("".join(all_parts).rstrip() + "\n", encoding="utf-8")
    written.append(all_path)

    return total, written


def main() -> int:
    dir_override: Optional[Path] = None
    if len(sys.argv) >= 2:
        dir_override = Path(sys.argv[1]).expanduser()

    config = get_karabiner_config_path()
    if not config.exists():
        print(f"エラー: 設定が見つかりません: {config}", file=sys.stderr)
        return 1

    out_dir = dir_override or (Path.home() / ".config" / "karabiner" / "karabiner-manager" / "mappings_by_device")
    total, files = export_markdown(config, out_dir)
    n_dev = len(files) - 3
    print(f"✅ Markdown: global.md + {n_dev} デバイス + _index.md + all.md（データ {total} 件）")
    for p in files:
        print(f"   {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
