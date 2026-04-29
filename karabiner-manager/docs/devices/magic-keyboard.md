# Apple キーボード（Magic Keyboard）キーマップ一覧

Karabiner-Elements の設定（`karabiner.json`）における **Apple Magic Keyboard**（このリポジトリでは `vendor_id` 76 / `product_id` 671 として登録）向けマッピングです。

## デバイス識別


| 項目         | 値                                 |
| ---------- | --------------------------------- |
| 製品例        | Apple Magic Keyboard（Bluetooth 等） |
| vendor_id  | 76                                |
| product_id | 671                               |
| 備考         | 複合ルールはすべて `device_if` でこの端末に限定    |


別モデル（Vendor / Product が異なる Magic Keyboard）を使う場合は、Karabiner-Elements の **Devices** で実値を確認し、`karabiner.json` の `identifiers` に追加してください。

---

## 複合ルール

ルールグループ名: **Magic Keyboard - カスタム設定**


| #   | 入力        | 出力・動作                                                        |
| --- | --------- | ------------------------------------------------------------ |
| 1   | F2        | Shift + F13                                                  |
| 2   | F3        | Control + K                                                  |
| 3   | F4        | `Tenten8223` を 1 文字ずつ入力 → Enter（AppleScript / System Events） |
| 4   | F7        | Option（左）+ H                                                 |
| 5   | F19       | `pmset sleepnow`（スリープ）                                       |
| 6   | 右 Control | Space × 4 → Enter（修飾キー任意は `optional: any`）                   |


---

## デバイス別 Simple Modifications


| 入力（from）  | 出力（to）                                                 |
| --------- | ------------------------------------------------------ |
| Caps Lock | 左 Option                                               |
| F1        | Print Screen（`print_screen`）                           |
| 左 Option  | Spotlight（`apple_vendor_keyboard_key_code`: spotlight） |
| 右 Option  | 音声入力（`consumer_key_code`: dictation）                   |


## デバイス別 Fn キー（`fn_function_keys`）

この端末エントリで明示されている Fn キー設定はありません。


プロファイル全体の `fn_function_keys`（F1〜F12 を F キーとして通す等）も併用されます。物理キーが「明るさ」などの特殊動作になる場合は、macOS の **キーボード**設定（F1/F2 を標準のキーとして使用）も合わせて確認してください。

---

## グローバル複合ルールとの関係（このキーボード）

次の **プロファイル共通** の複合ルールは、特に書かれていれば **このキーボードにも適用**されます。


| ルール概要                         | Magic Keyboard への扱い                                |
| ----------------------------- | -------------------------------------------------- |
現在のグローバル複合ルールは、左Command/右Commandの単独短押しIME切替とプロファイル直下の Fn キーです。その他、プロファイル内の **X8 / TENBT03 / Logitech 専用** ルールは `device_if` 付きのため、この Magic Keyboard には掛かりません。

---

## システムショートカットとの関係

- Shift + F13・Spotlight・Control + K などは **macOS のショートカット設定** やアプリのキーバインドに依存します。
- F4 の AppleScript は **アクセシビリティ（System Events）** の許可が必要な場合があります。

---

## 注意

- 物理ラベルと `key_code` の対応は機種差があります。**Karabiner-EventViewer** で実際のコードを確認してください。
- 複合ルール変更後は Karabiner-Elements が `karabiner.json` を読み直すまで反映されないことがあります。
