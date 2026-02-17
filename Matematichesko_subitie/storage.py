
import json
import os

def save_participants(participants, filename="participants.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(participants, f, ensure_ascii=False, indent=2)
    print(f"Запазени {len(participants)} участници в {filename}")

def load_participants(filename="participants.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)