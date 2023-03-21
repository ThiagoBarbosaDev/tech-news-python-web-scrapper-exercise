from tech_news.database import get_collection
from collections import Counter


# Requisito 10
def top_5_categories():
    """Seu código deve vir aqui"""
    db = list(get_collection().find({}, {"category": True, "_id": False}))
    category_counter = Counter(item["category"] for item in db)
    most_common_list = category_counter.most_common(5)
    sorted_most_common_list = sorted(
        most_common_list, key=lambda x: (-x[1], x[0])
    )
    return [category[0] for category in sorted_most_common_list]
