
import os
import json
import unicodedata

def normalize(text):
    return unicodedata.normalize('NFC', text)

def get_registered_files(db_path):
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    paths = set()
    for entry in data:
        if 'image_path' in entry:
            paths.add(normalize(os.path.basename(entry['image_path'])))
    return paths

def get_all_files(photos_dir):
    files = set()
    for f in os.listdir(photos_dir):
        if os.path.isfile(os.path.join(photos_dir, f)) and not f.startswith('.'):
            files.add(normalize(f))
    return files

photos_dir = 'photos'
db_path = 'data/database.json'

reg_files = get_registered_files(db_path)
all_files = get_all_files(photos_dir)

unregistered = all_files - reg_files

print(f"Total files in photos: {len(all_files)}")
print(f"Registered files: {len(reg_files)}")
print(f"Unregistered files: {len(unregistered)}")
print("\nUnregistered files list:")
for f in sorted(list(unregistered)):
    print(f)
