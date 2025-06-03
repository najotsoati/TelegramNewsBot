import feedparser

def get_feed_articles(feed_urls):
    articles = []
    for url in feed_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:3]:  # faqat oxirgi 3 ta yangilik
                articles.append({
                    "title": entry.get("title", "Sarlavha yo'q"),
                    "link": entry.get("link", "Havola mavjud emas"),
                    "summary": entry.get("summary", "Mazmun yo'q")
                })
        except Exception as e:
            print(f"Xatolik RSS o'qishda: {url} | Xatolik: {e}")
            continue
    return articles
