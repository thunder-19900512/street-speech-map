# 🗺 街頭演説マップ 公開API (v1)

このAPIは、全国の街頭演説スケジュールをプログラムから取得するためのものです。
全データを取得するほか、日付別や候補者別に絞り込んだ軽量なデータを取得できます。

## 📍 エンドポイント

ベースURL: `https://[あなたのユーザー名].github.io/[リポジトリ名]/api/v1`

### 1. 全データの取得
全てのスケジュールを一括で取得します。
- **URL**: `/all.json`
- **ファイルサイズ**: 約500KB〜

### 2. 日付別で取得 (推奨)
特定の日付だけのデータを取得します。通信量を大幅に削減できます。
- **URL**: `/dates/[YYYY-MM-DD].json`
- **例**: `/dates/2026-02-07.json`

### 3. 候補者別で取得
特定の候補者の過去・未来の全スケジュールを抽出します。
- **URL**: `/candidates/[候補者名].json`
- **例**: `/candidates/安野貴博.json`
  ※ 候補者名にスペースが含まれる場合は `_` に置換されています。

---

## 🛠 外部サイトからの利用 (CORSについて)

GitHub Pagesで公開している場合、標準でCORS（要素間リソース共有）が許可されているため、外部のJavaScriptから直接 `fetch()` して利用することが可能です。

### 利用例 (JavaScript)

```javascript
// 明日の演説予定を取得して表示する例
const date = "2026-02-07";
fetch(`https://[あなたのURL]/api/v1/dates/${date}.json`)
  .then(res => res.json())
  .then(data => {
    console.log(`${date}の予定は ${data.length} 件あります`);
    data.forEach(item => {
      console.log(`${item.candidate}: ${item.schedule[0].location}`);
    });
  });
```

## 📝 データの更新
このAPIは `database.json` が更新されるたびに、GitHub Actions（または手動スクリプト）によって自動生成されます。
