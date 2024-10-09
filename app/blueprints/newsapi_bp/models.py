from dataclasses import dataclass
from datetime import datetime


@dataclass
class NewsApiArticle:
    source: str
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: datetime
    content: str

    def __post_init__(self):
        self.publishedAt = datetime.strptime(self.publishedAt, "%Y-%m-%dT%H:%M:%SZ")
        self.source = self.source.get("id")
