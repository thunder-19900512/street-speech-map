const fs = require('fs');
const path = require('path');
const readline = require('readline');

const DATABASE_JSON = path.join(__dirname, '../data/database.json');
const DATABASE_JS = path.join(__dirname, '../data/database.js');
const BACKUP_DIR = path.join(__dirname, '../data/backups');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

console.log("-----------------------------------------");
console.log("🗳 街頭演説マップ データベース更新ツール");
console.log("-----------------------------------------");
console.log("更新用のJSONデータをここに貼り付けて、Enterを押してください。");
console.log("(貼り付けが終わったら Ctrl+D を押して完了)");
console.log("-----------------------------------------");

let inputData = '';

rl.on('line', (line) => {
    inputData += line;
});

rl.on('close', () => {
    if (!inputData.trim()) {
        console.error("エラー: データが空です。");
        process.exit(1);
    }

    try {
        // Validate JSON
        const db = JSON.parse(inputData);

        // Ensure data directory exists
        const dataDir = path.dirname(DATABASE_JSON);
        if (!fs.existsSync(dataDir)) {
            fs.mkdirSync(dataDir, { recursive: true });
        }

        // Ensure backup directory exists
        if (!fs.existsSync(BACKUP_DIR)) {
            fs.mkdirSync(BACKUP_DIR, { recursive: true });
        }

        // Create backup of current version if it exists
        if (fs.existsSync(DATABASE_JSON)) {
            const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
            const backupPath = path.join(BACKUP_DIR, `database_backup_${timestamp}.json`);
            fs.copyFileSync(DATABASE_JSON, backupPath);
            console.log(`✅ バックアップを作成しました: ${path.relative(process.cwd(), backupPath)}`);
        }

        // Update database.json
        fs.writeFileSync(DATABASE_JSON, JSON.stringify(db, null, 4));
        console.log(`✅ ${path.relative(process.cwd(), DATABASE_JSON)} を更新しました。`);

        // Update database.js
        const jsContent = `const GAITOU_DB = ${JSON.stringify(db, null, 4)};`;
        fs.writeFileSync(DATABASE_JS, jsContent);
        console.log(`✅ ${path.relative(process.cwd(), DATABASE_JS)} を更新しました。`);

        console.log("\n✨ すべての更新が完了しました！");

    } catch (e) {
        console.error("❌ エラー: JSONの解析に失敗しました。貼り付けた内容を確認してください。");
        console.error(e.message);
        process.exit(1);
    }
});
