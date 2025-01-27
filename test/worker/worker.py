import threading

from app.crawler.crawler import github_blog_crawler
from app.crawler.data_processor import DataProcessor
from app.crawler.url_filter import UrlFilter
from app.crawler.url_selector import url_selector
from app.workers import create_threads

from app.workers.crawler_worker import crawling_worker
from app.workers.db_worker import db_worker
from app.workers.url_distribution_worker import url_distribution_worker

num_threads = 3
data_processor = DataProcessor()
url_filter = UrlFilter()
url_thread = threading.Thread(target=url_distribution_worker, args=(url_selector,))

crawling_threads = create_threads(crawling_worker, num_threads, (github_blog_crawler, data_processor))
db_threads = create_threads(db_worker, num_threads, (data_processor, url_filter))

print("스레드 시작")
url_selector.append_url("https://richter3766.github.io/")
url_thread.start()
