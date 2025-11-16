# Greater East Asia Co-Prosperity Sphere (GEACPS) Mod

## 概要
**GEACPS (Greater East Asia Co-Prosperity Sphere)** は *Hearts of Iron IV* 向けの大型オーバーホール・MODです。  
「日本が大東亜戦争に勝利していたら？」という架空の歴史をベースに、新しい国境線、州、国家方針、イデオロギーなどを追加します。

このMODは、歴史改変シナリオに基づいた独自の世界観を提供し、プレイヤーに新しい戦略的選択肢と歴史的可能性を探求する機会を与えます。

## 主な特徴
- **架空歴史シナリオ**: 日本勝利を前提とした大東亜共栄圏の世界
- **豊富なイデオロギー**: 10種類以上の新規イデオロギーを追加
- **カスタムマップ**: 新しい州・国境線・戦略地域
- **国家方針ツリー**: 各国に独自の国家方針ツリーを実装
- **イベント・ディシジョン**: 史実とは異なる展開を楽しめる各国独自のイベントとディシジョン
- **グラフィック対応**: 大規模マップ修正と日本語フォント対応
- **詳細な世界観**: `通史.txt` に記載された詳細な架空歴史設定

## 必要要件
- **Hearts of Iron IV v1.14.*** (現在のバージョン: 1.14.0)
- **DLC**: 全てのDLCに対応していますが、必須ではありません
- **依存MOD**: なし（スタンドアローンMOD）

**注意**: 本MODは大規模なオーバーホールMODのため、他のオーバーホールMODとの併用は推奨されません。

## インストール方法

### 方法1: Gitクローンを使用（開発者向け）
1. このリポジトリをクローンします。
   ```bash
   git clone https://github.com/GEACPS-development-team/GEACPS_mod.git
   ```

2. クローンしたフォルダを Hearts of Iron IV の MOD フォルダに配置します。
   - **Windows**: `C:\Users\<ユーザー名>\Documents\Paradox Interactive\Hearts of Iron IV\mod\`
   - **Mac**: `~/Documents/Paradox Interactive/Hearts of Iron IV/mod/`
   - **Linux**: `~/.local/share/Paradox Interactive/Hearts of Iron IV/mod/`

3. `descriptor.mod` ファイルをコピーし、`GEACPS_mod.mod` という名前で MOD フォルダ直下に配置します。

4. `GEACPS_mod.mod` ファイルを開き、以下の行を追加します。
   ```
   path="mod/GEACPS_mod"
   ```

### 方法2: ZIPダウンロードを使用（一般ユーザー向け）
1. GitHubページの「Code」→「Download ZIP」からダウンロードします。

2. ダウンロードしたZIPファイルを解凍します。

3. 解凍したフォルダを Hearts of Iron IV の MOD フォルダに配置します（上記のパスを参照）。

4. 上記の方法1の手順3-4を実行します。

## 使い方

### MODの有効化
1. Hearts of Iron IV ランチャーを起動します。
2. 「プレイセット」タブを開きます。
3. 「GEACPS」または「Greater East Asia Co-Prosperity Sphere」を探してチェックを入れます。
4. 「プレイ」ボタンをクリックしてゲームを起動します。

### ゲームの開始
1. シングルプレイヤーを選択します。
2. ブックマーク（開始シナリオ）から好きな時代と国家を選択します。
3. ゲーム設定を調整してゲームを開始します。

### 推奨設定
- **難易度**: 初回プレイ時は「一般兵」または「下級将校」を推奨
- **鉄人モード**: オフ（初回プレイ時）
- **歴史的国家方針**: オフ（MOD独自の展開を楽しむため）

## プロジェクト構造

```
GEACPS_mod/
├── common/           # ゲームルール、国家、イデオロギー、技術など
├── events/           # イベント定義
├── gfx/              # グラフィックリソース
├── history/          # 歴史的初期設定（国家、州、部隊など）
├── interface/        # UI定義
├── localisation/     # 日本語・英語のローカライゼーション
├── map/              # マップデータ
├── music/            # 音楽ファイル
├── portraits/        # 指導者・将軍の肖像画
├── descriptor.mod    # MOD情報ファイル
├── thumbnail.png     # MODサムネイル
├── 通史.txt          # 架空歴史の詳細設定
└── README.md         # このファイル
```

## トラブルシューティング

### MODが表示されない
- `descriptor.mod` が正しく `.mod` ファイルとして MOD フォルダ直下にコピーされているか確認してください。
- MODファイルのパスが正しく設定されているか確認してください。
- ランチャーを再起動してみてください。

### ゲームがクラッシュする
- Hearts of Iron IV のバージョンが v1.14.* であることを確認してください。
- 他のオーバーホールMODを無効化してください。
- ゲームファイルの整合性を確認してください（Steamの場合）。

### 文字化けが発生する
- ゲーム設定で日本語が選択されているか確認してください。
- フォントファイルが正しく配置されているか確認してください。

### その他の問題
問題が解決しない場合は、[Issues](https://github.com/GEACPS-development-team/GEACPS_mod/issues) にて報告してください。

## 開発・貢献

このプロジェクトへの貢献を歓迎します！

### 貢献方法
1. このリポジトリをフォークします。
2. フィーチャーブランチを作成します (`git checkout -b feature/amazing-feature`)
3. 変更をコミットします (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュします (`git push origin feature/amazing-feature`)
5. プルリクエストを作成します。

### 開発ガイドライン
- コードは既存のスタイルに従ってください。
- 大きな変更を行う前に、Issueで議論することを推奨します。
- ローカライゼーションは日本語と英語の両方を更新してください。
- コミットメッセージは明確で説明的なものにしてください。

## バージョン履歴

- **v1.14.0** (最新): Hearts of Iron IV v1.14.* 対応
- 詳細な更新履歴は [Releases](https://github.com/GEACPS-development-team/GEACPS_mod/releases) を参照してください。

## クレジット

このMODは GEACPS development team によって開発・メンテナンスされています。

## ライセンス

このプロジェクトのライセンスについては、リポジトリのライセンスファイルを参照してください。

## リンク

- **GitHub**: [https://github.com/GEACPS-development-team/GEACPS_mod](https://github.com/GEACPS-development-team/GEACPS_mod)
- **Issues**: [https://github.com/GEACPS-development-team/GEACPS_mod/issues](https://github.com/GEACPS-development-team/GEACPS_mod/issues)

---

**免責事項**: このMODは架空の歴史シナリオを題材としたエンターテインメント作品であり、実際の歴史的事実や政治的立場を代表するものではありません。
