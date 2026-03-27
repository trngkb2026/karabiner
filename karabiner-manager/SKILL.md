---
name: karabiner-manager
description: |
  Karabiner-Elementsの設定管理スキル。複数デバイス（Ewin Tenkey, 8BitDo Zero 2, K02 BLE等）のキーマッピングを一括管理。
  マッピング変更、設定確認、バックアップ/復元に対応。
  使用場面：「Karabiner」「キーマッピング」「テンキー」「8BitDo」「K02」「キー設定」「マッピング変更」などのリクエスト時。
---

# Karabiner-Elements 設定管理

macOSのKarabiner-Elements設定を管理する。

## 設定ファイル

`~/.config/karabiner/karabiner.json`

## 管理対象デバイス

| デバイス名 | vendor_id | product_id | ルール名 |
|------------|-----------|------------|----------|
| Ewin Wireless Tenkey Pad | 1452 | 599 | Ewin Wireless Tenkey Pad - カスタム設定 |
| 8BitDo Zero 2 | 11720 | 36888 | 8BitDo Zero 2 - 全ボタン設定 |
| K02 BLE Keyboard | 1452 | 599 | K02 BLE Keyboard - 各種設定 |

## ワークフロー

### 1. 設定確認

1. karabiner.jsonを読み込む
2. `profiles[].complex_modifications.rules[]`からルールを抽出
3. デバイスごとにマッピングをテーブル表示

### 2. マッピング変更

1. 変更内容をヒアリング
2. 変更前後のdiffを提示

```diff
- "to": [{ "key_code": "old_key" }]
+ "to": [{ "key_code": "new_key", "modifiers": ["modifier"] }]
```

3. 承認後、karabiner.jsonを編集（Karabinerは自動検出）

### 3. バックアップ/復元

- **バックアップ**: `scripts/backup.py`を実行
- **復元**: `scripts/restore.py`を実行

## from句の書き方

```json
// 単体キー
"from": { "key_code": "keypad_plus" }

// 修飾キー必須（特定のShift）
"from": {
    "key_code": "8",
    "modifiers": { "mandatory": ["right_shift"] }
}

// 修飾キー必須（どちらのShiftでもOK）
"from": {
    "key_code": "9",
    "modifiers": { "mandatory": ["shift"], "optional": ["caps_lock"] }
}

// 修飾キー任意
"from": {
    "key_code": "up_arrow",
    "modifiers": { "optional": ["caps_lock"] }
}
```

## to句の書き方

```json
// 単一キー
{ "key_code": "spacebar" }
{ "key_code": "f11" }
{ "key_code": "print_screen" }

// 修飾キー付き
{ "key_code": "a", "modifiers": ["command"] }           // ⌘+A
{ "key_code": "v", "modifiers": ["command", "control"] } // ⌘+^+V
{ "key_code": "x", "modifiers": ["command", "shift"] }   // ⌘+Shift+X

// 連続入力
[
    { "key_code": "spacebar" },
    { "key_code": "spacebar" },
    { "key_code": "return_or_enter" }
]

// 特殊キー
{ "apple_vendor_keyboard_key_code": "spotlight" }
{ "consumer_key_code": "dictation" }
{ "shell_command": "pmset sleepnow" }
```

## 利用可能なkey_code

**基本キー**: spacebar, return_or_enter, escape, delete_or_backspace, delete_forward, tab

**修飾キー**: left_shift, right_shift, left_command, right_command, left_option, right_option, left_control, right_control

**テンキー**: keypad_0〜keypad_9, keypad_plus, keypad_hyphen, keypad_slash, keypad_period, keypad_asterisk, keypad_num_lock, keypad_enter

**ファンクション**: f1〜f12, print_screen

**矢印**: up_arrow, down_arrow, left_arrow, right_arrow

**その他**: a-z, 0-9, hyphen, comma

## キーコード確認方法

不明なキーはKarabiner-EventViewerで確認：
1. Karabiner-EventViewerを起動
2. 対象のキーを押す
3. `key_code`と`modifiers`を記録

## 詳細リファレンス

- デバイス別マッピング一覧: `references/device_mappings.md`
