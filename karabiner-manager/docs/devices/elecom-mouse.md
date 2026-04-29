# ELECOM マウス（vendor 1390 / product 342）

`system_profiler` で **Vendor 0x056E = Elecom**、**Product 0x0156**、Minor Type: Mouse として検出された Bluetooth マウス。
具体的な製品名は未確定（EX-G / DEFT PRO 等の Elecom 高機能マウスの一種と推測）。

## デバイス識別

| 項目         | 値          |
| ------------ | ----------- |
| vendor_id    | 1390（0x056E = Elecom） |
| product_id   | 342（0x0156）           |
| 識別子       | `is_pointing_device: true` |
| 接続         | Bluetooth |
| 製品例       | ELECOM 製マウス（型番未確定） |

## Complex Modifications

**なし**（`device_if` で 1390:342 を指定するルールは無い）。

## Simple Modifications（10件）

`profiles[].devices[]` 内のデバイスエントリに登録されている device_simple_modification。

### マウスボタン

| From | To | 用途の推測 |
|------|------|---------|
| `pointing_button: button1` | `1` + `option`（⌥1） | 用途未確定 |
| `pointing_button: button2` | `v` + `shift` + `option`（⇧⌥V） | 用途未確定 |
| `pointing_button: button3` | `return_or_enter` | Enter |
| `pointing_button: button4` | `c` + `command`（⌘C） | コピー |
| `pointing_button: button5` | `v` + `command`（⌘V） | ペースト |

### Consumer キー（メディアキー）

| From | To |
|------|------|
| `consumer_key_code: play_or_pause` | `key_code: fn` |
| `consumer_key_code: scan_previous_track` | `tab` + `shift` + `control`（⇧⌃Tab） |
| `consumer_key_code: scan_next_track` | `tab` + `control`（⌃Tab） |
| `consumer_key_code: volume_increment` | `return_or_enter` |
| `consumer_key_code: volume_decrement` | `delete_or_backspace` + `command`（⌘Backspace） |

## 備考

- ELECOM の Bluetooth マウスは**ファーム更新や接続モードで VID/PID が変わることがある**。EventViewer で要確認。
- GUIでは `リラコン` として表示しているが、実機型番は未確定。物理ボタンと `button1`〜`button5` の対応は EventViewer で再確認する。
- `play_or_pause` → `fn` は、`fn` 単独送出が他アプリで何かのトリガーになっている可能性あり（未検証）。
