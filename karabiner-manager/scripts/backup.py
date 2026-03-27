#!/usr/bin/env python3
"""
Karabiner-Elements設定のバックアップスクリプト
タイムスタンプ付きでバックアップを作成する
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

def get_karabiner_config_path():
    return Path.home() / ".config" / "karabiner" / "karabiner.json"

def get_backup_dir():
    return Path.home() / ".config" / "karabiner" / "backups"

def backup():
    config_path = get_karabiner_config_path()
    backup_dir = get_backup_dir()

    if not config_path.exists():
        print(f"エラー: 設定ファイルが見つかりません: {config_path}")
        return False

    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"karabiner_{timestamp}.json"

    shutil.copy2(config_path, backup_path)
    print(f"✅ バックアップ完了: {backup_path}")

    # バックアップ一覧を表示
    backups = sorted(backup_dir.glob("karabiner_*.json"), reverse=True)
    print(f"\n📁 バックアップ一覧 ({len(backups)}件):")
    for i, b in enumerate(backups[:5]):
        print(f"   {i+1}. {b.name}")
    if len(backups) > 5:
        print(f"   ... 他{len(backups)-5}件")

    return True

if __name__ == "__main__":
    backup()
