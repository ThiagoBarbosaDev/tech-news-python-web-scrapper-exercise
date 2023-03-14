from parsel import Selector
import requests
import time


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
    news_links = selector.css('h2.entry-title a::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_link = selector.css('a.next::attr(href)').get()
    return next_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


html_content = fetch("https://blog.betrybe.com/")

# print(scrape_updates(html_content))
print(scrape_next_page_link(html_content))
