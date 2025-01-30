import os
from urllib.parse import urlparse

from app.crawler import github_blog_crawler, url_selector
from app.workers import worker_manager

def url_distribution_worker():
    while worker_manager.working:
        url = url_selector.select_url()
        if url is None:
            continue
        print("url 선택: ", url)
        prefix = urlparse(url).netloc
        if prefix == os.getenv('HYEONSOO_BLOG_URL'):
            github_blog_crawler.add_url(url)
