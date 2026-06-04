import json
import time
import urllib.request
import urllib.parse
from datetime import datetime

data = [
    {
        "id": str(int(time.time()*1000)),
        "date": "2026-05-14",
        "day_of_week": "木",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260514_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "09:15", "location": "新潟駅万代口 第5マルカビル前", "query": "新潟市中央区万代1丁目3 新潟駅万代口 第5マルカビル"},
            {"time": "11:30", "location": "ベイシア様隣 靴のかかつ 豊栄店様", "query": "新潟市北区葛塚 ベイシア 豊栄店"},
            {"time": "13:10", "location": "チャレンジャー 燕三条店様", "query": "新潟県燕市井土巻 チャレンジャー 燕三条店"},
            {"time": "15:00", "location": "アオーレ長岡", "query": "新潟県長岡市大手通 アオーレ長岡"},
            {"time": "17:00", "location": "上越文化会館", "query": "新潟県上越市新光町 上越文化会館"},
            {"time": "19:00", "location": "ヒスイ王国館", "query": "新潟県糸魚川市大町 ヒスイ王国館"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+1),
        "date": "2026-05-15",
        "day_of_week": "金",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260515_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "08:00", "location": "デンカ(株)様 青海工場正門前", "query": "新潟県糸魚川市青海 デンカ 青海工場正門"},
            {"time": "09:10", "location": "能生商工会前", "query": "新潟県糸魚川市能生 能生商工会"},
            {"time": "11:35", "location": "(株)山崎建設様前", "query": "新潟県妙高市東陽町2-20 株式会社山﨑建設"},
            {"time": "15:40", "location": "雪だるま物産館", "query": "新潟県上越市安塚区樽田 雪だるま物産館"},
            {"time": "17:45", "location": "ユーモール様", "query": "新潟県十日町市本町 ユーモール"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+2),
        "date": "2026-05-16",
        "day_of_week": "土",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260516_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "09:30", "location": "JAえちご中越越路支所様", "query": "新潟県長岡市浦 JAえちご中越 越路支所"},
            {"time": "15:00", "location": "JAえちご中越見附西支店様 駐車場", "query": "新潟県見附市上新田町 JAえちご中越 見附西支店"},
            {"time": "16:00", "location": "トチオーレ", "query": "新潟県長岡市栃尾宮沢 トチオーレ"},
            {"time": "17:00", "location": "花みずき温泉 喜芳", "query": "新潟県長岡市みずき野 花みずき温泉 喜芳"},
            {"time": "17:35", "location": "旧良寛牛乳 跡地", "query": "新潟県三島郡出雲崎町大門260-1 旧良寛牛乳"},
            {"time": "18:20", "location": "(株)水倉組様和島営業所駐車場", "query": "新潟県長岡市和島中沢 (株)水倉組 和島営業所"},
            {"time": "19:10", "location": "(株)中元組様駐車場", "query": "新潟県柏崎市田中7-7 中元組 柏崎営業所"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+3),
        "date": "2026-05-17",
        "day_of_week": "日",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260517_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "10:30", "location": "いっぺこーと", "query": "新潟県新潟市西区亀貝 いっぺこーと"},
            {"time": "14:00", "location": "万代シティ ビルボードプレイス前", "query": "新潟県新潟市中央区八千代 万代シテイ ビルボードプレイス"},
            {"time": "15:00", "location": "酒屋町民の家 (個人演説会)", "query": "新潟県新潟市江南区酒屋町 酒屋町民の家"},
            {"time": "16:30", "location": "大江山地区 農村環境改善センター (個人演説会)", "query": "新潟県新潟市江南区細山 大江山地区農村環境改善センター"},
            {"time": "18:10", "location": "河渡マーケットシティ前", "query": "新潟県新潟市東区河渡 河渡マーケットシティ"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+4),
        "date": "2026-05-18",
        "day_of_week": "月",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260518_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "08:00", "location": "関川村役場前", "query": "新潟県関川村 関川村役場"},
            {"time": "08:50", "location": "胎内市役所 黒川支所前", "query": "新潟県胎内市 黒川支所"},
            {"time": "10:00", "location": "JA北新潟 営農センター様", "query": "新潟県胎内市本郷字家の下493-2 JA北新潟 胎内営農センター"},
            {"time": "11:50", "location": "月岡温泉足湯前広場", "query": "新潟県新発田市月岡温泉 月岡温泉足湯前広場"},
            {"time": "15:30", "location": "旧第四銀行新津支店様前 (新潟市秋葉区新津本町2-4-15)", "query": "新潟市秋葉区新津本町2-4-15 旧第四銀行新津支店"},
            {"time": "18:10", "location": "ウオロク松浜店様前", "query": "新潟市東区松浜 ウオロク松浜店"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+5),
        "date": "2026-05-19",
        "day_of_week": "火",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260519_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "10:30", "location": "あいかわ開発総合センター", "query": "新潟県佐渡市相川二町目 あいかわ開発総合センター"},
            {"time": "13:00", "location": "アミューズメント佐渡", "query": "新潟県佐渡市中原 アミューズメント佐渡"},
            {"time": "15:45", "location": "あゆす会館", "query": "新潟県佐渡市羽茂本郷 あゆす会館"},
            {"time": "18:25", "location": "道の駅 あいぽーと佐渡", "query": "新潟県佐渡市両津夷 道の駅 あいぽーと佐渡"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+6),
        "date": "2026-05-20",
        "day_of_week": "水",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260520_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "12:30", "location": "田上町交流会館", "query": "新潟県南蒲原郡田上町大字田上 田上町交流会館"},
            {"time": "16:00", "location": "ハイブ長岡", "query": "新潟県長岡市千秋 ハイブ長岡"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+7),
        "date": "2026-05-21",
        "day_of_week": "木",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260521_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "09:15", "location": "雪国おくにじまん会館", "query": "新潟県南魚沼市塩沢 雪国おくにじまん会館"},
            {"time": "11:30", "location": "旧第四銀行小出支店様前 (魚沼市本町1丁目 本町バス停付近)", "query": "新潟県魚沼市本町1丁目 旧第四銀行小出支店"},
            {"time": "16:00", "location": "原信 桜町店様前", "query": "新潟県小千谷市桜町 原信 桜町店"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+8),
        "date": "2026-05-22",
        "day_of_week": "金",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260522_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "08:00", "location": "JAえちご上越浦川原物産館様前", "query": "新潟県上越市浦川原区顕聖寺 JAえちご上越 浦川原物産館"},
            {"time": "12:00", "location": "津南町役場 正面駐車場", "query": "新潟県中魚沼郡津南町大字下船渡 津南町役場"},
            {"time": "14:40", "location": "第四北越銀行 湯沢支店様前", "query": "新潟県南魚沼郡湯沢町大字湯沢 第四北越銀行 湯沢支店"},
            {"time": "15:30", "location": "JAみなみ魚沼様 大木六低温倉庫前", "query": "新潟県南魚沼市大木六 JAみなみ魚沼 大木六低温倉庫"},
            {"time": "16:00", "location": "六日町郵便局様前", "query": "新潟県南魚沼市六日町 六日町郵便局"},
            {"time": "17:00", "location": "第四北越銀行 十日町支店様前", "query": "新潟県十日町市本町 第四北越銀行 十日町支店"},
            {"time": "18:00", "location": "十日町市 川西支所前", "query": "新潟県十日町市上野 甲 十日町市役所川西支所"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+9),
        "date": "2026-05-23",
        "day_of_week": "土",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260523_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "09:30", "location": "直江津駅前 北口", "query": "新潟県上越市東町 直江津駅前北口"},
            {"time": "12:55", "location": "原信岩上店前", "query": "新潟県柏崎市岩上 原信 岩上店"},
            {"time": "13:50", "location": "ラピカ北側駐車場", "query": "新潟県刈羽郡刈羽村大字刈羽 生涯学習センター「ラピカ」"},
            {"time": "16:30", "location": "(株)中村組 駐車場", "query": "新潟県長岡市与板町与板642 株式会社中村組"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+10),
        "date": "2026-05-24",
        "day_of_week": "日",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260524_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "10:15", "location": "弥彦神社 一の鳥居前", "query": "新潟県西蒲原郡弥彦村弥彦 弥彦神社 一の鳥居"},
            {"time": "15:30", "location": "亀田郷土地改良区 (個人演説会)", "query": "新潟市江南区泉町 亀田郷土地改良区"},
            {"time": "18:30", "location": "新潟駅万代口 マルタケビル前", "query": "新潟市中央区東大通 新潟駅万代口 マルタケビル"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+11),
        "date": "2026-05-25",
        "day_of_week": "月",
        "candidate": "はなずみ英世",
        "prefecture": "新潟県",
        "constituency": "新潟県",
        "party": "無所属",
        "image_path": "photos/260525_新潟県_はなずみ英世 ギア+.jpeg",
        "schedule": [
            {"time": "08:30", "location": "猿沢コミュニティセンター", "query": "新潟県村上市猿沢 猿沢コミュニティセンター"},
            {"time": "14:00", "location": "胎内市役所前", "query": "新潟県胎内市新栄町 胎内市役所"},
            {"time": "15:10", "location": "加治川地区体育館前", "query": "新潟県新発田市住田 加治川地区体育館"},
            {"time": "16:00", "location": "上館公会堂 (個人演説会)", "query": "新潟県新発田市上館 上館公会堂"},
            {"time": "16:45", "location": "(株)岩村物産 紫雲寺SS隣", "query": "新潟県新発田市稲荷岡796 株式会社岩村物産 紫雲寺給油所"}
        ]
    }
]

import os
import sqlite3

def geocode(query):
    # Nominatim fallback or just a basic search, if not found use default lat lng (Tokyo roughly or Prefecture center)
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Antigravity/1.0'})
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode())
            if res and len(res) > 0:
                return float(res[0]['lat']), float(res[0]['lon'])
    except:
        pass
    
    # Try just city
    parts = query.split(' ')
    if len(parts) > 1:
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={urllib.parse.quote(parts[0])}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Antigravity/1.0'})
        try:
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode())
                if res and len(res) > 0:
                    return float(res[0]['lat']), float(res[0]['lon'])
        except:
            pass
            
    # Default Fallback based on prefecture
    if "秋田" in query: return 39.7186, 140.1023 # Akita
    if "島根" in query: return 35.4722, 133.0505 # Shimane
    if "新潟" in query: return 37.9024, 139.0232 # Niigata
    return 35.6895, 139.6917

# Load existing database
db_path = 'data/database.json'
with open(db_path, 'r', encoding='utf-8') as f:
    existing_db = json.load(f)

for item in data:
    for sched in item['schedule']:
        lat, lng = geocode(sched['query'])
        sched['lat'] = lat
        sched['lng'] = lng
        sched['status'] = 0
        del sched['query']
        time.sleep(1.0) # respect Nominatim limit
    
    # Check for duplicates using date and candidate
    duplicate = False
    for existing in existing_db:
        if existing['date'] == item['date'] and existing['candidate'] == item['candidate']:
            # We assume it's duplicate
            duplicate = True
            break
            
    if not duplicate:
        existing_db.append(item)

# Print as JSON
print(json.dumps(existing_db, ensure_ascii=False, indent=4))
