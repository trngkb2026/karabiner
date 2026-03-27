#!/usr/bin/env python3
"""
Karabiner-Elements設定の復元スクリプト
バックアップから設定を復元する
"""

import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

def get_karabiner_config_path():
    return Path.home() / ".config" / "karabiner" / "karabiner.json"

def get_backup_dir():
    return Path.home() / ".config" / "karabiner" / "backups"

def list_backups():
    backup_dir = get_backup_dir()
    if not backup_dir.exists():
        print("バックアップが見つかりません")
        return []

    backups = sorted(backup_dir.glob("karabiner_*.json"), reverse=True)
    if not backups:
        print("バックアップが見つかりません")
        return []

    print("📁 利用可能なバックアップ:")
    for i, b in enumerate(backups):
        size = b.stat().st_size / 1024
        print(f"   {i+1}. {b.name} ({size:.1f}KB)")

    return backups

def restore(backup_index=None):
    config_path = get_karabiner_config_path()
    backups = list_backups()

    if not backups:
        return False

    if backup_index is None:
        print("\n復元するバックアップの番号を指定してください")
        print("使用法: python restore.py <番号>")
        return False

    try:
        idx = int(backup_index) - 1
        if idx < 0 or idx >= len(backups):
            print(f"エラー: 無効な番号です (1-{len(backups)})")
            return False
    except ValueError:
        print("エラー: 数字を指定してください")
        return False

    backup_path = backups[idx]

    # 現在の設定をバックアップ
    if config_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pre_restore_backup = get_backup_dir() / f"karabiner_pre_restore_{timestamp}.json"
        shutil.copy2(config_path, pre_restore_backup)
        print(f"📦 復元前バックアップ: {pre_restore_backup.name}")

    # 復元
    shutil.copy2(backup_path, config_path)
    print(f"✅ 復元完了: {backup_path.name}")
    print("   Karabiner-Elementsが自動で変更を検出します")

    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        restore(sys.argv[1])
    else:
        restore()
