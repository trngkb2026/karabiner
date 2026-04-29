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
| 7   | 右 Option  | Spotlight（`apple_vendor_keyboard_key_code`: spotlight）       |


---

## デバイス別 Simple Modifications


| 入力（from）  | 出力（to）                                                 |
| --------- | ------------------------------------------------------ |
| Caps Lock | 左 Option                                               |
| F1        | Print Screen（`print_screen`）                           |
| 左 Option  | Spotlight（`apple_vendor_keyboard_key_code`: spotlight） |
| 右 Option  | 音声入力（`consumer_key_code`: dictation）                   |


### 右 Option について

**Simple Modifications** では右 Option → 音声入力、**複合ルール**では右 Option → Spotlight と定義されています。実際に効く方は Karabiner の適用順に依存します。挙動を固定したい場合はどちらか一方にそろえることを推奨します。

---

## デバイス別 Fn キー（`fn_function_keys`）

この端末エントリで明示されているのは次のみです（いずれも F キーとしてそのまま扱う設定）。


| 入力  | 出力  |
| --- | --- |
| F1  | F1  |
| F2  | F2  |


プロファイル全体の `fn_function_keys`（F1〜F12 を F キーとして通す等）も併用されます。物理キーが「明るさ」などの特殊動作になる場合は、macOS の **キーボード**設定（F1/F2 を標準のキーとして使用）も合わせて確認してください。

---

## グローバル複合ルールとの関係（このキーボード）

次の **プロファイル共通** の複合ルールは、特に書かれていれば **このキーボードにも適用**されます。


| ルール概要                         | Magic Keyboard への扱い                                |
| ----------------------------- | -------------------------------------------------- |
| Space：単発でスペース／長押し・併用で Command | `**device_unless`（671/76）により対象外**。通常のスペースとして扱われます。 |
| ⌃Space：英数⇔かなトグル（内部変数）         | 端末限定なし（このキーボードからも有効）                               |


その他、プロファイル内の **X8 / TENBT03 / Ewin / Logitech 専用** ルールは `device_if` 付きのため、この Magic Keyboard には掛かりません。

---

## スペースキーがもたつくとき（設定は正常か）

`karabiner.json` を確認した限り、**次の点は意図どおりで矛盾はありません。**

- **Magic Keyboard（`vendor_id` 76 / `product_id` 671）** からの **素の Space** は、グローバルルール「Space: 単発でスペース / 長押し・併用で Command」の `**device_unless` により対象外**です。
- そのルールが **掛かっているキーボード**では、`to_if_alone_timeout_milliseconds` が **400ms** なので、**スペースが確定するまで最大約 0.4 秒待つ**挙動になり、タイプ時に「もたつく」感じが出やすいです（Karabiner の仕様）。

**だから「もたつく」と感じる場合、まず次を疑うのが筋が良いです。**


| 疑い                   | 内容                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **デバイス ID が一致していない** | Karabiner-EventViewer で Space 押下時の **Vendor ID / Product ID** を見て、**本当に 76 / 671 か**確認する。別モデル・接続の違いだと数字が変わり、`device_unless` が効かず **400ms ルールが掛かる**。 |
| **内蔵キーボードで打っている**    | 除外は **671/76 のみ**。MacBook **内蔵**はこのリストに無いので、**内蔵では Space 長押しルールが有効**のまま。外付け Magic だけ快適・内蔵だけ遅い、というパターンになり得る。                                         |
| **Karabiner 以外**     | IME の変換待ち、特定アプリのショートカット、他ユーティリティのキー処理など。一時的に Complex Modifications の該当ルールをオフにして比較すると切り分けしやすい。                                                       |


**⌃Space（IME トグル）** は Control 必須なので、**素の Space の遅延原因には通常なりません。**

---

## システムショートカットとの関係

- Shift + F13・Spotlight・Control + K などは **macOS のショートカット設定** やアプリのキーバインドに依存します。
- F4 の AppleScript は **アクセシビリティ（System Events）** の許可が必要な場合があります。

---

## 注意

- 物理ラベルと `key_code` の対応は機種差があります。**Karabiner-EventViewer** で実際のコードを確認してください。
- 複合ルール変更後は Karabiner-Elements が `karabiner.json` を読み直すまで反映されないことがあります。

