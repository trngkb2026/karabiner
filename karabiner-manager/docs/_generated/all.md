# Karabiner マッピング（全件）デバイス別ファイルの連結です。目次は [_index.md](_index.md)。---## global.md# Karabiner マッピング（デバイス非依存）

次を含みます。

- `device_if` 条件のない複合ルール
- プロファイル直下の **fn_function_keys**（F1–F12）

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. 左 Command 単独短押し→英数

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** ⌘ 短押しで IME（左→英数 / 右→かな）（X8 BLE / TENBT03 以外）
- **マニピュレータ:** 左 Command 単独短押し→英数

**from:**

```json
{
  "key_code": "left_command",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "left_command",
    "lazy": true
  }
]
```

**extra（parameters / to_if_alone 等）:**

```json
{
  "parameters": {
    "basic.to_if_alone_timeout_milliseconds": 300
  },
  "to_if_alone": [
    {
      "key_code": "japanese_eisuu"
    }
  ]
}
```


### 2. 右 Command 単独短押し→かな

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** ⌘ 短押しで IME（左→英数 / 右→かな）（X8 BLE / TENBT03 以外）
- **マニピュレータ:** 右 Command 単独短押し→かな

**from:**

```json
{
  "key_code": "right_command",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "right_command",
    "lazy": true
  }
]
```

**extra（parameters / to_if_alone 等）:**

```json
{
  "parameters": {
    "basic.to_if_alone_timeout_milliseconds": 300
  },
  "to_if_alone": [
    {
      "key_code": "japanese_kana"
    }
  ]
}
```


### 3. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f1"
}
```

**to:**

```json
[
  {
    "key_code": "f1"
  }
]
```


### 4. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f2"
}
```

**to:**

```json
[
  {
    "key_code": "f2"
  }
]
```


### 5. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f3"
}
```

**to:**

```json
[
  {
    "key_code": "f3"
  }
]
```


### 6. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f4"
}
```

**to:**

```json
[
  {
    "key_code": "f4"
  }
]
```


### 7. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f5"
}
```

**to:**

```json
[
  {
    "key_code": "f5"
  }
]
```


### 8. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f6"
}
```

**to:**

```json
[
  {
    "key_code": "f6"
  }
]
```


### 9. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f7"
}
```

**to:**

```json
[
  {
    "key_code": "f7"
  }
]
```


### 10. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f8"
}
```

**to:**

```json
[
  {
    "key_code": "f8"
  }
]
```


### 11. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f9"
}
```

**to:**

```json
[
  {
    "key_code": "f9"
  }
]
```


### 12. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f10"
}
```

**to:**

```json
[
  {
    "key_code": "f10"
  }
]
```


### 13. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f11"
}
```

**to:**

```json
[
  {
    "key_code": "f11"
  }
]
```


### 14. profile_fn_function_key

- **種別:** `profile_fn_function_key`
- **プロファイル:** `240106`

**from:**

```json
{
  "key_code": "f12"
}
```

**to:**

```json
[
  {
    "key_code": "f12"
  }
]
```
---## v76_p671.md

# Karabiner マッピング（vendor 76 / product 671）

- **vendor_id:** `76`
- **product_id:** `671`

**identifiers（devices ブロック）:**

```json
{
  "is_keyboard": true,
  "product_id": 671,
  "vendor_id": 76
}
```

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. F2 → Shift+F13

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Magic Keyboard - カスタム設定
- **マニピュレータ:** F2 → Shift+F13
- **デバイス条件:** vendor=76 product=671

**from:**

```json
{
  "key_code": "f2"
}
```

**to:**

```json
[
  {
    "key_code": "f13",
    "modifiers": [
      "shift"
    ]
  }
]
```


### 2. F3 → Control+K

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Magic Keyboard - カスタム設定
- **マニピュレータ:** F3 → Control+K
- **デバイス条件:** vendor=76 product=671

**from:**

```json
{
  "key_code": "f3"
}
```

**to:**

```json
[
  {
    "key_code": "k",
    "modifiers": [
      "control"
    ]
  }
]
```


### 3. F4 → Tenten8223+Enter（1文字ずつ）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Magic Keyboard - カスタム設定
- **マニピュレータ:** F4 → Tenten8223+Enter（1文字ずつ）
- **デバイス条件:** vendor=76 product=671

**from:**

```json
{
  "key_code": "f4"
}
```

**to:**

```json
[
  {
    "shell_command": "/usr/bin/osascript -e 'tell application \"System Events\"' -e 'set s to \"Tenten8223\"' -e 'repeat with i from 1 to length of s' -e 'keystroke character i of s' -e 'end repeat' -e 'keystroke return' -e 'end tell'"
  }
]
```


### 4. F7 → Option+H

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Magic Keyboard - カスタム設定
- **マニピュレータ:** F7 → Option+H
- **デバイス条件:** vendor=76 product=671

**from:**

```json
{
  "key_code": "f7"
}
```

**to:**

```json
[
  {
    "key_code": "h",
    "modifiers": [
      "left_option"
    ]
  }
]
```


### 5. F19 → スリープ

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Magic Keyboard - カスタム設定
- **マニピュレータ:** F19 → スリープ
- **デバイス条件:** vendor=76 product=671

**from:**

```json
{
  "key_code": "f19"
}
```

**to:**

```json
[
  {
    "shell_command": "pmset sleepnow"
  }
]
```


### 6. 右Control → Space×4+Enter

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Magic Keyboard - カスタム設定
- **マニピュレータ:** 右Control → Space×4+Enter
- **デバイス条件:** vendor=76 product=671

**from:**

```json
{
  "key_code": "right_control",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 7. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 671,
  "vendor_id": 76
}

**from:**

```json
{
  "key_code": "f1"
}
```

**to:**

```json
[
  {
    "key_code": "print_screen"
  }
]
```


### 8. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 671,
  "vendor_id": 76
}

**from:**

```json
{
  "key_code": "caps_lock"
}
```

**to:**

```json
[
  {
    "key_code": "left_option"
  }
]
```


### 9. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 671,
  "vendor_id": 76
}

**from:**

```json
{
  "key_code": "left_option"
}
```

**to:**

```json
[
  {
    "apple_vendor_keyboard_key_code": "spotlight"
  }
]
```


### 10. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 671,
  "vendor_id": 76
}

**from:**

```json
{
  "key_code": "right_option"
}
```

**to:**

```json
[
  {
    "consumer_key_code": "dictation"
  }
]
```

---

## v1133_p50503.md

# Karabiner マッピング（vendor 1133 / product 50503）

- **vendor_id:** `1133`
- **product_id:** `50503`

**デバイス条件:** vendor=1133 product=50503

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. Block do_not_disturb from Logitech USB Receiver (all event types)

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Block do_not_disturb from Logitech USB Receiver (all event types)
- **デバイス条件:** vendor=1133 product=50503

**from:**

```json
{
  "consumer_key_code": "do_not_disturb"
}
```

**to:**

```json
[]
```


### 2. Block do_not_disturb from Logitech USB Receiver (all event types)

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Block do_not_disturb from Logitech USB Receiver (all event types)
- **デバイス条件:** vendor=1133 product=50503

**from:**

```json
{
  "key_code": "do_not_disturb"
}
```

**to:**

```json
[]
```

---

## v1390_p342.md

# Karabiner マッピング（vendor 1390 / product 342）

- **vendor_id:** `1390`
- **product_id:** `342`

**identifiers（devices ブロック）:**

```json
{
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}
```

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "pointing_button": "button1"
}
```

**to:**

```json
[
  {
    "key_code": "1",
    "modifiers": [
      "option"
    ]
  }
]
```


### 2. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "pointing_button": "button2"
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "shift",
      "option"
    ]
  }
]
```


### 3. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "pointing_button": "button3"
}
```

**to:**

```json
[
  {
    "key_code": "return_or_enter"
  }
]
```


### 4. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "pointing_button": "button4"
}
```

**to:**

```json
[
  {
    "key_code": "c",
    "modifiers": [
      "command"
    ]
  }
]
```


### 5. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "pointing_button": "button5"
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "command"
    ]
  }
]
```


### 6. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "consumer_key_code": "play_or_pause"
}
```

**to:**

```json
[
  {
    "key_code": "fn"
  }
]
```


### 7. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "consumer_key_code": "scan_previous_track"
}
```

**to:**

```json
[
  {
    "key_code": "tab",
    "modifiers": [
      "shift",
      "control"
    ]
  }
]
```


### 8. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "consumer_key_code": "scan_next_track"
}
```

**to:**

```json
[
  {
    "key_code": "tab",
    "modifiers": [
      "control"
    ]
  }
]
```


### 9. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "consumer_key_code": "volume_increment"
}
```

**to:**

```json
[
  {
    "key_code": "return_or_enter"
  }
]
```


### 10. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_pointing_device": true,
  "product_id": 342,
  "vendor_id": 1390
}

**from:**

```json
{
  "consumer_key_code": "volume_decrement"
}
```

**to:**

```json
[
  {
    "key_code": "delete_or_backspace",
    "modifiers": [
      "command"
    ]
  }
]
```

---

## v1452_p599.md

# Karabiner マッピング（vendor 1452 / product 599）

- **vendor_id:** `1452`
- **product_id:** `599`

**identifiers（devices ブロック）:**

```json
{
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 599,
  "vendor_id": 1452
}
```

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. X8 BLE: Fn+トラックパッド移動→スクロール（speed_multiplier 2.0）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE: Fn+トラックパッド移動→スクロール（speed_multiplier 2.0）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "modifiers": {
    "mandatory": [
      "fn"
    ],
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
null
```


### 2. Caps → 英数（トグル）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** Caps → 英数（トグル）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "caps_lock",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "set_variable": {
      "name": "x8_ble_caps_ime",
      "value": 0
    }
  },
  {
    "key_code": "japanese_eisuu"
  }
]
```


### 3. Caps → かな（トグル）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** Caps → かな（トグル）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "caps_lock",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "set_variable": {
      "name": "x8_ble_caps_ime",
      "value": 1
    }
  },
  {
    "key_code": "japanese_kana"
  }
]
```


### 4. ボタン1（ポインティング）→ 音声入力

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** ボタン1（ポインティング）→ 音声入力
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "modifiers": {
    "optional": [
      "any"
    ]
  },
  "pointing_button": "button1"
}
```

**to:**

```json
[
  {
    "consumer_key_code": "dictation"
  }
]
```


### 5. ボタン2（ポインティング）→ Enter

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** ボタン2（ポインティング）→ Enter
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "modifiers": {
    "optional": [
      "any"
    ]
  },
  "pointing_button": "button2"
}
```

**to:**

```json
[
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 6. ボタン3（ポインティング）→ ⌘+左クリック

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** ボタン3（ポインティング）→ ⌘+左クリック
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "modifiers": {
    "optional": [
      "any"
    ]
  },
  "pointing_button": "button3"
}
```

**to:**

```json
[
  {
    "key_code": "left_command"
  }
]
```


### 7. application キー → アプリケーションのウィンドウ（Control+↓ / osascript）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** application キー → アプリケーションのウィンドウ（Control+↓ / osascript）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "application",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "s",
    "modifiers": [
      "control"
    ]
  }
]
```


### 8. ac_home（Consumer）→ デスクトップ表示（F11 / osascript）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** ac_home（Consumer）→ デスクトップ表示（F11 / osascript）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "consumer_key_code": "ac_home",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "control"
    ]
  }
]
```


### 9. ミュート（Consumer）→ Mission Control

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** ミュート（Consumer）→ Mission Control
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "consumer_key_code": "mute",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "mission_control"
  }
]
```


### 10. 音量下げ（Consumer）→ eisuu→o→k→return（順に1回ずつ）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 音量下げ（Consumer）→ eisuu→o→k→return（順に1回ずつ）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "consumer_key_code": "volume_decrement",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "c",
    "modifiers": [
      "command"
    ]
  }
]
```


### 11. 音量上げ（Consumer）→ eisuu→D→o→n→e→return（順に1回ずつ）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 音量上げ（Consumer）→ eisuu→D→o→n→e→return（順に1回ずつ）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "consumer_key_code": "volume_increment",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "command"
    ]
  }
]
```


### 12. 数字 1 → keypad_1（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 1 → keypad_1（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "1",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_1"
  }
]
```


### 13. 数字 2 → keypad_2（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 2 → keypad_2（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "2",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_2"
  }
]
```


### 14. 数字 3 → keypad_3（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 3 → keypad_3（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "3",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_3"
  }
]
```


### 15. 数字 4 → keypad_4（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 4 → keypad_4（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "4",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_4"
  }
]
```


### 16. 数字 5 → keypad_5（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 5 → keypad_5（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "5",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_5"
  }
]
```


### 17. 数字 6 → keypad_6（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 6 → keypad_6（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "6",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_6"
  }
]
```


### 18. 数字 7 → keypad_7（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 7 → keypad_7（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "7",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_7"
  }
]
```


### 19. 数字 8 → keypad_8（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 8 → keypad_8（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "8",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_8"
  }
]
```


### 20. 数字 9 → keypad_9（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 9 → keypad_9（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "9",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_9"
  }
]
```


### 21. 数字 0 → keypad_0（半角）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 数字 0 → keypad_0（半角）
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "0",
  "modifiers": {
    "optional": [
      "caps_lock"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "keypad_0"
  }
]
```


### 22. ¥ → ⌘+Backspace

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** ¥ → ⌘+Backspace
- **デバイス条件:** vendor=1452 product=599

**from:**

```json
{
  "key_code": "international_3",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "delete_or_backspace",
    "modifiers": [
      "command"
    ]
  }
]
```


### 23. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 599,
  "vendor_id": 1452
}

**from:**

```json
{
  "key_code": "f1"
}
```

**to:**

```json
[
  {
    "key_code": "print_screen"
  }
]
```


### 24. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 599,
  "vendor_id": 1452
}

**from:**

```json
{
  "key_code": "left_arrow"
}
```

**to:**

```json
[
  {
    "key_code": "delete_or_backspace"
  }
]
```


### 25. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 599,
  "vendor_id": 1452
}

**from:**

```json
{
  "key_code": "right_arrow"
}
```

**to:**

```json
[
  {
    "key_code": "return_or_enter"
  }
]
```

---

## v9427_p12427.md

# Karabiner マッピング（vendor 9427 / product 12427）

- **vendor_id:** `9427`
- **product_id:** `12427`

**identifiers（devices ブロック）:**

```json
{
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}
```

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. Custom rule

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Custom rule
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "delete_forward"
}
```

**to:**

```json
[
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 2. Custom rule

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Custom rule
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_period"
}
```

**to:**

```json
[
  {
    "key_code": "t",
    "modifiers": [
      "shift"
    ]
  },
  {
    "key_code": "e"
  },
  {
    "key_code": "n"
  },
  {
    "key_code": "t"
  },
  {
    "key_code": "e"
  },
  {
    "key_code": "n"
  },
  {
    "key_code": "8"
  },
  {
    "key_code": "2"
  },
  {
    "key_code": "2"
  },
  {
    "key_code": "3"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 3. Custom rule

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Custom rule
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "8",
  "modifiers": {
    "mandatory": [
      "shift",
      "left_shift"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f13"
  }
]
```


### 4. Custom rule

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Custom rule
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "9",
  "modifiers": {
    "mandatory": [
      "left_shift"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f13",
    "modifiers": [
      "left_shift"
    ]
  }
]
```


### 5. TENBT03 Left Shift 単独タップ→音声入力（他キー併用時はLeft Shiftのまま）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 Left Shift 単独タップ→音声入力（他キー併用時はLeft Shiftのまま）
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "left_shift",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "left_shift",
    "lazy": true
  }
]
```

**extra（parameters / to_if_alone 等）:**

```json
{
  "to_if_alone": [
    {
      "consumer_key_code": "dictation"
    }
  ]
}
```


### 6. Custom rule

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Custom rule
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "hyphen",
  "modifiers": {
    "mandatory": [
      "left_shift"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "down_arrow",
    "modifiers": [
      "control"
    ]
  }
]
```


### 7. BS10

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** BS10
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_asterisk"
}
```

**to:**

```json
[
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  },
  {
    "key_code": "delete_or_backspace"
  }
]
```


### 8. Custom rule

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Custom rule
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "left_option"
}
```

**to:**

```json
[
  {
    "key_code": "japanese_eisuu"
  },
  {
    "key_code": "o"
  },
  {
    "key_code": "k"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 9. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "left_command"
}
```

**to:**

```json
[
  {
    "apple_vendor_keyboard_key_code": "spotlight"
  }
]
```


### 10. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "keypad_num_lock"
}
```

**to:**

```json
[
  {
    "key_code": "f6"
  }
]
```


### 11. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "keypad_slash"
}
```

**to:**

```json
[
  {
    "key_code": "f11"
  }
]
```


### 12. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "keypad_plus"
}
```

**to:**

```json
[
  {
    "consumer_key_code": "volume_increment"
  }
]
```


### 13. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "keypad_hyphen"
}
```

**to:**

```json
[
  {
    "consumer_key_code": "volume_decrement"
  }
]
```


### 14. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "tab"
}
```

**to:**

```json
[
  {
    "key_code": "delete_or_backspace",
    "modifiers": [
      "command"
    ]
  }
]
```


### 15. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "down_arrow"
}
```

**to:**

```json
[
  {
    "key_code": "fn"
  }
]
```


### 16. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "up_arrow"
}
```

**to:**

```json
[
  {
    "key_code": "return_or_enter"
  }
]
```


### 17. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "left_arrow"
}
```

**to:**

```json
[
  {
    "key_code": "tab",
    "modifiers": [
      "control",
      "shift"
    ]
  }
]
```


### 18. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "is_pointing_device": true,
  "product_id": 12427,
  "vendor_id": 9427
}

**from:**

```json
{
  "key_code": "right_arrow"
}
```

**to:**

```json
[
  {
    "key_code": "tab",
    "modifiers": [
      "control"
    ]
  }
]
```

---

## v11720_p36888.md

# Karabiner マッピング（vendor 11720 / product 36888）

- **vendor_id:** `11720`
- **product_id:** `36888`

**デバイス条件:** vendor=11720 product=36888

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. ↑ → →矢印

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** ↑ → →矢印
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "c"
}
```

**to:**

```json
[
  {
    "key_code": "right_arrow"
  }
]
```


### 2. ↓ → ←矢印

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** ↓ → ←矢印
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "d"
}
```

**to:**

```json
[
  {
    "key_code": "left_arrow"
  }
]
```


### 3. ← → ↑矢印

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** ← → ↑矢印
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "e"
}
```

**to:**

```json
[
  {
    "key_code": "up_arrow"
  }
]
```


### 4. → → ↓矢印

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** → → ↓矢印
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "f"
}
```

**to:**

```json
[
  {
    "key_code": "down_arrow"
  }
]
```


### 5. Y → ⌘+Shift+Option+H

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** Y → ⌘+Shift+Option+H
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "i"
}
```

**to:**

```json
[
  {
    "key_code": "h",
    "modifiers": [
      "command",
      "shift",
      "option"
    ]
  }
]
```


### 6. A → F13

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** A → F13
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "g"
}
```

**to:**

```json
[
  {
    "key_code": "print_screen"
  }
]
```


### 7. X → End

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** X → End
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "h"
}
```

**to:**

```json
[
  {
    "key_code": "end"
  }
]
```


### 8. B → Home

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** B → Home
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "j"
}
```

**to:**

```json
[
  {
    "key_code": "home"
  }
]
```


### 9. L → Backspace

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** L → Backspace
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "k"
}
```

**to:**

```json
[
  {
    "key_code": "delete_or_backspace"
  }
]
```


### 10. R → Shift+Enter

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** R → Shift+Enter
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "m"
}
```

**to:**

```json
[
  {
    "key_code": "return_or_enter",
    "modifiers": [
      "shift"
    ]
  }
]
```


### 11. Select → 音声入力

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** Select → 音声入力
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "n"
}
```

**to:**

```json
[
  {
    "consumer_key_code": "dictation"
  }
]
```


### 12. Start → Escape

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** 8BitDo Zero 2 - 全ボタン設定
- **マニピュレータ:** Start → Escape
- **デバイス条件:** vendor=11720 product=36888

**from:**

```json
{
  "key_code": "o"
}
```

**to:**

```json
[
  {
    "key_code": "escape"
  }
]
```

---

## v11720_p36897.md

# Karabiner マッピング（vendor 11720 / product 36897）

- **vendor_id:** `11720`
- **product_id:** `36897`

**identifiers（devices ブロック）:**

```json
{
  "is_keyboard": true,
  "product_id": 36897,
  "vendor_id": 11720
}
```

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 36897,
  "vendor_id": 11720
}

**from:**

```json
{
  "key_code": "caps_lock"
}
```

**to:**

```json
[
  {
    "key_code": "japanese_eisuu"
  }
]
```


### 2. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 36897,
  "vendor_id": 11720
}

**from:**

```json
{
  "key_code": "e"
}
```

**to:**

```json
[
  {
    "consumer_key_code": "dictation"
  }
]
```


### 3. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 36897,
  "vendor_id": 11720
}

**from:**

```json
{
  "key_code": "f"
}
```

**to:**

```json
[
  {
    "key_code": "fn"
  }
]
```


### 4. device_simple_modification

- **種別:** `device_simple_modification`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 36897,
  "vendor_id": 11720
}

**from:**

```json
{
  "key_code": "i"
}
```

**to:**

```json
[
  {
    "consumer_key_code": "dictation"
  }
]
```

---

## v13364.md

# Karabiner マッピング（vendor 13364 / product —）

- **vendor_id:** `13364`
- **product_id:** `—`

**デバイス条件:** vendor=13364 product=

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. Consumer 画面輝度下げ(F1相当)→F13

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer 画面輝度下げ(F1相当)→F13
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "display_brightness_decrement",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f13"
  }
]
```


### 2. Consumer 画面輝度上げ(F2相当)→Shift+F13

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer 画面輝度上げ(F2相当)→Shift+F13
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "display_brightness_increment",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f13",
    "modifiers": [
      "shift"
    ]
  }
]
```


### 3. Apple vendor Mission Control(F3相当)→Tenten8223+Enter（osascript）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Apple vendor Mission Control(F3相当)→Tenten8223+Enter（osascript）
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "apple_vendor_keyboard_key_code": "mission_control",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "shell_command": "/usr/bin/osascript -e 'tell application \"System Events\"' -e 'set s to \"Tenten8223\"' -e 'repeat with i from 1 to length of s' -e 'keystroke character i of s' -e 'end repeat' -e 'keystroke return' -e 'end tell'"
  }
]
```


### 4. key_code mission_control(F3代替)→Tenten8223+Enter（osascript）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** key_code mission_control(F3代替)→Tenten8223+Enter（osascript）
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "mission_control",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "shell_command": "/usr/bin/osascript -e 'tell application \"System Events\"' -e 'set s to \"Tenten8223\"' -e 'repeat with i from 1 to length of s' -e 'keystroke character i of s' -e 'end repeat' -e 'keystroke return' -e 'end tell'"
  }
]
```


### 5. Apple vendor expose_desktop(F3代替)→Tenten8223+Enter（osascript）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Apple vendor expose_desktop(F3代替)→Tenten8223+Enter（osascript）
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "apple_vendor_keyboard_key_code": "expose_desktop",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "shell_command": "/usr/bin/osascript -e 'tell application \"System Events\"' -e 'set s to \"Tenten8223\"' -e 'repeat with i from 1 to length of s' -e 'keystroke character i of s' -e 'end repeat' -e 'keystroke return' -e 'end tell'"
  }
]
```


### 6. F3 → Tenten8223+Enter（osascript・1文字ずつ）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F3 → Tenten8223+Enter（osascript・1文字ずつ）
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f3"
}
```

**to:**

```json
[
  {
    "shell_command": "/usr/bin/osascript -e 'tell application \"System Events\"' -e 'set s to \"Tenten8223\"' -e 'repeat with i from 1 to length of s' -e 'keystroke character i of s' -e 'end repeat' -e 'keystroke return' -e 'end tell'"
  }
]
```


### 7. Apple vendor Spotlight(F4相当)→F9

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Apple vendor Spotlight(F4相当)→F9
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "apple_vendor_keyboard_key_code": "spotlight",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f9"
  }
]
```


### 8. Apple vendor Launchpad(F4代替)→F9

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Apple vendor Launchpad(F4代替)→F9
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "apple_vendor_keyboard_key_code": "launchpad",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f9"
  }
]
```


### 9. key_code launchpad(F4代替)→F9

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** key_code launchpad(F4代替)→F9
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "launchpad",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f9"
  }
]
```


### 10. Apple top-case キーボード輝度▼(F5相当)→Option+H

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Apple top-case キーボード輝度▼(F5相当)→Option+H
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "apple_vendor_top_case_key_code": "illumination_down",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "h",
    "modifiers": [
      "left_option"
    ]
  }
]
```


### 11. key_code illumination_decrement(F5代替)→Option+H

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** key_code illumination_decrement(F5代替)→Option+H
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "illumination_decrement",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "h",
    "modifiers": [
      "left_option"
    ]
  }
]
```


### 12. Consumer 音声入力(F5相当)→Option+H

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer 音声入力(F5相当)→Option+H
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "dictation",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "h",
    "modifiers": [
      "left_option"
    ]
  }
]
```


### 13. key_code illumination_increment(F6代替)→F6

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** key_code illumination_increment(F6代替)→F6
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "illumination_increment",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f6"
  }
]
```


### 14. Consumer rewind(F7相当)→Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer rewind(F7相当)→Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "rewind",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option"
    ]
  }
]
```


### 15. Consumer scan_previous_track(F7代替)→Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer scan_previous_track(F7代替)→Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "scan_previous_track",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option"
    ]
  }
]
```


### 16. key_code rewind(F7代替)→Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** key_code rewind(F7代替)→Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "rewind",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option"
    ]
  }
]
```


### 17. Consumer fast_forward(F8相当)→Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer fast_forward(F8相当)→Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "fast_forward",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 18. Consumer fastforward(F8代替・アンダースコアなし)→Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer fastforward(F8代替・アンダースコアなし)→Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "fastforward",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 19. key_code fastforward(F8代替)→Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** key_code fastforward(F8代替)→Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "fastforward",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 20. Consumer scan_next_track(F8代替)→Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer scan_next_track(F8代替)→Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "scan_next_track",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 21. Consumer play_or_pause(F8代替)→Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Consumer play_or_pause(F8代替)→Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "play_or_pause",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 22. key_code play_or_pause(F8代替)→Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** key_code play_or_pause(F8代替)→Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "play_or_pause",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 23. F1 → F13

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F1 → F13
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f1"
}
```

**to:**

```json
[
  {
    "key_code": "f13"
  }
]
```


### 24. F2 → Shift+F13

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F2 → Shift+F13
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f2"
}
```

**to:**

```json
[
  {
    "key_code": "f13",
    "modifiers": [
      "shift"
    ]
  }
]
```


### 25. F4 → F9

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F4 → F9
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f4"
}
```

**to:**

```json
[
  {
    "key_code": "f9"
  }
]
```


### 26. F5 → Option+H

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F5 → Option+H
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f5"
}
```

**to:**

```json
[
  {
    "key_code": "h",
    "modifiers": [
      "left_option"
    ]
  }
]
```


### 27. Insert → F6

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Insert → F6
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "insert",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "f6"
  }
]
```


### 28. F7 → Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F7 → Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f7"
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option"
    ]
  }
]
```


### 29. F8 → Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F8 → Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f8"
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 30. F9 → Control+K

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** F9 → Control+K
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "f9",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "k",
    "modifiers": [
      "control"
    ]
  }
]
```


### 31. 音量下げ（Consumer）→ Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** 音量下げ（Consumer）→ Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "volume_decrement",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option"
    ]
  }
]
```


### 32. 音量上げ（Consumer）→ Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** 音量上げ（Consumer）→ Shift+Option+V
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "consumer_key_code": "volume_increment",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "v",
    "modifiers": [
      "option",
      "shift"
    ]
  }
]
```


### 33. Forward Delete → Space×4+Enter

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Forward Delete → Space×4+Enter
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "delete_forward"
}
```

**to:**

```json
[
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 34. Caps Lock → Backspace

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** Caps Lock → Backspace
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "caps_lock",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "delete_or_backspace"
  }
]
```


### 35. 右Shift 単独タップ→音声入力（Consumer dictation）（他キー併用時は右Shiftのまま）

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** 右Shift 単独タップ→音声入力（Consumer dictation）（他キー併用時は右Shiftのまま）
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "right_shift",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "right_shift",
    "lazy": true
  }
]
```

**extra（parameters / to_if_alone 等）:**

```json
{
  "to_if_alone": [
    {
      "consumer_key_code": "dictation"
    }
  ]
}
```


### 36. 右Option → Space×4+Enter

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Keychron Link-KM - カスタム設定
- **マニピュレータ:** 右Option → Space×4+Enter
- **デバイス条件:** vendor=13364 product=

**from:**

```json
{
  "key_code": "right_option",
  "modifiers": {
    "optional": [
      "any"
    ]
  }
}
```

**to:**

```json
[
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "spacebar"
  },
  {
    "key_code": "return_or_enter"
  }
]
```

---
