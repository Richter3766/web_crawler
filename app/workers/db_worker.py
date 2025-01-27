import threading

from urllib.parse import urlparse

from app import db_manager
from app.crawler.data_processor import DataProcessor
from app.crawler.url_filter import UrlFilter
from app.crawler.url_selector import url_selector

from app.database import CrawledIndex
from app.dto.crawled_dto import CrawledDto


def process_urls(crawled_dto, url_filter):
    parsed_url = urlparse(crawled_dto.url)
    prefix = f"{parsed_url.scheme}://{parsed_url.netloc}"
    urls = url_filter.filter_urls(crawled_dto.urls, prefix)
    for url in urls:
        url_selector.append_url(url)


def db_worker(data_processor: DataProcessor, url_filter: UrlFilter):
    session = db_manager.get_session()
    while True:
        crawled_dto: CrawledDto = data_processor.get_non_duplicate_data(session)

        if crawled_dto is not None:
            # TODO: 로직이 마음에 안 드므로 개선 필요
            try:
                print("크롤링 데이터 저장 시작: ", crawled_dto.url)
                crawled_index: CrawledIndex = crawled_dto.to_index()
                data_processor.add_data(session, crawled_index)
                data_processor.commit(session)

                crawled_data = crawled_dto.to_data(crawled_index.id)
                crawled_index.crawled_data.append(crawled_data)

                data_processor.add_data(session, crawled_data)
                data_processor.commit(session)

            except Exception as e:
                print("에러 ", e)
                data_processor.rollback(session)
                continue

            print("크롤링 데이터 저장 종료: ", crawled_dto.url)
            filter_worker = threading.Thread(target=process_urls, args=(crawled_dto, url_filter))
            filter_worker.start()
    session.close()