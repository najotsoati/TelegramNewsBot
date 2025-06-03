import json
import os

DATA_FILE = "admin_data.json"

# Fayldan ma'lumot yuklash
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "feeds": [
                "https://gazeta.uz/rss/",
                "https://daryo.uz/feed/",
                "https://www.bbc.com/uzbek/index.xml"
            ],
            "channel": "@yangiliklar_ai"
        }

# Ma'lumotni faylga yozish
def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(admin_data, f, ensure_ascii=False, indent=4)

# Global o'zgaruvchi
admin_data = load_data()

# Feed qo‘shish
def add_feed(url):
    if url not in admin_data["feeds"]:
        admin_data["feeds"].append(url)
        save_data()
        return "✅ Manba qo‘shildi."
    return "ℹ️ Bu manba allaqachon mavjud."

# Feed o‘chirish
def remove_feed(url):
    if url in admin_data["feeds"]:
        admin_data["feeds"].remove(url)
        save_data()
        return "🗑️ Manba o‘chirildi."
    return "⚠️ Bu manba topilmadi."

# Barcha feedlar
def get_feeds():
    return admin_data["feeds"]

# Kanal o‘zgartirish
def set_channel(username):
    admin_data["channel"] = username
    save_data()
    return f"📢 Kanal o‘zgartirildi: {username}"

# Kanalni olish
def get_channel():
    return admin_data["channel"]
    
