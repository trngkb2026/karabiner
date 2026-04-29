# Karabiner キーマップ ドキュメント

> **最終更新: 2026-04-21** — `references/` + `mappings_by_device/` を `docs/` に統合。

Karabiner-Elements の設定（`~/.config/karabiner/karabiner.json`）に関する手書きドキュメント一式。
生成ファイルではなく、**人間が書いて `karabiner.json` と整合させる**メモ。
機械生成の最新棚卸しは [`_generated/_index.md`](_generated/_index.md) を参照。

## 構成

```
docs/
├── README.md              # 本ファイル（インデックス + 接続デバイス一覧）
├── global-rules.md        # デバイス非依存の複合ルール（スペース/⌘→IME/etc）
├── variables.md           # Karabiner 変数一覧（from/to で使っているもの）
├── _generated/            # `export_mappings_md.py` による機械生成の棚卸し
├── devices/               # デバイスごとのキーマップ
│   ├── tenbt03.md              # MCO TENBT03（9427:12427）
│   ├── x8-ble-keyboard.md      # Ewin X8・K02 等（1452:599）
│   ├── magic-keyboard.md       # Apple Magic Keyboard（76:671）
│   ├── keychron-link-km.md     # Keychron B3 Pro 他（13364:*）
│   ├── logitech-receiver.md    # Logitech USB Receiver（1133:50503）
│   ├── elecom-mouse.md         # ELECOM マウス（1390:342）
│   ├── 8bitdo-zero2.md         # 8BitDo Zero 2（11720:36888）
│   └── 8bitdo-micro.md         # 8BitDo Micro（11720:36897）
├── assets/                # 実機写真
│   ├── tenbt03.jpg
│   └── ewin-x8.png
└── archive/               # 過去の調査レポート
    └── tenbt03-lshift-f13-report.md
```

`karabiner.json` の生データと、その下位ドキュメント（デバイス別詳細）の**間**にあたる中層ドキュメントがこの `README.md` + `global-rules.md` + `variables.md`。

## デバイス一覧（`karabiner.json` で扱っている識別子）

| 用途                             | vendor_id | product_id | 詳細                                         |
| -------------------------------- | --------- | ---------- | -------------------------------------------- |
| Magic Keyboard（Apple BT）       | 76        | 671        | [magic-keyboard.md](devices/magic-keyboard.md) |
| X8 BLE / K02（Apple VID の HID） | 1452      | 599        | [x8-ble-keyboard.md](devices/x8-ble-keyboard.md) |
| Logitech USB Receiver            | 1133      | 50503      | [logitech-receiver.md](devices/logitech-receiver.md) |
| ELECOM マウス                    | 1390      | 342        | [elecom-mouse.md](devices/elecom-mouse.md) |
| 8BitDo Zero 2（KB モード）       | 11720     | 36888      | [8bitdo-zero2.md](devices/8bitdo-zero2.md) |
| 8BitDo Micro 他                  | 11720     | 36897      | [8bitdo-micro.md](devices/8bitdo-micro.md) |
| Keychron（`vendor_id` のみ）     | 13364     | —          | [keychron-link-km.md](devices/keychron-link-km.md) |
| MCO TENBT03 テンキー             | 9427      | 12427      | [tenbt03.md](devices/tenbt03.md) |
| 内蔵キーボード                   | —         | —          | `is_built_in_keyboard: true` |

**メインキーボードは Bluetooth 接続に一本化**する前提。USB / 2.4GHz ドングル用の `devices[]` 行（旧 Keychron 53286 / 53296 等）は削除済み。

## デバイス識別のコツ

- VID/PID は**接続モード・ファーム・OS で変わる**ことがある。差分が出たら Karabiner-EventViewer で取り直す。
- `vendor_id` のみ指定（`product_id` なし）は「その VID のあらゆる機器」に一致する点に注意。
- 合成デバイス（キーボード + ポインティング）は `is_keyboard` / `is_pointing_device` を両方持つ。

## 接続デバイス例（Karabiner-EventViewer エクスポート）

**参考**。製品名・PID は環境依存なので、以下は「過去の一スナップショット」にすぎない。
実機を確認する場合は Karabiner-EventViewer の Devices タブを再取得する。

- **8BitDo Micro gamepad**: 11720 / 36897（Bluetooth）
- **Keychron B3 Pro**: 13364 / 1844（BLE）
- **Magic Keyboard / Magic Trackpad / Logitech USB Receiver / TENBT03**: 上表の通り
- **Karabiner Virtual HID**、**DJI MIC MINI**、**Pebble V3** など: 複合ルールでは個別に扱っていない

<details>
<summary>生 JSON（展開）</summary>

```json
[
    {
        "device_id": 4295094444,
        "device_identifiers": { "is_keyboard": true, "product_id": 36897, "vendor_id": 11720 },
        "location_id": 1492772147,
        "product": "8BitDo Micro gamepad",
        "serial_number": "E4:17:D8:F9:E5:33",
        "transport": "Bluetooth"
    },
    {
        "device_id": 4295091914,
        "device_identifiers": { "is_keyboard": true, "is_pointing_device": true, "product_id": 1844, "vendor_id": 13364 },
        "location_id": 2684732309,
        "manufacturer": "Keychron ",
        "product": "Keychron B3 Pro",
        "serial_number": "SN1234567890",
        "transport": "Bluetooth Low Energy"
    },
    {
        "device_id": 4294972840,
        "device_identifiers": { "is_keyboard": true, "product_id": 671, "vendor_id": 76 },
        "is_apple": true,
        "location_id": 945735173,
        "manufacturer": "Apple Inc.",
        "product": "太郎のMagic Keyboard",
        "transport": "Bluetooth"
    },
    {
        "device_id": 4294972177,
        "device_identifiers": { "is_keyboard": true, "product_id": 50503, "vendor_id": 1133 },
        "manufacturer": "Logitech",
        "product": "USB Receiver",
        "transport": "USB"
    }
]
```

</details>

## グローバルルール（複数デバイスに影響）

詳細は [global-rules.md](global-rules.md)。

| ルール概要                  | メモ                                                                                           |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| Space 単発 / 長押し・併用   | Magic Keyboard（76:671）**以外**で ⌘ 系とスペースの切り替え                                  |
| 左⌘ / 右⌘ 単独短押し        | 英数 / かな。**X8 BLE（1452:599）・MCO TENBT03（9427:12427）以外**（2026-04-21 に TENBT03 を除外追加） |
| ⌃Space                     | `ctrl_space_ime_toggle` で英数⇔かな                                                           |
| ⌘W                         | スペース                                                                                       |

## 変数

[variables.md](variables.md) を参照。

## ドキュメント原則

- **実機の動作が一次情報**。Web 検索で得た仕様と食い違う場合は実機（写真・EventViewer）を正とする。
- `karabiner.json` の `to` / `from` と、本ドキュメントの `description` が食い違う場合は **JSON を正**とし、ドキュメント側に備考で注記する。
- 実機写真は `assets/` に入れる。デバイスドキュメントからは相対パスで `../assets/tenbt03.jpg` のように参照する。
- 旧仕様・廃止した実験は `archive/` に置く（削除はしない）。
