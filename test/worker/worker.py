from app.database import *
from app.workers import *

num_threads = 3

create_url_table()
create_queue_table()

data_processor = DataProcessor()
url_filter = UrlFilter()
url_selector = UrlSelector(["12345"])
github_blog_crawler = Crawler(GithubBlogParser())

url_thread = create_threads(url_distribution_worker, num_threads, (url_selector,))
crawling_threads = create_threads(crawling_worker, num_threads, (github_blog_crawler, data_processor))
db_threads = create_threads(db_worker, num_threads, (data_processor, url_filter))

print("스레드 시작")
url_selector.append_url("https://richter3766.github.io/")
url_thread.start()
