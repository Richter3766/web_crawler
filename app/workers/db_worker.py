from concurrent.futures import ThreadPoolExecutor

from urllib.parse import urlparse

from app.database import db_manager
from app.crawler import *
from app.database.model import CrawledIndex
from app.dto import CrawledDto
from app.workers import worker_manager


def process_urls(crawled_dto):
    parsed_url = urlparse(crawled_dto.url)
    prefix = f"{parsed_url.scheme}://{parsed_url.netloc}"
    urls = url_filter.filter_urls(crawled_dto.urls, prefix)
    for url in urls:
        url_selector.append_url(url)

def db_worker():
    session = db_manager.get_session()
    while worker_manager.working:
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
            worker_manager.create_threads(process_urls, 1, (crawled_dto, ))

    session.close()