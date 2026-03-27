# X8 BLE Keyboard キーマップ一覧

Karabiner-Elements の設定（`karabiner.json`）における **X8 BLE Keyboard** 向けマッピングです。

## デバイス識別

| 項目 | 値 |
|------|-----|
| 製品例 | X8 BLE Keyboard |
| vendor_id | 1452 |
| product_id | 599 |
| 備考 | 複合ルールはすべて `device_if` でこの端末に限定 |

## 複合ルール

ルールグループ名: **X8 BLE Keyboard - カスタム設定**

| # | 入力 | 出力・動作 |
|---|------|------------|
| 1 | Caps Lock | 英数 ⇔ かなのトグル（内部変数 `x8_ble_caps_ime`） |
| 2 | ポインティング button1（左クリック相当） | 音声入力（dictation） |
| 3 | ポインティング button3（中クリック相当のことが多い） | ⌘W |
| 4 | `application` キー | アプリケーションのウィンドウ（osascript: Control + ↓、key code 125） |
| 5 | Consumer `ac_home` | デスクトップ表示（osascript: F11 相当、key code 103） |
| 6 | Consumer `mute` | Mission Control（`mission_control`） |

## デバイス別 Simple Modifications

| 設定 |
|------|
| `simple_modifications`: **空配列 `[]`**（X8 用の Simple Mod はファイル上は未設定） |

## システムショートカットとの関係

以下は macOS の **キーボードショートカット** の既定に依存します。変更している場合は `karabiner.json` 内の `shell_command` や `key_code` を合わせて調整してください。

- アプリケーションのウィンドウ: Mission Control の「アプリケーションのウィンドウを表示」（既定は Control + ↓）
- デスクトップ表示: 「デスクトップを表示」（既定は F11）

## 注意

- button1 を音声入力にしているため、**タッチパッドの左クリックが音声入力に置き換わります**。
- 複合ルールの変更後は Karabiner-Elements が `karabiner.json` を読み直すまで反映されない場合があります。
