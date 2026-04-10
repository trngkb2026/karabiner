# デバイス一覧（Karabiner まわり）

`karabiner.json` に出てくる識別子と、EventViewer などで取得した**接続デバイス例**を分けて記載する。VID/PID は接続モード・ファーム・OS で変わることがある。

## 1. `karabiner.json` で明示的に扱っている識別子

| 用途 | vendor_id | product_id | ルールまたは `devices[]` の備考 |
|------|-----------|------------|--------------------------------|
| Magic Keyboard（Apple BT） | 76 | 671 | `Magic Keyboard - カスタム設定`、Space ルールでは `device_unless` |
| X8 BLE / K02 等（Apple ベンダー表示の HID） | 1452 | 599 | `X8 BLE Keyboard`、Fn+ポインティング→スクロール、キーボード＋ポインティングの合成デバイスあり |
| Logitech USB Receiver（キーボード） | 1133 | 50503 | DND ブロック、一部グローバル複合ルールの `device_unless` 対象 |
| Logitech USB Receiver（ポインティング） | 1133 | 50503 | `ignore_vendor_events` 等は `devices[]` 参照 |
| 8BitDo Zero 2（キーボードモード想定） | 11720 | 36888 | `8BitDo Zero 2 - 全ボタン設定`（**現状 `enabled: false`**） |
| 8BitDo（別 PID） | 11720 | 36897 | Keychron ルールの除外リストに含まれる。`devices[]` で `simple_modifications`（例: f20→dictation） |
| Keychron（メインキーボード・BT 前提、`devices[]`） | 13364 | （`product_id` なし・`is_keyboard: true`） | `grave_accent_and_tilde` → `volume_increment` など。旧 USB PID **53286 / 53296** の専用行は削除済み |
| TENBT03 等テンキー（`devices[]` のみ） | 9427 | 12427 | キーボード＋ポインティング合成行想定。`grave_accent_and_tilde` → `volume_increment`（**Keychron 複合ルールの `device_if` には含めない**） |
| 内蔵キーボード | — | — | `is_built_in_keyboard: true`（Keychron 複合ルールは `device_if` のため内蔵は対象外） |

### Keychron Link-KM ルールの対象

`Keychron Link-KM - カスタム設定` は **`device_if`** で **`vendor_id: 13364` のみ**（`product_id` なし、`is_keyboard` なし）に一致するイベントに適用される。

**9427 / 12427**（TENBT03 等）は **複合ルールからは外している**（テンキー用 `devices[]` の Simple Mod のみ残す）。

**13364 以外の VID** ではマッチしない。Event Viewer で実機を確認し、必要なら `device_if.identifiers` に **1 行追加**する。

メインキーボードは **Bluetooth 接続に一本化**する前提で、USB / 2.4GHz ドングル用の `devices[]` 行（例: 旧 **53286 / 53296**）は削除済み。

## 2. 接続デバイス例（EventViewer エクスポート）

以下はある時点の接続一覧の JSON だが、**製品名・PID は環境依存**。差分が出たら EventViewer で取り直す。

- **8BitDo Micro gamepad**: 11720 / 36897（Bluetooth）— 上記 `36897` と一致しうる
- **Keychron B3 Pro**: 13364 / 1844（BLE）— `devices[]` は **`is_keyboard` + `vendor_id` 13364**（PID なし）でカバー
- **Magic Keyboard / Magic Trackpad / Logitech USB Receiver**: 上表と対応
- **Karabiner Virtual HID**、**DJI MIC MINI**、**Pebble V3** など: 本リポジトリの complex ルールでは個別に名前付けしていない

生データ:

```json
[
    {
        "device_id": 4295094444,
        "device_identifiers": {
            "is_keyboard": true,
            "product_id": 36897,
            "vendor_id": 11720
        },
        "location_id": 1492772147,
        "product": "8BitDo Micro gamepad",
        "serial_number": "E4:17:D8:F9:E5:33",
        "transport": "Bluetooth"
    },
    {
        "device_id": 4295035558,
        "device_identifiers": {
            "is_consumer": true,
            "product_id": 16401,
            "vendor_id": 11427
        },
        "location_id": 51511296,
        "manufacturer": "DJI Technology Co., Ltd.",
        "product": "DJI MIC MINI",
        "serial_number": "XSP12345678B",
        "transport": "USB"
    },
    {
        "device_id": 4294970213,
        "device_identifiers": { "is_consumer": true },
        "is_apple": true,
        "manufacturer": "Apple",
        "product": "Headset",
        "transport": "Audio"
    },
    {
        "device_id": 4295094478,
        "device_identifiers": {
            "is_keyboard": true,
            "is_virtual_device": true,
            "product_id": 593,
            "vendor_id": 1452
        },
        "manufacturer": "pqrs.org",
        "product": "Karabiner DriverKit VirtualHIDKeyboard 1.8.0",
        "serial_number": "pqrs.org:Karabiner-DriverKit-VirtualHIDKeyboard"
    },
    {
        "device_id": 4295094481,
        "device_identifiers": {
            "is_pointing_device": true,
            "is_virtual_device": true,
            "product_id": 10202,
            "vendor_id": 5824
        },
        "manufacturer": "pqrs.org",
        "product": "Karabiner DriverKit VirtualHIDPointing 1.8.0",
        "serial_number": "pqrs.org:Karabiner-DriverKit-VirtualHIDPointing"
    },
    {
        "device_id": 4295091914,
        "device_identifiers": {
            "is_keyboard": true,
            "is_pointing_device": true,
            "product_id": 1844,
            "vendor_id": 13364
        },
        "location_id": 2684732309,
        "manufacturer": "Keychron ",
        "product": "Keychron B3 Pro",
        "serial_number": "SN1234567890",
        "transport": "Bluetooth Low Energy"
    },
    {
        "device_id": 4295037269,
        "device_identifiers": {
            "is_pointing_device": true,
            "product_id": 613,
            "vendor_id": 76
        },
        "is_apple": true,
        "location_id": 1992172764,
        "manufacturer": "Apple Inc.",
        "product": "Magic Trackpad",
        "serial_number": "3C:A6:F6:BE:24:DC",
        "transport": "Bluetooth"
    },
    {
        "device_id": 4295041738,
        "device_identifiers": {
            "is_consumer": true,
            "product_id": 12914,
            "vendor_id": 1054
        },
        "location_id": 34603008,
        "manufacturer": "ACTIONS",
        "product": "Pebble V3",
        "serial_number": "㉕捤稰眷㕳愳㤷湲",
        "transport": "USB"
    },
    {
        "device_id": 4294972177,
        "device_identifiers": {
            "is_keyboard": true,
            "product_id": 50503,
            "vendor_id": 1133
        },
        "location_id": 51445760,
        "manufacturer": "Logitech",
        "product": "USB Receiver",
        "transport": "USB"
    },
    {
        "device_id": 4294972193,
        "device_identifiers": {
            "is_pointing_device": true,
            "product_id": 50503,
            "vendor_id": 1133
        },
        "location_id": 51445760,
        "manufacturer": "Logitech",
        "product": "USB Receiver",
        "transport": "USB"
    },
    {
        "device_id": 4294972840,
        "device_identifiers": {
            "is_keyboard": true,
            "product_id": 671,
            "vendor_id": 76
        },
        "is_apple": true,
        "location_id": 945735173,
        "manufacturer": "Apple Inc.",
        "product": "太郎のMagic Keyboard",
        "serial_number": "AC:97:38:5E:C6:05",
        "transport": "Bluetooth"
    }
]
```
