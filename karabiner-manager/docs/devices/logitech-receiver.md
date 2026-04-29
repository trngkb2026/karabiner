# Logitech USB Receiver（vendor 1133 / product 50503）

Logitech の USB ドングル（キーボード・マウス共通の VID/PID）。
同じ識別子で **キーボード側とポインティング側の両方**が接続される（合成デバイスではなく、別デバイスとして 2 つ見える）。

## デバイス識別

| 項目         | 値            |
| ------------ | ------------- |
| vendor_id    | 1133          |
| product_id   | 50503         |
| 製品例       | Logitech USB Receiver（キーボード・ポインティング両方で同一 VID/PID） |

## Complex Modifications

ルール名: **Block do_not_disturb from Logitech USB Receiver (all event types)**

USB レシーバが誤って「集中モード切替（do_not_disturb）」を送出するのをブロックする。

| # | from | to |
|---|------|------|
| 1 | `consumer_key_code: do_not_disturb` | `[]`（破棄） |
| 2 | `key_code: do_not_disturb`          | `[]`（破棄） |

- どちらも `device_if` で `vendor=1133 product=50503` に限定

## Simple Modifications / devices[] 設定

`profiles[].devices[]` 側のキーボード・ポインティングエントリに個別設定あり（詳しくは `karabiner.json` の該当エントリを参照）。

一部のグローバル複合ルール（`⌘ 短押しで IME` 系）の `device_unless` 対象として、合成の結果ルールが発火しないよう除外されている箇所あり。

## 備考

- Logitech Unifying / Bolt レシーバは**ファームによっては VID/PID が変わる**ことがある。EventViewer で要確認。
- キーボード・ポインティングが**別 `device_id` で同一 VID/PID**の合成。`device_if` は両方に当たるので注意。
