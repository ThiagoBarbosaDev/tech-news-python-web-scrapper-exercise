from parsel import Selector
import requests
import time


class News:
    def __init__(
        self, url, title, timestamp, writer, reading_time, summary, category
    ):
        self.url = url
        self.title = title
        self.timestamp = timestamp
        self.writer = writer
        self.reading_time = reading_time
        self.summary = summary
        self.category = category

    def get_news(self):
        return {
            "url": self.url,
            "title": self.title,
            "timestamp": self.timestamp,
            "writer": self.writer,
            "reading_time": self.reading_time,
            "summary": self.summary,
            "category": self.category,
        }


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        print("Timed out")


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_links = selector.css("h2.entry-title a::attr(href)").getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_link = selector.css("a.next::attr(href)").get()
    return next_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    url = selector.css("div.pk-share-buttons-wrap::attr(data-share-url)").get()
    title = selector.css("h1::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    reading_time_str = selector.css("li.meta-reading-time::text").get()
    reading_time = int(reading_time_str.split()[0])
    summary = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) ::text").getall()
    ).strip()
    category = selector.css("span.label::text").get()

    news = News(url, title, timestamp, writer, reading_time, summary, category)
    return news.get_news()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# html_content = fetch("https://blog.betrybe.com/")
# html_content = fetch(
#     "https://blog.betrybe.com/linguagem-de-programacao/o-que-e-array/"
# )

# print(scrape_updates(html_content))
# print(scrape_next_page_link(html_content))
# print(scrape_news(html_content))
