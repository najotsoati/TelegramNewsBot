import feedparser

def get_feed_articles(feed_urls):
    articles = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # faqat oxirgi 3 ta yangilikni olamiz
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary
            })
    return articles
