document.addEventListener('DOMContentLoaded', () => {
    const ADMIN_URL = "https://thunder-19900512.github.io/street-speech-map/index.html?mode=admin";
    const SHEET_URL = "https://docs.google.com/spreadsheets/d/1-ZZ-xkeHHTN4g69picsPUBgg4Xz-cOjD7Sv3nkAHM9o/edit?gid=0#gid=0";
    const DROPBOX_URL = "https://www.dropbox.com/home/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%20%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88/2026%E8%A1%86%E9%99%A2%E9%81%B8_%E8%A1%97%E5%AE%A3%E3%82%AB%E3%83%BC%E3%83%89%E5%8F%8E%E9%9B%86";
    const X_POST_URL = "https://x.com/YamadaY_Mirai/status/2016879578657305015";

    const updateTab = async (url) => {
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        if (tab) {
            chrome.tabs.update(tab.id, { url });
        } else {
            window.open(url, '_blank');
        }
    };

    // 管理者ページを開く
    document.getElementById('openAdmin').addEventListener('click', () => {
        updateTab(ADMIN_URL);
        markDone(1);
    });

    // スプシを開く
    document.getElementById('openSheet').addEventListener('click', () => {
        updateTab(SHEET_URL);
        markDone(3);
    });

    // Dropboxを開く
    document.getElementById('openDropbox').addEventListener('click', () => {
        updateTab(DROPBOX_URL);
        markDone(4);
    });

    // X発信
    document.getElementById('openX').addEventListener('click', () => {
        updateTab(X_POST_URL);
        markDone(7);
    });

    // コマンドコピー機能
    document.querySelectorAll('.copy-cmd').forEach(btn => {
        btn.addEventListener('click', () => {
            const text = btn.getAttribute('data-copy');
            navigator.clipboard.writeText(text).then(() => {
                const originalText = btn.innerText;
                btn.innerText = "コピー完了！";
                setTimeout(() => btn.innerText = originalText, 1500);

                // 直近のステップを完了にする（おおよその判定）
                if (text.includes('update_db')) markDone(2);
                if (text.includes('photosフォルダ')) markDone(5);
                if (text.includes('git push')) markDone(6);
                if (text.includes('街頭演説マップ')) markDone(7);
            });
        });
    });

    // 進捗状況の読み込み
    chrome.storage.local.get(['doneSteps'], (result) => {
        const doneSteps = result.doneSteps || [];
        doneSteps.forEach(s => {
            const el = document.getElementById(`step${s}`);
            if (el) el.classList.add('done');
        });
    });

    // リセット
    document.getElementById('reset').addEventListener('click', () => {
        chrome.storage.local.set({ doneSteps: [] }, () => {
            location.reload();
        });
    });

    function markDone(stepNum) {
        const el = document.getElementById(`step${stepNum}`);
        if (el) el.classList.add('done');

        chrome.storage.local.get(['doneSteps'], (result) => {
            let doneSteps = result.doneSteps || [];
            if (!doneSteps.includes(stepNum)) {
                doneSteps.push(stepNum);
                chrome.storage.local.set({ doneSteps });
            }
        });
    }
});
