# Karabiner マッピング（デバイス非依存）

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
