# Keychron Link-KM キーマップ一覧

> **反映元:** `~/.config/karabiner/karabiner.json`（`karabiner-manager/` の 1 階層上にあるファイル）。**更新: 2026-04-04**（内容は JSON が正本）。

## デバイス情報

| 項目        | 値                |
| --------- | ---------------- |
| 製品        | Keychron Link-KM |
| vendor_id | 13364 (0x3434)   |
| product_id | 1844 |
| 接続        | Bluetooth        |

## Complex Modifications（Keychron Link-KM - カスタム設定）

`device_if` vendor_id=13364 のみ。

### ファンクション行

| 物理キー | 出力 |
|----------|------|
| F1 (輝度↓) | F13 (スクショ) |
| F2 (輝度↑) | Shift+F13 (動画スクショ) |
| F3 (Mission Control) | Tenten8223+Enter (osascript) |
| F4 (Spotlight/Launchpad) | F9 |
| F5 (キーボード輝度↓/音声入力) | Option+H |
| F6 (キーボード輝度↑) | F6 |
| F7 (巻き戻し) | Option+V |
| F8 (早送り/再生) | Shift+Option+V |
| F9 | Control+K |

### その他

| 物理キー | 出力 |
|----------|------|
| Insert | F6 |
| 音量↓ | Option+V |
| 音量↑ | Shift+Option+V |
| Forward Delete | Space×4+Enter |
| Caps Lock | Backspace |
| 右Shift (単独タップ) | 音声入力 (dictation) |
| 右Option | Space×4+Enter |

### 注意事項

- Keychron Mac モードではファンクション行が **Consumer キー**として届く。`key_code: f1` だけでは不十分で、Consumer / Apple vendor 側にも定義が必要
- `device_if` で vendor_id のみ指定（`is_keyboard` は付けない）。F行が別 HID として届く場合のマッチ漏れ防止
- F3 の osascript にはアクセシビリティ許可が必要

## グローバル複合ルールとの関係

以下のルールは Keychron でも有効（デバイス条件なし or Keychron を除外していない）:

| ルール | メモ |
|--------|------|
| ⌘ 短押しで IME（左→英数 / 右→かな）（X8 BLE / TENBT03 以外） | `to_if_alone_timeout_milliseconds` 300 |
| プロファイル直下の Fn キー | F1-F12 を F キーとして扱う |
