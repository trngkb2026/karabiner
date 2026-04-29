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
| `pointing_button: button1` | `pointing_button: button1` | 左クリック（恒等マッピング・意図不明、動作確認推奨） |
| `pointing_button: button2` | `pointing_button: button2` | 右クリック（恒等マッピング） |
| `pointing_button: button3` | `c` + `command`（⌘C） | コピー |
| `pointing_button: button4` | `s` + `control`（⌃S） | 進む・戻る系を別機能に置換 |
| `pointing_button: button5` | `v` + `control`（⌃V） | 同上 |

### Consumer キー（メディアキー）

| From | To |
|------|------|
| `consumer_key_code: play_or_pause` | `key_code: fn` |
| `consumer_key_code: scan_previous_track` | `delete_or_backspace` + `command`（⌘Del） |
| `consumer_key_code: scan_next_track` | `return_or_enter` + `command`（⌘Enter） |
| `consumer_key_code: volume_increment` | `up_arrow` |
| `consumer_key_code: volume_decrement` | `down_arrow` |

## 備考

- ELECOM の Bluetooth マウスは**ファーム更新や接続モードで VID/PID が変わることがある**。EventViewer で要確認。
- `button1` / `button2` の恒等マッピング（入力＝出力）は、Karabiner で「そのボタンは他ルールの影響を受けない」ことを明示する目的か、あるいは意図せず残った設定と思われる。消すかどうかは要判断。
- `play_or_pause` → `fn` は、`fn` 単独送出が他アプリで何かのトリガーになっている可能性あり（未検証）。
