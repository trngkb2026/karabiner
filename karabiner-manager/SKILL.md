---
name: karabiner-manager
description: |
  Karabiner-Elementsの設定管理スキル。複数デバイス（Magic Keyboard、X8 BLE / K02 / Ewin テンキー、Logitech USB Receiver、8BitDo Zero 2 / Micro(36897)、Keychron Link-KM・B3 Pro 等）のキーマッピングを一括管理。
  マッピング変更、設定確認、バックアップ/復元に対応。
  使用場面：「Karabiner」「キーマッピング」「テンキー」「8BitDo」「8BitDo Micro」「K02」「Ewin」「X8」「ミニキーボード」「Magic Keyboard」「Keychron」「Link-KM」「B3 Pro」「Logitech」「キー設定」「マッピング変更」「ゲームパッド」「コントローラー設定」などのリクエスト時。
---

# Karabiner-Elements 設定管理

macOS の Karabiner-Elements 設定を管理する。デバイス ID は EventViewer で確認し、次表はリポジトリの `karabiner.json` に合わせたもの（ルールの `description` を正とする）。

## 設定ファイル

`~/.config/karabiner/karabiner.json`

## 管理対象デバイス（complex_modifications / devices）

| デバイス（ルール名・役割） | vendor_id | product_id | 備考 |
|---------------------------|-----------|------------|------|
| Magic Keyboard - カスタム設定 | 76 | 671 | Apple Bluetooth キーボード |
| X8 BLE Keyboard - カスタム設定 | 1452 | 599 | Ewin X8 / K02 など **同一 VID/PID** の BLE（キーボード＋トラックパッドとして認識される構成あり） |
| Block do_not_disturb …（Logitech USB Receiver） | 1133 | 50503 | レシーバー経由のキーボード／ポインティング |
| 8BitDo Zero 2 - 全ボタン設定 | 11720 | 36888 | 複合ルール。**現状ルールに `enabled: false`**（有効化まで未適用） |
| Keychron Link-KM - カスタム設定 | 13364 | （複合ルールは `device_if`・PID なし） | メインキーボードは **Bluetooth 前提**。USB/ドングル用 PID 専用行は削除済み（`docs/README.md`） |
| 8BitDo Micro 等（36897） | 11720 | 36897 | Zero 2 とは別 PID。`devices` の simple_modifications。一部グローバルルールの `device_unless` 除外対象 |
| Keychron（devices の simple_modifications） | 13364 | （`is_keyboard` のみ・PID なし） | `grave_accent_and_tilde` → 音量 など |
| TENBT03 等テンキー（devices の simple_modifications） | 9427 | 12427 | 上記と別デバイス。**Keychron 複合ルールの対象外** |

## デバイス横断・その他のルール

`complex_modifications` にはデバイス専用以外に、例えば次がある（内容は `karabiner.json` を確認）：

- 左⌘ / 右⌘ 単独短押しによる IME 切替
- X8 BLE: Fn＋トラックパッド移動 → スクロール

## ワークフロー

### 0. デバイス選択（最初に必ず実行）

スキル起動時、ユーザーの指示からデバイスが特定できない場合は、以下の選択肢を提示して対象デバイスを確認する:

1. **Magic Keyboard** (76:671)
2. **X8 BLE / K02** (1452:599)
3. **Keychron Link-KM** (13364)
4. **8BitDo Zero 2** (11720:36888)
5. **8BitDo Micro** (11720:36897)
6. **TENBT03 テンキー** (9427:12427)
7. **グローバル（デバイス横断）**

ユーザーが「Keychron」「テンキー」等のキーワードで指定済みの場合はスキップ。

### 1. 設定確認

1. `karabiner.json` を読み込む
2. `profiles[].complex_modifications.rules[]` からルールを抽出
3. `conditions` の `device_if` / `device_unless` と `identifiers` をデバイス名と突き合わせる
4. デバイスごとにマッピングをテーブル表示

### 2. マッピング変更

1. 変更内容をヒアリング
2. 変更前後の diff を提示

```diff
- "to": [{ "key_code": "old_key" }]
+ "to": [{ "key_code": "new_key", "modifiers": ["modifier"] }]
```

3. 承認後、`karabiner.json` を編集（Karabiner は自動検出）

### 3. バックアップ/復元

- **バックアップ**: `karabiner-manager/scripts/backup.py` を実行
- **復元**: `karabiner-manager/scripts/restore.py` を実行

## from 句の書き方

```json
// 単体キー
"from": { "key_code": "keypad_plus" }

// 修飾キー必須（特定の Shift）
"from": {
    "key_code": "8",
    "modifiers": { "mandatory": ["right_shift"] }
}

// 修飾キー必須（どちらの Shift でも可）
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

## to 句の書き方

```json
// 単一キー
{ "key_code": "spacebar" }
{ "key_code": "f11" }
{ "key_code": "print_screen" }

// 修飾キー付き
{ "key_code": "a", "modifiers": ["command"] }
{ "key_code": "v", "modifiers": ["command", "control"] }
{ "key_code": "x", "modifiers": ["command", "shift"] }

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

## 利用可能な key_code（よく使うもの）

**基本**: spacebar, return_or_enter, escape, delete_or_backspace, delete_forward, tab

**修飾**: left_shift, right_shift, left_command, right_command, left_option, right_option, left_control, right_control

**テンキー**: keypad_0〜keypad_9, keypad_plus, keypad_hyphen, keypad_slash, keypad_period, keypad_asterisk, keypad_num_lock, keypad_enter

**ファンクション**: f1〜f12, print_screen

**矢印**: up_arrow, down_arrow, left_arrow, right_arrow

**その他**: a-z, 0-9, hyphen, comma

## キーコード確認方法

不明なキーは Karabiner-EventViewer で確認する。

1. Karabiner-EventViewer を起動
2. 対象キーを押す
3. `key_code` と `modifiers` を記録

## 詳細リファレンス

- デバイス一覧・接続例・グローバルルール: `karabiner-manager/docs/README.md`
- 名前付き変数（IME トグル等）: `karabiner-manager/docs/variables.md`
- グローバル複合ルール（デバイス非依存）: `karabiner-manager/docs/global-rules.md`
- デバイス別マッピング: `karabiner-manager/docs/devices/*.md`（`karabiner.json` と矛盾する場合は JSON を正とする）
  - TENBT03: `docs/devices/tenbt03.md` / X8 BLE: `docs/devices/x8-ble-keyboard.md` / Magic Keyboard: `docs/devices/magic-keyboard.md`
  - Keychron Link-KM: `docs/devices/keychron-link-km.md` / Logitech Receiver: `docs/devices/logitech-receiver.md`
  - 8BitDo Zero 2: `docs/devices/8bitdo-zero2.md` / 8BitDo Micro: `docs/devices/8bitdo-micro.md`
- 実機写真: `karabiner-manager/docs/assets/`（`tenbt03.jpg` / `ewin-x8.png`）
- 過去の調査レポート: `karabiner-manager/docs/archive/`
