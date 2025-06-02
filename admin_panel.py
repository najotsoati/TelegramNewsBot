admin_data = {
    "feeds": [
        "https://gazeta.uz/rss/",
        "https://daryo.uz/feed/",
        "https://www.bbc.com/uzbek/index.xml"
    ],
    "channel": "@yangiliklar_ai"
}

def add_feed(url):
    if url not in admin_data["feeds"]:
        admin_data["feeds"].append(url)
        return "Manba qo‘shildi."
    return "Bu manba allaqachon mavjud."

def remove_feed(url):
    if url in admin_data["feeds"]:
        admin_data["feeds"].remove(url)
        return "Manba o‘chirildi."
    return "Bu manba topilmadi."

def get_feeds():
    return admin_data["feeds"]

def set_channel(username):
    admin_data["channel"] = username
    return "Kanal o‘zgartirildi."

def get_channel():
    return admin_data["channel"]
  
