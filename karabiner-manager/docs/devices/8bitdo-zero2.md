# 8BitDo Zero 2（vendor 11720 / product 36888）

小型ゲームパッド **8BitDo Zero 2** をキーボードモードで使う場合のマッピング。

## デバイス識別

| 項目         | 値         |
| ------------ | ---------- |
| vendor_id    | 11720      |
| product_id   | 36888      |
| 製品例       | 8BitDo Zero 2（キーボードモード） |

**注意**: `8BitDo Micro gamepad`（11720/36897）とは **PID が違う**。Micro 側の設定は [8bitdo-micro.md](8bitdo-micro.md)。

## 現在のステータス

ルールグループ **`8BitDo Zero 2 - 全ボタン設定`** は **`"enabled": false`** が付いているため、
**有効化するまでマッピングは動かない**。実機で使うときは Karabiner-Elements の UI から有効化するか、
`karabiner.json` を直接編集して `enabled: true` にする。

## ボタン送出キー（キーボードモード）

Zero 2 はキーボードモードで各ボタンを英字キーとして送出する。

| 物理ボタン | 送出 `key_code` |
|-----------|-----------------|
| ↑         | `c`             |
| ↓         | `d`             |
| ←         | `e`             |
| →         | `f`             |
| Y         | `i`             |
| A         | `g`             |
| X         | `h`             |
| B         | `j`             |
| L         | `k`             |
| R         | `m`             |
| Select    | `n`             |
| Start     | `o`             |

## Complex Modifications（12件）

すべて `device_if` で `vendor_id:11720 / product_id:36888` に限定。

| # | 物理ボタン | from | to |
|---|-----------|------|------|
| 1 | ↑      | `c` | `right_arrow` |
| 2 | ↓      | `d` | `left_arrow` |
| 3 | ←      | `e` | `up_arrow` |
| 4 | →      | `f` | `down_arrow` |
| 5 | Y      | `i` | `h` + `command` + `shift` + `option`（⌘⇧⌥H） |
| 6 | A      | `g` | `print_screen`（ルール description は「F13」だが `to` は print_screen） |
| 7 | X      | `h` | `end` |
| 8 | B      | `j` | `home` |
| 9 | L      | `k` | `delete_or_backspace`（Backspace） |
| 10 | R      | `m` | `return_or_enter` + `shift`（Shift+Enter） |
| 11 | Select | `n` | `consumer_key_code: dictation`（音声入力） |
| 12 | Start  | `o` | `escape` |

## 備考

- 方向キー 4 つは**意図的に 90° 回転マッピング**されている（↑→右、↓→左、←→上、→→下）。縦持ち用途と思われる。
- ルール 6（A ボタン）は description と実際の `to` が食い違う。JSON 側（`print_screen`）が正。
