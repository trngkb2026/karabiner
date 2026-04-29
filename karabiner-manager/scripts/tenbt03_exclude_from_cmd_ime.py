#!/usr/bin/env python3
"""左⌘/右⌘ → IME（英数/かな）グローバルルールの device_unless に
TENBT03 (vendor=9427 / product=12427) を追加する。

- description 部分一致: '短押しで IME'（左→英数 / 右→かな）
- 対象: from.key_code が left_command / right_command のもの全 manipulator
- 既に 9427/12427 が追加されていれば idempotent
"""
import json
import os
import shutil
import sys
import time

SRC = os.path.expanduser("~/.config/karabiner/karabiner.json")
TARGET_V = 9427
TARGET_P = 12427


def main() -> int:
    # backup
    ts = time.strftime("%Y%m%d%H%M%S")
    bak = f"{SRC}.bak.tenbt03_cmd_ime_exclude_{ts}"
    shutil.copy2(SRC, bak)
    print(f"[backup] {bak}")

    with open(SRC) as f:
        cfg = json.load(f)

    touched = 0
    for prof in cfg.get("profiles", []):
        for rule in prof.get("complex_modifications", {}).get("rules", []):
            desc = rule.get("description", "")
            if "短押しで IME" not in desc:
                continue
            for m in rule.get("manipulators", []):
                frm = m.get("from", {}) or {}
                if frm.get("key_code") not in ("left_command", "right_command"):
                    continue
                conds = m.get("conditions", []) or []
                updated = False
                for c in conds:
                    if c.get("type") != "device_unless":
                        continue
                    idents = c.get("identifiers", []) or []
                    already = any(
                        i.get("vendor_id") == TARGET_V and i.get("product_id") == TARGET_P
                        for i in idents
                    )
                    if not already:
                        idents.append({"vendor_id": TARGET_V, "product_id": TARGET_P})
                        c["identifiers"] = idents
                        updated = True
                if updated:
                    touched += 1
                    print(
                        f"[update] rule='{desc}' from={json.dumps(frm, ensure_ascii=False)}"
                    )

    if touched == 0:
        print("[warn] 変更なし。ルールが見つからないか、すでに除外済み。")
        return 0

    with open(SRC, "w") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=4)
        f.write("\n")

    # 構文検証
    with open(SRC) as f:
        json.load(f)
    print(f"[ok] json syntax ok / 更新 manipulator: {touched} 件")

    # 適用後の確認ダンプ
    print()
    print("=== 適用後: 左⌘/右⌘ → IME の device_unless 一覧 ===")
    with open(SRC) as f:
        cfg2 = json.load(f)
    for prof in cfg2.get("profiles", []):
        for rule in prof.get("complex_modifications", {}).get("rules", []):
            if "短押しで IME" not in rule.get("description", ""):
                continue
            for m in rule.get("manipulators", []):
                frm = m.get("from", {}) or {}
                if frm.get("key_code") not in ("left_command", "right_command"):
                    continue
                for c in m.get("conditions", []) or []:
                    if c.get("type") == "device_unless":
                        idents = c.get("identifiers", []) or []
                        names = ",".join(
                            f"{i.get('vendor_id')}:{i.get('product_id')}" for i in idents
                        )
                        print(f"  {frm.get('key_code')} unless=[{names}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
