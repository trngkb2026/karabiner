# Karabiner マッピング（全件）デバイス別ファイルの連結です。目次は [_index.md](_index.md)。---## global.md# Karabiner マッピング（デバイス非依存）

次を含みます。

- `device_if` 条件のない複合ルール
- プロファイル直下の **fn_function_keys**（F1–F12）

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. Space: 単発でスペース / 長押し・併用で Command

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Space: 単発でスペース / 長押し・併用で Command

**from:**

```json
{
  "key_code": "spacebar",
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
    "key_code": "left_command",
    "lazy": true
  }
]
```

**extra（parameters / to_if_alone 等）:**

```json
{
  "parameters": {
    "basic.to_if_alone_timeout_milliseconds": 400,
    "basic.to_if_held_down_threshold_milliseconds": 250
  },
  "to_if_alone": [
    {
      "key_code": "spacebar"
    }
  ],
  "to_if_held_down": [
    {
      "key_code": "left_command"
    }
  ]
}
```


### 2. ⌘W → スペース

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** ⌘W → スペース

**from:**

```json
{
  "key_code": "w",
  "modifiers": {
    "mandatory": [
      "command"
    ],
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
    "key_code": "spacebar"
  }
]
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
    "shell_command": "osascript -e 'tell application \"System Events\"' -e 'set s to \"Tenten8223\"' -e 'repeat with i from 1 to length of s' -e 'keystroke character i of s' -e 'end repeat' -e 'keystroke return' -e 'end tell'"
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


### 7. 右Option → Spotlight

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** Magic Keyboard - カスタム設定
- **マニピュレータ:** 右Option → Spotlight
- **デバイス条件:** vendor=76 product=671

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
    "apple_vendor_keyboard_key_code": "spotlight"
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


### 11. device_simple_modification

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


### 12. device_fn_function_key

- **種別:** `device_fn_function_key`
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
    "key_code": "f1"
  }
]
```


### 13. device_fn_function_key

- **種別:** `device_fn_function_key`
- **プロファイル:** `240106`
- **デバイス条件:** {
  "is_keyboard": true,
  "product_id": 671,
  "vendor_id": 76
}

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

## v1452_p599.md

# Karabiner マッピング（vendor 1452 / product 599）

- **vendor_id:** `1452`
- **product_id:** `599`

**デバイス条件:** vendor=1452 product=599

このファイルには、上記デバイス向けの **複合ルール** と **simple_modifications** / **fn_function_keys** をまとめています。

生成: `karabiner-manager/scripts/export_mappings_md.py`

---

### 1. Caps → 英数（トグル）

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


### 2. Caps → かな（トグル）

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


### 3. ボタン1（ポインティング）→ 音声入力

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


### 4. ボタン3（ポインティング）→ Enter

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** ボタン3（ポインティング）→ Enter
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
    "key_code": "return_or_enter"
  }
]
```


### 5. application キー → アプリケーションのウィンドウ（Control+↓ / osascript）

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
    "shell_command": "/usr/bin/osascript -e 'tell application \"System Events\" to key code 125 using control down'"
  }
]
```


### 6. ac_home（Consumer）→ デスクトップ表示（F11 / osascript）

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
    "shell_command": "/usr/bin/osascript -e 'tell application \"System Events\" to key code 103'"
  }
]
```


### 7. ミュート（Consumer）→ Mission Control

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


### 8. 音量下げ（Consumer）→ Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 音量下げ（Consumer）→ Option+V
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
    "key_code": "v",
    "modifiers": [
      "option"
    ]
  }
]
```


### 9. 音量上げ（Consumer）→ Shift+Option+V

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** X8 BLE Keyboard - カスタム設定
- **マニピュレータ:** 音量上げ（Consumer）→ Shift+Option+V
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
      "option",
      "shift"
    ]
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

### 1. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "escape"
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


### 2. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "keypad_8"
  },
  {
    "key_code": "keypad_2"
  },
  {
    "key_code": "keypad_2"
  },
  {
    "key_code": "keypad_3"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 3. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "8",
  "modifiers": {
    "mandatory": [
      "shift"
    ],
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
    "key_code": "x",
    "modifiers": [
      "command",
      "right_shift"
    ]
  }
]
```


### 4. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "9",
  "modifiers": {
    "mandatory": [
      "shift"
    ],
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
    "key_code": "h",
    "modifiers": [
      "command",
      "shift",
      "option"
    ]
  }
]
```


### 5. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
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


### 6. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
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
    "key_code": "keypad_1",
    "modifiers": [
      "option"
    ]
  }
]
```


### 7. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "left_control"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_2",
    "modifiers": [
      "option"
    ]
  }
]
```


### 8. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "equal_sign"
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


### 9. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "return_or_enter",
    "modifiers": [
      "command"
    ]
  }
]
```


### 10. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "left_shift"
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


### 11. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "japanese_kana"
  }
]
```


### 12. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_7"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_7"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 13. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_8"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_8"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 14. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_9"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_9"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 15. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "comma",
    "modifiers": [
      "command"
    ]
  }
]
```


### 16. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_4"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_4"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 17. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_5"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_5"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 18. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_6"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_6"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 19. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "left_arrow",
    "modifiers": [
      "command",
      "option"
    ]
  }
]
```


### 20. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "right_arrow",
    "modifiers": [
      "command",
      "option"
    ]
  }
]
```


### 21. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_1"
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


### 22. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_2"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_2"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 23. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_3"
}
```

**to:**

```json
[
  {
    "key_code": "keypad_3"
  },
  {
    "key_code": "return_or_enter"
  }
]
```


### 24. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_enter"
}
```

**to:**

```json
[
  {
    "key_code": "spacebar"
  }
]
```


### 25. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

**from:**

```json
{
  "key_code": "keypad_0"
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


### 26. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
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
    "key_code": "delete_or_backspace"
  }
]
```


### 27. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "c",
    "modifiers": [
      "control"
    ]
  }
]
```


### 28. TENBT03 (MCO) - カスタム設定

- **種別:** `complex_modification`
- **プロファイル:** `240106`
- **ルールグループ:** TENBT03 (MCO) - カスタム設定
- **デバイス条件:** vendor=9427 product=12427

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
    "key_code": "f13",
    "modifiers": [
      "shift"
    ]
  }
]
```


### 29. device_simple_modification

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
  "key_code": "escape"
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


### 30. device_simple_modification

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
  "key_code": "f4"
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


### 31. device_simple_modification

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
  "key_code": "grave_accent_and_tilde"
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


### 32. device_simple_modification

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
  "key_code": "keypad_asterisk"
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


### 33. device_simple_modification

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
  "key_code": "keypad_enter"
}
```

**to:**

```json
[
  {
    "key_code": "spacebar"
  }
]
```


### 34. device_simple_modification

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
  "key_code": "keypad_period"
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


### 35. device_simple_modification

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
    "consumer_key_code": "dictation"
  }
]
```


### 36. device_simple_modification

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
  "key_code": "left_shift"
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


### 37. device_simple_modification

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
    "key_code": "japanese_kana"
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
  "key_code": "f20"
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
