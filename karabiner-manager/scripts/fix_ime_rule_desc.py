#!/usr/bin/env python3
"""Fix description of `⌘ 短押しで IME` rule to reflect TENBT03 exclusion.

- Before: "...（X8 BLE キーボード以外）"
- After:  "...（X8 BLE / TENBT03 以外）"

Idempotent: if the description is already correct, nothing is written.
Always writes a timestamped backup before modifying.
"""
import json
import os
import shutil
import sys
import time

SRC = os.path.expanduser("~/.config/karabiner/karabiner.json")
OLD = "（X8 BLE キーボード以外）"
NEW = "（X8 BLE / TENBT03 以外）"


def main() -> int:
    with open(SRC, encoding="utf-8") as f:
        data = json.load(f)

    changed = 0
    for prof in data.get("profiles", []):
        for rule in prof.get("complex_modifications", {}).get("rules", []):
            desc = rule.get("description", "")
            if "短押しで IME" in desc and OLD in desc:
                rule["description"] = desc.replace(OLD, NEW)
                changed += 1

    if changed == 0:
        print("NO_CHANGE (description already up to date)")
        return 0

    bak = f"{SRC}.bak.ime_rule_desc_{time.strftime('%Y%m%d%H%M%S')}"
    shutil.copy2(SRC, bak)

    with open(SRC, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.write("\n")

    print(f"BACKUP: {bak}")
    print(f"CHANGED: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
