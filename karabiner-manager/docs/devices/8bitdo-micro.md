# 8BitDo Micro（vendor 11720 / product 36897）

**8BitDo Micro gamepad**（Bluetooth 接続時の識別）。
同じ 8BitDo でも **Zero 2（11720:36888）**とは PID が違うため、別ルール扱い。

## デバイス識別

| 項目         | 値         |
| ------------ | ---------- |
| vendor_id    | 11720      |
| product_id   | 36897      |
| 製品例       | 8BitDo Micro gamepad |
| 識別子（`devices[]`） | `is_keyboard: true` / `product_id: 36897` / `vendor_id: 11720` |

## Simple Modifications（1件）

`profiles[].devices[]` 内の当該デバイスエントリに登録されている **device_simple_modification**。

| from | to |
|------|------|
| `f20` | `consumer_key_code: dictation`（音声入力） |

## Complex Modifications

**なし**（Zero 2 と違って独自の Complex ルールはない）。

## グローバルルールとの関係

**Keychron Link-KM 系ルール** の `device_unless` 除外リストに `36897` が含まれている
（Keychron ルールの対象から外れている）。同列の扱いで Zero 2（36888）も除外されている。

## 備考

- ゲームパッドだが macOS は **キーボードとして認識**している（`is_keyboard: true`）。
- 設定は Zero 2 と違って最小限。必要なら Complex Modifications を別途追加する形になる。
