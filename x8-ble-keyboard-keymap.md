# X8 BLE Keyboard キーマップ一覧

Karabiner-Elements の設定（`karabiner.json`）における **X8 BLE Keyboard** 向けマッピングです。

## デバイス識別


| 項目         | 値                              |
| ---------- | ------------------------------ |
| 製品例        | X8 BLE Keyboard                |
| vendor_id  | 1452                           |
| product_id | 599                            |
| 備考         | 下記「X8 BLE Keyboard - カスタム設定」内のルールは `device_if` で X8 のみ。スペースの ⌘ デュアルロールは **全キーボード**（別ルール） |


## 複合ルール

ルールグループ名: **X8 BLE Keyboard - カスタム設定**


| #   | 入力                                | 出力・動作                                               |
| --- | --------------------------------- | --------------------------------------------------- |
| 1   | F1                                | F13                                                 |
| 2   | F2                                | Shift + F13                                         |
| 3   | F3                                | Control + K                                         |
| 4   | F4                                | Shift+T,E,N,T,E,N + テンキー 8,2,2,3 + Enter（1キーずつ）      |
| 5   | Caps Lock                         | 英数 ⇔ かなのトグル（内部変数 `x8_ble_caps_ime`）                 |
| 6   | ポインティング button1（左クリック相当）          | 音声入力（dictation）                                     |
| 7   | ポインティング button2（右クリック相当）          | Enter（`return_or_enter`）                             |
| 8   | ポインティング button3（中クリック相当のことが多い）    | ⌘+左クリック（`button1` + `left_command`）                |
| 9   | `application` キー                  | アプリケーションのウィンドウ（osascript: Control + ↓、key code 125） |
| 10  | Consumer `ac_home`                | デスクトップ表示（osascript: F11 相当、key code 103）            |
| 11  | Consumer `mute`                   | Mission Control（`mission_control`）                  |
| 12  | Consumer `volume_decrement`（音量下げ） | F13                                                 |
| 13  | Consumer `volume_increment`（音量上げ） | Shift + F13                                         |
| 14  | 左 Command                         | F13                                                 |
| 15  | 右 Command                         | F13                                                 |

### Space と Command（別ルール・全キーボード）

ルール名: **Space: 単発でスペース / 長押し・併用で Command（全キーボード）**

`device_if` なし。**接続しているすべてのキーボード**のスペースキーが次のように動きます。

| 操作 | 動作 |
|------|------|
| 単発（すぐ離す） | スペース入力 |
| 長押し（約 250ms 以上） | 左 Command として保持 |
| 押したまま他キー | ⌘+そのキー（`lazy` 左 Command） |

X8 は物理 ⌘ が F13 のため、**⌘ 相当はこのスペース挙動が特に重要**。Magic Keyboard でも同じスペース挙動が有効（物理 ⌘ もそのまま使える）。

### スクロール量（別ルール）

ルール名: **X8 BLE: Fn+トラックパッド移動→スクロール（speed_multiplier 2.0）**

| 条件 | 動作 |
|------|------|
| **Fn を押したまま** X8 のトラックパッドで指を動かす | その移動が **スクロール** として送られ、`speed_multiplier` **2.0** で量が増える（`mouse_motion_to_scroll`） |

**補足:** Karabiner 標準では **物理ホイールの「1ノッチあたりのデルタ」を直接倍にする**ことはできません。ホイールだけ速くしたい場合は **システム設定 → マウス** のスクロール速度や、**Mos** などのユーティリティを検討してください。


## デバイス別 Simple Modifications


| 設定                                                                |
| ----------------------------------------------------------------- |
| `simple_modifications`: **空配列 `[]`**（X8 用の Simple Mod はファイル上は未設定） |


## システムショートカットとの関係

以下は macOS の **キーボードショートカット** の既定に依存します。変更している場合は `karabiner.json` 内の `shell_command` や `key_code` を合わせて調整してください。

- アプリケーションのウィンドウ: Mission Control の「アプリケーションのウィンドウを表示」（既定は Control + ↓）
- デスクトップ表示: 「デスクトップを表示」（既定は F11）

## 注意

- button1 を音声入力にしているため、**タッチパッドの左クリックが音声入力に置き換わります**。
- button2 を Enter にしているため、**右クリック相当のボタンは使えません**。
- button3 は **⌘+左クリック**（新規タブで開く等）。Karabiner やアプリによっては効かないことがあります。
- X8 の **物理 ⌘ は F13** です。**⌘ 修飾**はスペースの長押し／スペース＋他キー、**Magic Keyboard の ⌘**、いずれでも可（スペース ⌘ デュアルロールは **全キーボード**で有効）。
- 複合ルールの変更後は Karabiner-Elements が `karabiner.json` を読み直すまで反映されない場合があります。

