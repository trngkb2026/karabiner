# Karabiner 変数・状態

## `karabiner.json` の complex_modifications で使う名前付き変数

| 変数名 | 値の意味 | 使っているルール |
|--------|-----------|------------------|
| `ctrl_space_ime_toggle` | `1` のとき次の ⌃Space で英数、`0` のときかな（トグル） | `⌃Space: 英数⇔かなトグル` |
| `x8_ble_caps_ime` | `1` のとき次の Caps で英数、`0` のときかな（トグル） | `X8 BLE Keyboard` の Caps 系 |

初期値はルールの `variable_unless` / `variable_if` の組み合わせに依存（未設定は 0 扱い）。

## EventViewer の Variables タブ（参考スナップショット）

以下はある時点の **システム／Karabiner が公開している変数** の例。上のカスタム変数は、該当キーを押した後に EventViewer で確認できる。

```json
{
    "frontmost_application": {
        "bundle_identifier": "org.pqrs.Karabiner-Elements.Settings",
        "bundle_path": "/Applications/Karabiner-Elements.app",
        "file_path": "/Applications/Karabiner-Elements.app/Contents/MacOS/Karabiner-Elements",
        "pid": 84969
    },
    "input_source": {
        "input_source_id": "com.apple.keylayout.ABC",
        "language": "en"
    },
    "karabiner_machine_identifier": "krbn-c5351ba2-632d-43f6-9d1e-32a13467dde5",
    "variables": {
        "system.now.milliseconds": 1775008611615,
        "system.scroll_direction_is_natural": false,
        "system.temporarily_ignore_all_devices": false,
        "system.use_fkeys_as_standard_function_keys": true
    },
    "virtual_hid_devices_state": {
        "virtual_hid_keyboard_ready": true,
        "virtual_hid_pointing_ready": true
    }
}
```
