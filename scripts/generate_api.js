const fs = require('fs');
const path = require('path');

// 設定
const DATA_FILE = path.join(__dirname, '../data/database.json');
const API_DEST = path.join(__dirname, '../api/v1');

// メイン処理
function generateApi() {
    console.log('🚀 API生成を開始します...');

    // データの読み込み
    if (!fs.existsSync(DATA_FILE)) {
        console.error('❌ database.json が見つかりません。');
        return;
    }
    const rawData = fs.readFileSync(DATA_FILE, 'utf8');
    const db = JSON.parse(rawData);

    // 出力ディレクトリの作成
    const folders = ['dates', 'candidates', 'prefectures'];
    folders.forEach(f => {
        const dir = path.join(API_DEST, f);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }
    });

    // 1. 全データ
    fs.writeFileSync(path.join(API_DEST, 'all.json'), JSON.stringify(db, null, 2));

    // 2. 日付別
    const dateMap = {};
    // 3. 候補者別
    const candidateMap = {};

    db.forEach(item => {
        // 日付別
        if (!dateMap[item.date]) dateMap[item.date] = [];
        dateMap[item.date].push(item);

        // 候補者別
        if (!candidateMap[item.candidate]) candidateMap[item.candidate] = [];
        candidateMap[item.candidate].push(item);
    });

    // ファイル書き出し
    Object.keys(dateMap).forEach(date => {
        fs.writeFileSync(path.join(API_DEST, 'dates', `${date}.json`), JSON.stringify(dateMap[date], null, 2));
    });

    Object.keys(candidateMap).forEach(name => {
        // ファイル名として安全な名前に（一応）
        const safeName = name.replace(/\s+/g, '_');
        fs.writeFileSync(path.join(API_DEST, 'candidates', `${safeName}.json`), JSON.stringify(candidateMap[name], null, 2));
    });

    console.log(`✅ APIの生成が完了しました！`);
    console.log(`📍 場所: ${API_DEST}`);
    console.log(`   - 全データ: all.json`);
    console.log(`   - 日付別: ${Object.keys(dateMap).length} ファイル`);
    console.log(`   - 候補者別: ${Object.keys(candidateMap).length} ファイル`);
}

generateApi();
