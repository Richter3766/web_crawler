from .failed_url_collector import *
from .url_selector import *
from .url_filter import *

from .data_processor import *

url_selector = UrlSelector(["start URL"])
failed_url_collector = FailedUrlCollector()
url_filter = UrlFilter()
data_processor = DataProcessor()

from .crawler import *
from .parsers import GithubBlogParser
github_blog_crawler = Crawler(GithubBlogParser())