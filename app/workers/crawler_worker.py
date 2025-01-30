import time

from app.crawler import Crawler, data_processor
from app.dto import CrawledDto
from app.workers import worker_manager


def crawling_worker(crawler: Crawler):
    while worker_manager.working:
        data = crawler.request_html()
        if data is not None:
            crawled_dto: CrawledDto = crawler.parser.parse(data)
            if crawled_dto is None:
                continue
            crawled_dto.set_url(data.url)
            data_processor.append_dto(crawled_dto)

        time.sleep(2)

