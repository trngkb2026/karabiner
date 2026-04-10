# デバイス別マッピング一覧

`karabiner.json` の **現在の定義**に合わせる。ルールの `description` と JSON の `to` が食い違う場合は JSON を正とし、備考に記す。

---

## X8 BLE Keyboard（vendor 1452 / product 599）

Ewin X8・K02 BLE・同一 VID/PID のテンキー等、**同じ識別子で見える機器はこのブロックを共有**する。ルール名は `X8 BLE Keyboard - カスタム設定`。

### Ewin Wireless テンキー（物理キー → 入力キーコード）

| 物理キー | 入力キーコード |
|----------|----------------|
| PgUp | up_arrow + left_command |
| PgDn | down_arrow + left_command |
| Home | left_arrow + left_command |
| ( | 8 + shift |
| ) | 9 + shift |
| 次のモニター | hyphen + shift |
| Num | keypad_num_lock |
| Delete | delete_forward |
| Tab | tab |
| + | keypad_plus |
| - | keypad_hyphen |
| / | keypad_slash |
| . | keypad_period |
| ▲▼◀▶ | up/down/left/right_arrow |
| BT | comma |
| 0-9 | 0-9 |

### テンキー向けマッピング（`karabiner.json` 準拠）

| 物理キー | 入力 | 出力 |
|----------|------|------|
| PgUp | up_arrow + ⌘ | Clipy（⌘+⌃+V） |
| PgDn | down_arrow + ⌘ | Space×4+Enter |
| Home | left_arrow + ⌘ | カット（⌘+X） |
| ( | 8 + Shift | BTT 起動（f11） |
| ) | 9 + Shift | 1Password（⌘+Shift+X） |
| Num | keypad_num_lock | ミュート（⌘+Shift+M） |
| Delete | delete_forward | スリープ |
| Tab | tab | 全選択（⌘+A） |
| + | keypad_plus | Shift+Enter |
| - | keypad_hyphen | ⌘+, |
| / | keypad_slash | Alfred（Ctrl+A） |
| 次のモニター | hyphen + Shift | F3 |
| ▲ | up_arrow | 音声入力 |
| . | keypad_period | カンマ |
| ◀ | left_arrow | Backspace |
| ▶ | right_arrow | print_screen |
| ▼ | down_arrow | スペース |
| BT | comma | Spotlight |
| 0-9 | 0-9 | keypad_0〜9（半角） |

### ミニキーボード（K02 等）で共通する設定

- 数字行 0-9 → `keypad_0`〜`keypad_9`（Shift 併用時は記号のまま等、ルール参照）
- **Caps Lock**: 変数 `x8_ble_caps_ime` による英数⇔かなトグル
- **ポインティング面のボタン**: 音声入力 / Enter / ⌘+左クリック など（ルール内 `description` 参照）
- **Consumer キー**: Mission Control・音量下げは `o`→`k`→`return`、音量上げは `k`→`a`→`n`→`r`→`y`→`o`→👍 など（ルール参照）
- **左・右 Command** → F13

別ルール **X8 BLE: Fn+トラックパッド移動→スクロール**（`mouse_motion_to_scroll`, `speed_multiplier` 2.0）が 1452:599 のポインティングに適用。

---

## 8BitDo Zero 2（vendor 11720 / product 36888）

ルール名: `8BitDo Zero 2 - 全ボタン設定`。

**注意**: ルール全体に **`"enabled": false`** が付いているため、有効化するまでマッピングは動かない。

### ボタンと入力キーコード（キーボードモード）

| ボタン | 入力 key_code |
|--------|----------------|
| ↑ | c |
| ↓ | d |
| ← | e |
| → | f |
| Y | i |
| A | g |
| X | h |
| B | j |
| L | k |
| R | m |
| Select | n |
| Start | o |

### 現在のマッピング（`karabiner.json` 準拠）

| ボタン | 出力 |
|--------|------|
| ↑ | →矢印 |
| ↓ | ←矢印 |
| ← | ↑矢印 |
| → | ↓矢印 |
| Y | ⌘+Shift+Option+H |
| A | **print_screen**（ルール説明は「F13」だが `to` は print_screen） |
| X | End |
| B | Home |
| L | Backspace（delete_or_backspace） |
| R | Shift+Enter |
| Select | 音声入力（dictation） |
| Start | Escape |

---

## 8BitDo Micro 等（vendor 11720 / product 36897）

複合ルール `8BitDo Zero 2` とは **PID が異なる**。接続例では「8BitDo Micro gamepad」が 36897。

- Keychron Link-KM 系ルールの **`device_unless` 除外リストに 36897 が含まれる**（Zero 2 と同列扱いで、Link-KM 側ルールは当たらない）。
- `devices[]` で **f20 → dictation** などの `simple_modifications` あり（`karabiner.json` の該当エントリ参照）。

---

## Magic Keyboard（vendor 76 / product 671）

ルール名: `Magic Keyboard - カスタム設定`。

| 入力 | 出力（要約） |
|------|----------------|
| F2 | Shift+F13 |
| F3 | ⌃+K |
| F4 | Tenten8223 を 1 文字ずつ + Return（osascript） |
| F7 | Option+H |
| F19 | スリープ（pmset） |
| 右 Control | Space×4+Enter |
| 右 Option | Spotlight |

`profiles[].devices[]` 側に **Caps→Option**、**F1→print_screen** などの simple_modifications もある（JSON 参照）。

---

## Logitech USB Receiver（vendor 1133 / product 50503）

- **Block do_not_disturb**: `consumer_key_code` / `key_code` の do_not_disturb を破棄
- キーボード・ポインティングの個別設定は `devices[]` を参照

---

## Keychron Link-KM - カスタム設定

**`device_if`** で **`vendor_id` 13364** のみ（メインキーボードは **Bluetooth 接続に一本化**。USB / 2.4GHz ドングル用の `devices[]`・複合ルールの追加 OR は削除済み）。

内容は F キー・メディアキー・Consumer キーの大量の置換（F1→F13、輝度、**F3→Tenten8223+Enter（osascript）**、F4→F9、**F9→⌃K**、F5/F7/F8、**Insert→F6**、再生/早送り、Forward Delete、**Caps→Backspace・Enter は既定・右 Shift 単独→音声入力・右 Option→Space×4+Enter** など）。詳細は `karabiner.json` の `Keychron Link-KM - カスタム設定` ブロックを一覧するのが確実。

---

## グローバル（複数デバイス）

| ルール概要 | メモ |
|------------|------|
| Space 単発 / 長押し・併用 | Magic Keyboard（76/671）**以外**で ⌘ 系とスペースの切り替え |
| 左⌘ / 右⌘ 単独短押し | 英数（`japanese_eisuu`）/ かな（`japanese_kana`）。**X8 BLE（1452/599）以外**（`lazy` で ⌘ 併用は維持） |
| ⌃Space | `ctrl_space_ime_toggle` で英数⇔かな |
| ⌘W | スペース |
