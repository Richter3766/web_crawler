from app.database import CrawledIndex
from app.database.model.crawled_data import CrawledData


class CrawledDto:
    def __init__(self, title, contents, urls, hash_value):
        self.url = None
        self.title = title
        self.contents = contents
        self.urls = urls
        self.hash_value = hash_value

    def set_url(self, url):
        self.url = url

    def to_dict(self):
        return {
            'title': self.title,
            "contents": self.contents,
            "urls": self.urls,
            "hash_value": self.hash_value
        }

    def to_data(self, index_id):
        return CrawledData(
            title=self.title,
            contents=self.contents,
            crawled_index_id=index_id
        )

    def to_index(self):
        return CrawledIndex(
            url=self.url,
            hash_value = self.hash_value
        )