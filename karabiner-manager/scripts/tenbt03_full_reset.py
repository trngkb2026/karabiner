#!/usr/bin/env python3
"""TENBT03 (vendor=9427 / product=12427) の全カスタムルールを削除して
完全デフォルト状態に戻す。バックアップは呼び出し側で取得する前提。

- complex_modifications.rules から TENBT03 の device_if を含む manipulator を除去
- 除去後に manipulator が空になったルールは丸ごと削除
- profiles[].devices[] の該当エントリから simple_modifications / fn_function_keys を空配列化（エントリ自体は残す）
"""
import json
import os
import sys

SRC = os.path.expanduser("~/.config/karabiner/karabiner.json")
TARGET_V = 9427
TARGET_P = 12427


def main() -> int:
    with open(SRC) as f:
        cfg = json.load(f)

    removed_manips = []
    removed_sm = []
    removed_fn = []

    for prof in cfg.get("profiles", []):
        # 1) complex_modifications.rules
        new_rules = []
        for rule in prof.get("complex_modifications", {}).get("rules", []):
            new_manips = []
            for m in rule.get("manipulators", []):
                hit = False
                for c in m.get("conditions", []) or []:
                    if c.get("type") != "device_if":
                        continue
                    for ident in c.get("identifiers", []) or []:
                        if (
                            ident.get("vendor_id") == TARGET_V
                            and ident.get("product_id") == TARGET_P
                        ):
                            hit = True
                            break
                    if hit:
                        break
                if hit:
                    removed_manips.append(
                        {
                            "rule_desc": rule.get("description"),
                            "from": m.get("from"),
                        }
                    )
                else:
                    new_manips.append(m)
            if new_manips:
                rule["manipulators"] = new_manips
                new_rules.append(rule)
        prof["complex_modifications"]["rules"] = new_rules

        # 2) devices[] の simple_modifications / fn_function_keys
        for dev in prof.get("devices", []):
            ident = dev.get("identifiers", {})
            if (
                ident.get("vendor_id") == TARGET_V
                and ident.get("product_id") == TARGET_P
            ):
                if dev.get("simple_modifications"):
                    removed_sm.extend(dev["simple_modifications"])
                    dev["simple_modifications"] = []
                if dev.get("fn_function_keys"):
                    removed_fn.extend(dev["fn_function_keys"])
                    dev["fn_function_keys"] = []

    with open(SRC, "w") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=4)
        f.write("\n")

    print("=== 削除内容 ===")
    print(f"Complex manipulators: {len(removed_manips)} 件")
    for r in removed_manips:
        print(" ", r["rule_desc"], "|", json.dumps(r["from"], ensure_ascii=False))
    print(f"Simple modifications: {len(removed_sm)} 件")
    for s in removed_sm:
        print(" ", json.dumps(s, ensure_ascii=False))
    print(f"Fn function keys: {len(removed_fn)} 件")

    # 再読込で構文OKか検証
    with open(SRC) as f:
        json.load(f)
    print("post-apply json ok")

    # 残存確認
    print()
    print("=== 適用後の TENBT03 残存 ===")
    with open(SRC) as f:
        cfg2 = json.load(f)
    for prof in cfg2.get("profiles", []):
        hit_complex = 0
        for rule in prof.get("complex_modifications", {}).get("rules", []):
            for m in rule.get("manipulators", []):
                for c in m.get("conditions", []) or []:
                    if c.get("type") != "device_if":
                        continue
                    for ident in c.get("identifiers", []) or []:
                        if (
                            ident.get("vendor_id") == TARGET_V
                            and ident.get("product_id") == TARGET_P
                        ):
                            hit_complex += 1
        print(f"Complex manipulators 残存: {hit_complex}")
        for dev in prof.get("devices", []):
            ident = dev.get("identifiers", {})
            if (
                ident.get("vendor_id") == TARGET_V
                and ident.get("product_id") == TARGET_P
            ):
                print(
                    f"デバイスエントリ: 存在 / simple_modifications="
                    f"{len(dev.get('simple_modifications', []))} 件 / "
                    f"fn_function_keys={len(dev.get('fn_function_keys', []))} 件"
                )

    return 0


if __name__ == "__main__":
    sys.exit(main())
