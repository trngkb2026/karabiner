# TENBT03 テンキー 左Shift+8/9 → F13 系 マッピング追加 ＋ GUI拡張 完了報告

**日時:** 2026-04-20
**対象デバイス:** TENBT03（vendor_id 9427 / product_id 12427）
**対象ファイル:**
- `karabiner.json`（本体設定）
- `karabiner-manager/gui/index.html`（GUI管理画面）

---

## 1. 追加したマッピング

| from | to |
|------|------|
| `left_shift` + `keypad_8` | `f13` |
| `left_shift` + `keypad_9` | `shift` + `f13` |

- TENBT03 からの入力のみに反応（`device_if` で vendor_id/product_id を制約）
- 他デバイスの `8`/`9` には影響しない
- `optional: ["any"]` を指定しているため、Ctrl や Option など他の修飾キーを同時に押していても発火

## 2. GUI を修飾キー対応に拡張（この報告の主目的）

### 追加UI（マッピング追加ダイアログ）

- **From 修飾キー (mandatory)**: Shift / Ctrl / Opt / Cmd のチップをON/OFFで選択
- **他の修飾キーも許容 (optional: any)**: 有効にすると `modifiers.optional: ["any"]` が付与されます（別の修飾キーを同時に押しても発火）
- **左右を区別する**: 有効にすると `L·Shift` / `R·Shift` のように左右別のチップに展開（Karabiner の `left_shift` / `right_shift` に対応）
- **To 修飾キー**: TOキー側に付与する修飾キー（例: `f13` + Shift）のチップ

### 制約

- Simple Modification / Fn Function Key は Karabiner の仕様により From 側の修飾キーは不可（UI も自動的に非表示）。To 側の修飾キーは全タイプで指定可能
- 左右区別モードのチップと非区別モードは混ぜられない（トグル切り替え時に一旦 UI がリフレッシュ）

### 使い方

1. Karabiner Manager GUI を起動（`python3 karabiner-manager/gui/server.py`）
2. ブラウザで対象デバイス（例: TENBT03 テンキー）を選択
3. 「+ 追加」→ 種別「Complex Modification」
4. ルール説明を入力（省略時は `Custom rule`）
5. From キーを選択（⌨ボタンで実機キーキャプチャも可）
6. 「左右を区別する」をONにして `L·Shift` をクリック → `mandatory: ["left_shift"]`
7. 「他の修飾キーも許容」をONにして `optional: ["any"]`
8. To キー選択、Shift などの修飾を追加
9. 「追加」

## 3. 変更ファイルとバックアップ

| 項目 | パス |
|------|------|
| 本体 | `karabiner.json`（complex_modifications.rules に 1 ルール追記 / 全10ルール） |
| GUI HTML | `karabiner-manager/gui/index.html`（+85行 / -3行 程度） |
| バックアップ（変更前） | `karabiner.json.bak.tenbt03_lshift_20260420180820` |
| マッピング一覧 | `karabiner-manager/mappings_by_device/v9427_p12427.md` |

## 4. 実施した検証

- JSON構文: `python3 -m json.tool` → OK
- GUIサーバ疎通: ローカルでserver.pyを起動し `/api/config` が 200 を返し、TENBT03 4件を含む9グループが返ることを確認
- 修飾キー生成: `/api/add` に `{mandatory:["shift"], optional:["any"]}` を投入 → `karabiner.json` に期待通り反映されることを確認（テスト後に削除しクリーンアップ）
- 左右区別パターン: `/api/add` に `{mandatory:["left_shift"]}` + `to.modifiers:["left_shift"]` を投入 → 手動追加と同じ構造を再現できることを確認（テスト後削除）
- 旧ルール温存: 既存の TENBT03 ルール（Del → Space×4+Enter、F2 → Tenten8223+Enter）は無改変

## 5. 未検証事項（要実機確認）

- 実際にTENBT03テンキーで `左Shift + 8` を押したときに `f13` が発行されるかの実機テスト（物理キー操作が必要）
  - Karabiner-EventViewer を開き、8/9 が `keypad_8`/`keypad_9` として送られることを併せて確認してください
- サブプロセス（`karabiner_cli --format-json`）は macOS 実機では存在しますが、Mac 以外のサンドボックスでは呼び出しエラーになります（実機動作には影響なし）

## 6. 反応しなかった場合のチェック

1. Num Lock 状態（ON でない場合、`keypad_8` が `up_arrow` に変換されることがあります）
2. TENBT03 が `left_shift`（本体キーボード）と `keypad_8`（テンキー）を別デバイス扱いしている場合、`device_if` は keypad_8 側で効き、shift は本体からでも OK（今回の設定で問題なし）
3. Karabiner-Elements の再起動や設定リロード（`karabiner_cli --select-profile` など）

## 7. ロールバック手順

変更前に戻したい場合:

```bash
cp ~/.config/karabiner/karabiner.json.bak.tenbt03_lshift_20260420180820 \
   ~/.config/karabiner/karabiner.json
```

GUI側を戻したい場合は Git 管理下なので:

```bash
cd ~/.config/karabiner
git diff karabiner-manager/gui/index.html   # 変更確認
git checkout karabiner-manager/gui/index.html  # 戻す
```
