import threading

from urllib.parse import urlparse

from app import db_manager
from app.crawler import *
from app.database.model import CrawledIndex
from app.dto import CrawledDto


def process_urls(crawled_dto):
    parsed_url = urlparse(crawled_dto.url)
    prefix = f"{parsed_url.scheme}://{parsed_url.netloc}"
    urls = url_filter.filter_urls(crawled_dto.urls, prefix)
    for url in urls:
        url_selector.append_url(url)


def db_worker():
    session = db_manager.get_session()
    while True:
        crawled_dto: CrawledDto = data_processor.get_non_duplicate_data(session)

        if crawled_dto is not None:
            print("크롤링 데이터 저장 시작: ", crawled_dto.url)
            crawled_index: CrawledIndex = crawled_dto.to_index()
            try:
                session.add(crawled_index)
                session.commit()

                crawled_data = crawled_dto.to_data(crawled_index.id)
                crawled_index.crawled_data.append(crawled_data)

                session.add(crawled_data)
                session.commit()
            except Exception as e:
                print("에러 ", e)
                session.rollback()
                session.delete(crawled_index)
                session.commit()
                continue

            print("크롤링 데이터 저장 종료: ", crawled_dto.url)
            filter_worker = threading.Thread(target=process_urls, args=(crawled_dto, ))
            filter_worker.start()
    session.close()