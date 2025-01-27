from urllib.parse import urlparse

import pytest

from app.crawler.url_filter import UrlFilter
from app.crawler.url_selector import UrlSelector


@pytest.fixture
def url_filter():
    return UrlFilter()

@pytest.fixture()
def url_selector():
    return UrlSelector(["1234"])

def test_filter_urls(url_filter, url_selector):
    urls = [
        'https://example.com',
        'https://OTHER.com',
        'https://example.com/123',
        'https://example.com/444',
        '/555',

    ]
    parsed_url = urlparse(urls[0])
    prefix = f"{parsed_url.scheme}://{parsed_url.netloc}"

    result = url_filter.filter_urls(urls, prefix)
    print(result)