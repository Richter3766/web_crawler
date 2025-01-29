from .parsers import GithubBlogParser
from .url_selector import *
from .url_filter import *
from .crawler import *
from .data_processor import *

url_selector = UrlSelector(["start URL"])
url_filter = UrlFilter()
github_blog_crawler = Crawler(GithubBlogParser())
data_processor = DataProcessor()