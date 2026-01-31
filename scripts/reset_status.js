const fs = require('fs');
const databaseFile = '/Users/yamadayuji/.gemini/antigravity/scratch/gaitou/data/database.json';
const databaseJsFile = '/Users/yamadayuji/.gemini/antigravity/scratch/gaitou/data/database.js';

let db = JSON.parse(fs.readFileSync(databaseFile, 'utf8'));

// すべてのスケジュールエントリのステータスを 0 (自動推定) にリセット
db.forEach(item => {
    item.schedule.forEach(s => {
        s.status = 0;
    });
});

fs.writeFileSync(databaseFile, JSON.stringify(db, null, 4));
fs.writeFileSync(databaseJsFile, `const GAITOU_DB = ${JSON.stringify(db, null, 4)};`);

console.log("All statuses reset to 0 (Auto-estimated) per user policy.");
