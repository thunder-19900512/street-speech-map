import fs from 'fs';
import path from 'path';
import readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const DB_JSON_PATH = path.resolve('data/database.json');
const DB_JS_PATH = path.resolve('data/database.js');
const BACKUP_DIR = path.resolve('data/backups');

async function update() {
    console.log('--- 街頭演説マップ 安全更新ツール ---');
    console.log('管理者モードで出力した新しいJSONを貼り付けてから、Ctrl+D (または Ctrl+Z) を押してください:');

    let lines = [];
    for await (const line of rl) {
        lines.push(line);
    }
    const input = lines.join('\n').trim();

    if (!input) {
        console.error('エラー: 入力が空です。');
        process.exit(1);
    }

    try {
        const newData = JSON.parse(input);

        // 1. バックアップ作成
        if (!fs.existsSync(BACKUP_DIR)) fs.mkdirSync(BACKUP_DIR, { recursive: true });
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const backupPath = path.join(BACKUP_DIR, `database_backup_${timestamp}.json`);

        fs.copyFileSync(DB_JSON_PATH, backupPath);
        console.log(`✅ バックアップを作成しました: ${backupPath}`);

        // 2. database.json の更新
        fs.writeFileSync(DB_JSON_PATH, JSON.stringify(newData, null, 4));
        console.log(`✅ ${DB_JSON_PATH} を更新しました。`);

        // 3. database.js の更新
        const jsContent = `const GAITOU_DB = ${JSON.stringify(newData, null, 4)};`;
        fs.writeFileSync(DB_JS_PATH, jsContent);
        console.log(`✅ ${DB_JS_PATH} を更新しました。`);

        console.log('\n✨ すべての更新が正常に完了しました！Gitで変更を確認してコミットしてください。');

    } catch (e) {
        console.error('❌ エラー: 入力されたデータが正しいJSON形式ではありません。');
        console.error(e.message);
        process.exit(1);
    }
}

update();
