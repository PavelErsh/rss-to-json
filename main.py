import feedparser
import json
import ssl


def fetch_and_convert_rss_to_json(url):
    # Отключение проверки SSL
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    # Получаем RSS-ленту
    feed = feedparser.parse(url)

    # Проверка на наличие ошибок при парсинге
    if feed.bozo:
        print(f"Ошибка при получении RSS: {feed.bozo_exception}")
        return

    # Преобразуем данные в словарь Python
    rss_data = {
        "title": feed.feed.title if hasattr(feed.feed, 'title') else None,
        "link": feed.feed.link if hasattr(feed.feed, 'link') else None,
        "description": feed.feed.description if hasattr(feed.feed, 'description') else None,
        "entries": []
    }

    # Добавляем записи из RSS-ленты
    for entry in feed.entries:
        rss_data["entries"].append({
            "title": entry.title if hasattr(entry, 'title') else None,
            "link": entry.link if hasattr(entry, 'link') else None,
            "summary": entry.summary if hasattr(entry, 'summary') else None,
            "published": entry.published if hasattr(entry, 'published') else None
        })

    # Преобразуем данные в JSON
    json_data = json.dumps(rss_data, indent=4, ensure_ascii=False)

    # Выводим JSON в терминал
    print(json_data)


# Ссылка на RSS-ленту
rss_url = "https://feeds.content.dowjones.io/public/rss/RSSPersonalFinance"

# Вызываем функцию
fetch_and_convert_rss_to_json(rss_url)