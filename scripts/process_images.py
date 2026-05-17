import json
import time
import urllib.request
import urllib.parse
from datetime import datetime

data = [
    {
        "id": str(int(time.time()*1000)),
        "date": "2026-02-07",
        "day_of_week": "土",
        "candidate": "村岡としひで",
        "prefecture": "秋田県",
        "constituency": "秋田県",
        "party": "国民民主党",
        "image_path": "photos/260207_秋田県_村岡としひで.jpeg",
        "schedule": [
            {"time": "19:30", "location": "羽後信用金庫 本店前", "query": "秋田県由利本荘市本荘13 羽後信用金庫 本店"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+1),
        "date": "2026-02-05",
        "day_of_week": "木",
        "candidate": "福原じゅんじ",
        "prefecture": "秋田県",
        "constituency": "秋田2区",
        "party": "自民党",
        "image_path": "photos/260205_秋田県_福原じゅんじ.jpeg",
        "schedule": [
            {"time": "12:20", "location": "道の駅かみこあに", "query": "秋田県上小阿仁村 道の駅かみこあに"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+2),
        "date": "2026-02-04",
        "day_of_week": "水",
        "candidate": "村岡としひで",
        "prefecture": "秋田県",
        "constituency": "秋田県",
        "party": "国民民主党",
        "image_path": "photos/260204_秋田県_村岡としひで.jpeg",
        "schedule": [
            {"time": "15:20", "location": "横手 イオン隣 JRAウィンズ横手正面", "query": "秋田県横手市 ウィンズ横手"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+3),
        "date": "2026-01-31",
        "day_of_week": "土",
        "candidate": "たかがい恵美子",
        "prefecture": "島根県",
        "constituency": "島根1区",
        "party": "自民党",
        "image_path": "photos/260131_島根県_たかがい恵美子_2.jpeg",
        "schedule": [
            {"time": "13:20", "location": "ひまり大庭店さん", "query": "島根県松江市 ひまり大庭店"},
            {"time": "14:00", "location": "西津田会館", "query": "島根県松江市 西津田会館"},
            {"time": "14:55", "location": "いこい家小浜さん", "query": "島根県松江市 いこい家小浜"},
            {"time": "15:20", "location": "松江駅前", "query": "島根県松江市 松江駅"},
            {"time": "16:00", "location": "城西公民館", "query": "島根県松江市 城西公民館"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+4),
        "date": "2026-01-31",
        "day_of_week": "土",
        "candidate": "たかがい恵美子",
        "prefecture": "島根県",
        "constituency": "島根1区",
        "party": "自民党",
        "image_path": "photos/260131_島根県_たかがい恵美子.jpeg",
        "schedule": [
            {"time": "09:00", "location": "三刀屋バスセンター前", "query": "島根県雲南市 三刀屋バスセンター"},
            {"time": "11:10", "location": "佐世簡易郵便局さん", "query": "島根県雲南市 佐世簡易郵便局"},
            {"time": "12:45", "location": "須賀曽田屋さん前", "query": "島根県雲南市 須賀曽田屋"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+5),
        "date": "2026-01-29",
        "day_of_week": "木",
        "candidate": "たかがい恵美子",
        "prefecture": "島根県",
        "constituency": "島根1区",
        "party": "自民党",
        "image_path": "photos/260129_島根県_たかがい恵美子.jpeg",
        "schedule": [
            {"time": "10:30", "location": "まるなか建設さん", "query": "島根県松江市 まるなか建設 湖南テクノパーク"},
            {"time": "11:45", "location": "松江流通センター会館前", "query": "島根県松江市 松江流通センター会館"},
            {"time": "12:20", "location": "鉄工団地体育館前", "query": "島根県松江市 鉄工団地体育館"},
            {"time": "12:40", "location": "アースサポートさん駐車場", "query": "島根県松江市 アースサポート"},
            {"time": "17:45", "location": "安来第一病院", "query": "島根県安来市 安来第一病院"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+6),
        "date": "2026-01-28",
        "day_of_week": "水",
        "candidate": "たかがい恵美子",
        "prefecture": "島根県",
        "constituency": "島根1区",
        "party": "自民党",
        "image_path": "photos/260128_島根県_たかがい恵美子_2.jpeg",
        "schedule": [
            {"time": "16:40", "location": "横田蔵市駐車場", "query": "島根県奥出雲町 横田蔵市"},
            {"time": "17:15", "location": "旧JA鳥上支所前", "query": "島根県奥出雲町 鳥上支所"},
            {"time": "17:40", "location": "八川郵便局前", "query": "島根県奥出雲町 八川郵便局"},
            {"time": "18:15", "location": "馬木コミュニティーセンター前", "query": "島根県奥出雲町 馬木コミュニティーセンター"},
            {"time": "18:50", "location": "絲原記念館売店前", "query": "島根県奥出雲町 絲原記念館"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+7),
        "date": "2026-01-28",
        "day_of_week": "水",
        "candidate": "たかがい恵美子",
        "prefecture": "島根県",
        "constituency": "島根1区",
        "party": "自民党",
        "image_path": "photos/260128_島根県_たかがい恵美子.jpeg",
        "schedule": [
            {"time": "10:25", "location": "交流センターとんばらさん", "query": "島根県飯南町 交流センターとんばら"},
            {"time": "11:00", "location": "憩いの郷衣掛さん", "query": "島根県飯南町 憩いの郷衣掛"},
            {"time": "14:40", "location": "三沢郵便局前", "query": "島根県奥出雲町 三沢郵便局"},
            {"time": "15:10", "location": "阿井コミュニティーセンター前", "query": "島根県奥出雲町 阿井コミュニティーセンター"},
            {"time": "15:50", "location": "役場仁多庁舎前", "query": "島根県奥出雲町 仁多庁舎"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+8),
        "date": "2025-07-14",
        "day_of_week": "月",
        "candidate": "なかいずみ松司",
        "prefecture": "秋田県",
        "constituency": "秋田選挙区",
        "party": "自民党",
        "image_path": "photos/250714_秋田県_なかいずみ松司.jpg",
        "schedule": [
            {"time": "09:00", "location": "JA秋田おばこ総合本部", "query": "秋田県大仙市 JA秋田おばこ総合本部"},
            {"time": "09:25", "location": "大曲商工会議所", "query": "秋田県大仙市 大曲商工会議所"},
            {"time": "09:50", "location": "大仙市役所", "query": "秋田県大仙市 大仙市役所"},
            {"time": "10:05", "location": "仙北平野土地改良区", "query": "秋田県大仙市 仙北平野土地改良区"},
            {"time": "15:50", "location": "太田 農業振興情報センター", "query": "秋田県大仙市 農業振興情報センター"},
            {"time": "16:40", "location": "太田 高禮建設前", "query": "秋田県大仙市 高禮建設"},
            {"time": "17:50", "location": "中仙 中仙支所", "query": "秋田県大仙市 中仙支所"},
            {"time": "18:30", "location": "中仙 イーストモール", "query": "秋田県大仙市 イーストモール"},
            {"time": "13:50", "location": "六郷 アックスフーズマート六郷店", "query": "秋田県美郷町 アックスフーズマート六郷店"},
            {"time": "14:32", "location": "千畑 塚 トイレパーク", "query": "秋田県美郷町 塚トイレパーク"},
            {"time": "15:10", "location": "千畑 春日神社", "query": "秋田県美郷町 春日神社"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+9),
        "date": "2025-07-10",
        "day_of_week": "木",
        "candidate": "なかいずみ松司",
        "prefecture": "秋田県",
        "constituency": "秋田選挙区",
        "party": "自民党",
        "image_path": "photos/250710_秋田県_なかいずみ松司.jpg",
        "schedule": [
            {"time": "08:15", "location": "椿台 鈴木建設工業前", "query": "秋田県東成瀬村 鈴木建設工業"},
            {"time": "08:40", "location": "岩井川 ゆるるん前", "query": "秋田県東成瀬村 ゆるるん"},
            {"time": "09:20", "location": "田子内 役場前", "query": "秋田県東成瀬村 東成瀬村役場"},
            {"time": "10:40", "location": "大館公会堂", "query": "秋田県湯沢市 大館公会堂"},
            {"time": "11:10", "location": "三梨JA前", "query": "秋田県湯沢市 三梨 JA"},
            {"time": "11:40", "location": "佐藤養助商店 本社工場前", "query": "秋田県湯沢市 佐藤養助商店 本社工場"},
            {"time": "17:10", "location": "湯沢市役所", "query": "秋田県湯沢市 湯沢市役所"},
            {"time": "17:55", "location": "グランマート", "query": "秋田県湯沢市 グランマート"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+10),
        "date": "2025-07-09",
        "day_of_week": "水",
        "candidate": "なかいずみ松司",
        "prefecture": "秋田県",
        "constituency": "秋田選挙区",
        "party": "自民党",
        "image_path": "photos/250709_秋田県_なかいずみ松司.jpg",
        "schedule": [
            {"time": "09:15", "location": "船川 オガーレ前", "query": "秋田県男鹿市 オガーレ"},
            {"time": "12:40", "location": "船越 船越コミセン前", "query": "秋田県男鹿市 船越コミセン"},
            {"time": "15:40", "location": "出戸新町コミセン前", "query": "秋田県潟上市 出戸新町コミセン"},
            {"time": "16:45", "location": "ナイス追分店前", "query": "秋田県潟上市 ナイス追分店"},
            {"time": "17:30", "location": "いとく土崎みなと店", "query": "秋田県秋田市 いとく土崎みなと店"},
            {"time": "18:15", "location": "いとく自衛隊通店", "query": "秋田県秋田市 いとく自衛隊通店"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+11),
        "date": "2025-07-07",
        "day_of_week": "月",
        "candidate": "なかいずみ松司",
        "prefecture": "秋田県",
        "constituency": "秋田選挙区",
        "party": "自民党",
        "image_path": "photos/250707_秋田県_なかいずみ松司.jpg",
        "schedule": [
            {"time": "11:20", "location": "花岡町 エコシステム花岡", "query": "秋田県大館市 エコシステム花岡"},
            {"time": "11:45", "location": "御成町 いとく大館SC前", "query": "秋田県大館市 いとく大館SC"},
            {"time": "14:05", "location": "坊沢屋敷 旧JA鷹巣跡地", "query": "秋田県北秋田市 JA鷹巣"},
            {"time": "14:10", "location": "北秋田市交流センター", "query": "秋田県北秋田市 北秋田市交流センター"},
            {"time": "14:20", "location": "大町 JA秋田たかのす前", "query": "秋田県北秋田市 JA秋田たかのす"},
            {"time": "15:10", "location": "七日市 旧JA跡地", "query": "秋田県北秋田市 七日市 JA"},
            {"time": "16:40", "location": "本庁 旧JA跡地", "query": "秋田県北秋田市 北秋田市役所"},
            {"time": "17:20", "location": "前田駅前", "query": "秋田県北秋田市 前田駅"},
            {"time": "18:05", "location": "銀山 阿仁合駅前", "query": "秋田県北秋田市 阿仁合駅"},
            {"time": "18:50", "location": "比立内 菊地電気前", "query": "秋田県北秋田市 比立内 菊地電気"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+12),
        "date": "2025-07-05",
        "day_of_week": "土",
        "candidate": "なかいずみ松司",
        "prefecture": "秋田県",
        "constituency": "秋田選挙区",
        "party": "自民党",
        "image_path": "photos/250705_秋田県_なかいずみ松司.jpg",
        "schedule": [
            {"time": "09:00", "location": "比内町扇田 いとく比内店", "query": "秋田県大館市 いとく比内店"},
            {"time": "09:25", "location": "比内町独鈷 中田商店前", "query": "秋田県大館市 独鈷 中田商店"},
            {"time": "10:00", "location": "比内町大葛 旧保育所前", "query": "秋田県大館市 大葛"},
            {"time": "13:35", "location": "藤里役場前", "query": "秋田県藤里町 藤里町役場"},
            {"time": "14:45", "location": "二ツ井町荷上場 伊藤謙商店向い", "query": "秋田県能代市 伊藤謙商店"},
            {"time": "16:05", "location": "柳町 プラザ都前", "query": "秋田県能代市 プラザ都"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+13),
        "date": "2025-07-04",
        "day_of_week": "金",
        "candidate": "なかいずみ松司",
        "prefecture": "秋田県",
        "constituency": "秋田選挙区",
        "party": "自民党",
        "image_path": "photos/250704_秋田県_なかいずみ松司.jpg",
        "schedule": [
            {"time": "08:40", "location": "寺内 秋田クボタ本社前", "query": "秋田県秋田市 秋田クボタ"},
            {"time": "09:10", "location": "土崎 秋豊ネットライズ本社前", "query": "秋田県秋田市 秋豊ネットライズ"},
            {"time": "09:20", "location": "飯島 ヌノタニ前", "query": "秋田県秋田市 飯島 ヌノタニ"},
            {"time": "10:30", "location": "卸町 秋田卸センター前", "query": "秋田県秋田市 秋田卸センター"},
            {"time": "12:00", "location": "エリアなかいち", "query": "秋田県秋田市 エリアなかいち"},
            {"time": "14:15", "location": "朝市ふれあい館", "query": "秋田県五城目町 朝市ふれあい館"},
            {"time": "15:50", "location": "道の駅かみこあに", "query": "秋田県上小阿仁村 道の駅かみこあに"},
            {"time": "16:45", "location": "セントラル合川交差点", "query": "秋田県北秋田市 セントラル合川"},
            {"time": "17:30", "location": "佐々木電機前", "query": "秋田県北秋田市 佐々木電機"},
            {"time": "18:10", "location": "早口駅前", "query": "秋田県大館市 早口駅"},
            {"time": "19:45", "location": "田代公民館山田分館", "query": "秋田県大館市 田代公民館山田分館"}
        ]
    },
    {
        "id": str(int(time.time()*1000)+14),
        "date": "2025-07-03",
        "day_of_week": "木",
        "candidate": "なかいずみ松司",
        "prefecture": "秋田県",
        "constituency": "秋田選挙区",
        "party": "自民党",
        "image_path": "photos/250703_秋田県_なかいずみ松司.jpg",
        "schedule": [
            {"time": "09:50", "location": "八橋南 JA秋田中央会", "query": "秋田県秋田市 JA秋田中央会"},
            {"time": "10:30", "location": "下新城中野 まると食堂裏付近", "query": "秋田県秋田市 まると食堂"},
            {"time": "11:15", "location": "三傳商事", "query": "秋田県秋田市 三傳商事"},
            {"time": "11:35", "location": "ナイス新屋店駐車場", "query": "秋田県秋田市 ナイス新屋店"},
            {"time": "14:25", "location": "道の駅東由利", "query": "秋田県由利本荘市 道の駅東由利"},
            {"time": "15:00", "location": "道の駅うご", "query": "秋田県羽後町 道の駅うご"},
            {"time": "16:00", "location": "湯沢市役所前", "query": "秋田県湯沢市 湯沢市役所"},
            {"time": "17:00", "location": "道の駅十文字", "query": "秋田県横手市 道の駅十文字"},
            {"time": "18:00", "location": "しゅしゅえっとマルシェ", "query": "秋田県大仙市 しゅしゅえっとマルシェ"},
            {"time": "19:00", "location": "よねや角館店", "query": "秋田県仙北市 よねや角館店"}
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
