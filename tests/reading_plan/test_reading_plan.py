from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from tests.assets.news import NEWS
from unittest.mock import patch


def test_reading_plan_group_news():
    EXPECTED_RETURN = {
        "readable": [
            {
                "unfilled_time": 1,
                "chosen_news": [("noticia_0", 2), ("Notícia bacana", 4)],
            },
            {
                "unfilled_time": 2,
                "chosen_news": [
                    ("Notícia bacana 2", 1),
                    ("noticia_3", 1),
                    ("noticia_4", 1),
                    ("noticia_5", 1),
                    ("noticia_6", 1),
                ],
            },
            {"unfilled_time": 0, "chosen_news": [("noticia_7", 7)]},
            {"unfilled_time": 2, "chosen_news": [("noticia_9", 5)]},
        ],
        "unreadable": [("noticia_8", 8)],
    }
    with patch("tech_news.analyzer.reading_plan.find_news", return_value=NEWS):
        mocked_return = ReadingPlanService.group_news_for_available_time(7)
        assert (
            mocked_return == EXPECTED_RETURN
        )
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
