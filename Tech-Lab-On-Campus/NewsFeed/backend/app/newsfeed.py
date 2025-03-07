"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
from app.utils.redis import REDIS_CLIENT

@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str

def format_article(article: dict) -> Article:
    """Format raw data into an Article object."""
    return Article(
        author=article.get("author", "Unknown"),
        title=article["thread"].get("title", "No Title"),
        body=article.get("text", "No Content"),
        publish_date=datetime.fromisoformat(article["thread"].get("published", "1970-01-01T00:00:00.000+00:00")),
        image_url=article["thread"].get("main_image", ""),
        url=article.get("url", ""),
    )

def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    raw_articles = REDIS_CLIENT.get_entry("all_articles")
    # 2. Format the data into articles
    if raw_articles:
        return [format_article(article) for article in raw_articles]
    # 3. Return a list of the articles formatted 
    return []


def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    articles = get_all_news()
    # 2. Return as a list of articles sorted by most recent date
    if articles:
        return sorted(articles, key=lambda article: article.publish_date, reverse=True)
    return None
