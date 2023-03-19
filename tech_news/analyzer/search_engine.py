from tech_news.database import search_news
from datetime import datetime


def normalize_news(news_list):
    return [(news['title'], news['url']) for news in news_list]


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "-i"}}
    news_list = search_news(query)
    return normalize_news(news_list)


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        formattedDate = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": {"$regex": formattedDate, "$options": "i"}}
        news_list = search_news(query)
        return normalize_news(news_list)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
