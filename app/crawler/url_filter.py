from app import db_manager
from app.database import CrawledIndex


class UrlFilter:
    def __init__(self):
        self.session = db_manager.get_session()

    def filter_urls(self, urls: list[str], prefix):
        result = []
        for url in urls:
            if not url.startswith('https://'):
                url = prefix + url

            isExist = self.session.query(CrawledIndex).filter(CrawledIndex.url == url).first()
            if isExist is None:
                result.append(url)

        return result
