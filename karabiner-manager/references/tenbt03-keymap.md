# TENBT03（MCO）キーマップ一覧

> **運用上の注意（2026-04）:** **Keychron Link-KM** の複合ルールは **`device_if` で `vendor_id` 13364 のみ**（Bluetooth 前提・USB/ドングル用 PID 行は削除済み）。**TENBT03（9427 / 12427）には複合ルールは掛からない**（`devices[]` の Simple Mod のみ）。割り当ての正本は [keychron-link-km-keymap.md](./keychron-link-km-keymap.md) です。  
> このファイルは、**物理 TENBT03 テンキー**のキー配置メモとして残しています。

Karabiner-Elements の設定（`karabiner.json`）における **TENBT03（MCO）Bluetooth テンキー**向けの参考メモです。

## デバイス識別


| 項目         | 値                                                                                |
| ---------- | -------------------------------------------------------------------------------- |
| 製品例        | TENBT03（MCO）Bluetooth Tenkey Pad                                                 |
| vendor_id  | 9427                                                                             |
| product_id | 12427                                                                            |
| 備考         | **複合ルールは掛からない**（Keychron 専用）。`devices[]` では `is_keyboard` + `is_pointing_device` + Simple Mod（バッククォート→音量 等） |


## 複合ルール（`karabiner.json` の実体）

**Keychron Link-KM - カスタム設定**は **TENBT03 には適用されない**（`vendor_id` が異なるため）。Keychron 側の **F1〜F8・delete_forward** などは [keychron-link-km-keymap.md](./keychron-link-km-keymap.md) を参照。

**以前 TENBT03 向けに使っていた例（参考・現在の JSON とは異なる）**

| 入力 | 出力例（旧） |
| ---- | ------------ |
| F2 | Tenten マクロ（英字 + テンキー列 + Enter） |
| F4 | Shift + F13 |
| Forward Delete | Space×4 + Enter（**現在も Keychron 設定に残存**） |


## 未割り当て一覧

`vendor_id` 9427 / `product_id` 12427 向けの **`device_if` 付き複合ルールは無い**（`devices[]` の Simple Modifications のみ）。下表は **複合で触っていないキー**の整理（OS / アプリ既定どおり伝わります）。

**グローバル複合**（Space の単発/長押し、⌘W→スペース、⌃Space の IME トグルなど）は、端末を問わず掛かるため **この一覧には含めません**。


### この端末向けに割り当てている入力（対照）


| 入力（Event Viewer 想定）                         | 設定（TENBT03・`devices[]`）                          |
| -------------------------------------------- | ------------------------------------------------- |
| `grave_accent_and_tilde`（半角/全角キー相当のことが多い）     | Simple: Consumer 音量上げ                             |

※ `f2` / `f4` / `delete_forward` などの複合マクロは **Keychron Link-KM（13364）専用**。TENBT03 では **OS 既定**。


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
| 半角/全角キー相当（`grave_accent_and_tilde`）→ Consumer 音量上げ（`volume_increment`） |


## システムショートカットとの関係

- Spotlight などは **macOS のキーボードショートカット** の設定に依存します。


## 注意

- TENBT03 の `devices[]` には **F4 → Spotlight は入っていない**（Keychron 側の複合ルールもこの端末には掛からない）。
- テンキーの **NUM** など、機種によっては OS にイベントが届かずリマップできないキーがあります。
- 同一プロファイルの **グローバル複合ルール**（Space の単発/長押し、⌘W → スペース、⌃Space の IME トグルなど）も、このキーボードからの入力に適用されます。
- 複合ルールの変更後は Karabiner-Elements が `karabiner.json` を読み直すまで反映されない場合があります。
