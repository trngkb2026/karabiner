# デバイス別マッピング一覧

## Ewin Wireless Tenkey Pad

**デバイス情報**: vendor_id=1452, product_id=599

### 物理キーと入力キーコードの対応

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

### 現在のマッピング

| 物理キー | 入力 | 出力 |
|----------|------|------|
| PgUp | up_arrow + ⌘ | Clipy (⌘+^+V) |
| PgDn | down_arrow + ⌘ | Space×4+Enter |
| Home | left_arrow + ⌘ | カット (⌘+X) |
| ( | 8 + Shift | BTT起動 (f11) |
| ) | 9 + Shift | 1Password (⌘+Shift+X) |
| Num | keypad_num_lock | ミュート (⌘+Shift+M) |
| Delete | delete_forward | スリープ |
| Tab | tab | 全選択 (⌘+A) |
| + | keypad_plus | Shift+Enter |
| - | keypad_hyphen | ⌘+, |
| / | keypad_slash | Alfred (Ctrl+A) |
| 次のモニター | hyphen + Shift | F3 |
| ▲ | up_arrow | 音声入力 |
| . | keypad_period | カンマ |
| ◀ | left_arrow | Backspace |
| ▶ | right_arrow | print_screen |
| ▼ | down_arrow | スペース |
| BT | comma | スポットライト |
| 0-9 | 0-9 | keypad_0-9 (半角) |

---

## 8BitDo Zero 2

**デバイス情報**: vendor_id=11720, product_id=36888

### ボタンと入力キーコードの対応

| ボタン | 入力キーコード |
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

### 現在のマッピング

| ボタン | 出力 |
|--------|------|
| ↑ | テンキー3+Enter |
| ↓ | テンキー1+Enter |
| ← | テンキー2+Enter |
| → | テンキー4+Enter |
| Y | Escape |
| A | スペース |
| X | Clipy (⌘+^+V) |
| B | ⌘+Shift+2 |
| L | 右Shift |
| R | Backspace |
| Select | 全選択 (⌘+A) |
| Start | カット (⌘+X) |

---

## K02 BLE Keyboard

**デバイス情報**: vendor_id=1452, product_id=599

### 数字キー半角化

0-9キーをkeypad_0-9に変換（Shift併用時は記号のまま）

### Caps Lock → 英数/かなトグル

- 日本語入力中: japanese_eisuu（英数）
- 英語入力中: japanese_kana（かな）

### 特殊ボタン

| ボタン | 出力 |
|--------|------|
| 地球ボタン | Spotlight |
| ボタン2 | Space×4+Enter |
| left_control | 無効化 |
