# TENBT03（MCO）キーマップ一覧

Karabiner-Elements の設定（`karabiner.json`）における **TENBT03（MCO）Bluetooth テンキー**向けマッピングです。

## デバイス識別


| 項目         | 値                                                                                |
| ---------- | -------------------------------------------------------------------------------- |
| 製品例        | TENBT03（MCO）Bluetooth Tenkey Pad                                                 |
| vendor_id  | 9427                                                                             |
| product_id | 12427                                                                            |
| 備考         | 複合ルールはすべて `device_if` でこの端末に限定。`devices` では `is_keyboard` + `is_pointing_device` |


## 複合ルール

ルールグループ名: **TENBT03 (MCO) - カスタム設定**

表の **#** 列はこのドキュメント上の通し番号（1〜3）です。


### ファンクション・編集

| #   | 入力                                   | 出力・動作                                                |
| --- | ------------------------------------ | ---------------------------------------------------- |
| 1   | F2                                   | Shift+T, E, N, T, E, N, テンキー 8,2,2,3, Enter（1キーずつ送出） |
| 2   | F4                                   | Shift + F13                                          |
| 3   | Forward Delete（`delete_forward`、物理 DEL） | Space → Space → Space → Space → Enter（1キーずつ送出）           |

※ **F2** のマクロの **出力**にはテンキーコードが含まれますが、**物理テンキー各キ**の「押下→入力」の割り当ては別です（下表「未割り当て」参照）。


## 未割り当て一覧

`vendor_id` 9427 / `product_id` 12427 に **`device_if` 付き複合ルール** または **同端末の Simple Modifications** が無い入力の整理です（OS / アプリ既定どおり伝わります）。

**グローバル複合**（Space の単発/長押し、⌘W→スペース、⌃Space の IME トグルなど）は、端末を問わず掛かるため **この一覧には含めません**。


### この端末向けに割り当てている入力（対照）


| 入力（Event Viewer 想定）                         | 設定（TENBT03 専用）                                      |
| -------------------------------------------- | ------------------------------------------------- |
| `f2`                                         | 複合: マクロ（英字 + テンキー相当キー列 + Enter）                 |
| `f4`                                         | 複合: Shift+F13 **／** Simple: Spotlight（二重定義に注意） |
| `delete_forward`（Forward Delete / 物理 DEL 寄り） | 複合: Space×4 + Enter                               |
| `grave_accent_and_tilde`（半角/全角キー相当のことが多い）     | Simple: Consumer 音量上げ                             |


### 未割り当ての入力（TENBT03 専用ルールなし）


| カテゴリ    | 入力（`key_code` および修飾の目安）                               | 物理キー（参考・機種差あり） |
| ------- | ---------------------------------------------------- | --------------- |
| Esc     | `escape`                                             | Esc             |
| テンキー数字 | `keypad_0`〜`keypad_9`                                 | 0〜9            |
| テンキー   | `keypad_enter`                                       | Enter           |
| テンキー   | `keypad_period`                                      | `.`             |
| テンキー   | `keypad_slash`                                       | `/`             |
| テンキー   | `keypad_asterisk`                                    | `*`             |
| テンキー   | `keypad_hyphen`                                      | `-`             |
| テンキー   | `keypad_plus`                                        | `+`             |
| 括弧      | `8` + **Shift**（`mandatory` は多くの環境で `left_shift`）     | `(`             |
| 括弧      | `9` + **Shift**                                      | `)`             |
| 記号      | `hyphen` + **Shift**（JIS テンキーで `=` に相当することが多い）       | `=`             |
| 編集      | `delete_or_backspace`                                | BS              |
| 矢印      | `up_arrow` / `down_arrow` / `left_arrow` / `right_arrow` | ▲▼◀▶            |
| その他     | `tab`                                                | Tab             |
| 修飾      | `left_control`                                       | Ctrl/Cmd 相当     |
| 修飾      | `left_option` / `right_option`                       | Option（搭載されていれば） |
| 修飾      | `left_shift`（単独のリマップはなし。括弧・`=` と組み合わせで使用）        | Shift           |
| 特殊      | `keypad_num_lock` や `keypad_0` の連打など                         | 00 / NUM        |


- **NUM** はハードウェア処理のため Event Viewer に出ず、Karabiner でもリマップできないことがあります（メーカー仕様）。
- 物理ラベルは `karabiner-manager/references/device_mappings.md` の TENBT03 表に準拠。**実機では Karabiner-EventViewer で `key_code` を確認**してください（配列・ファームで差があります）。
- 本パッドに **左 Option** が無い／別コードで届く場合は、表に無くても Event Viewer の行をこの「未割り当て」側に読み替えてください。


## デバイス別 Simple Modifications


| 設定                                                                     |
| ---------------------------------------------------------------------- |
| F4 → Spotlight（`apple_vendor_keyboard_key_code`: spotlight）            |
| 半角/全角キー相当（`grave_accent_and_tilde`）→ Consumer 音量上げ（`volume_increment`） |


## システムショートカットとの関係

- Shift + F13・Spotlight などは **macOS のキーボードショートカット** の設定に依存します。


## 注意

- **F4** は複合ルール（Shift+F13）と Simple Modifications（Spotlight）の両方に定義されています。実際に効くのは Karabiner の処理順によるため、挙動を確実にしたいときはどちらかに統一することを推奨します。
- テンキーの **NUM** など、機種によっては OS にイベントが届かずリマップできないキーがあります。
- 同一プロファイルの **グローバル複合ルール**（Space の単発/長押し、⌘W → スペース、⌃Space の IME トグルなど）も、このキーボードからの入力に適用されます。
- 複合ルールの変更後は Karabiner-Elements が `karabiner.json` を読み直すまで反映されない場合があります。
