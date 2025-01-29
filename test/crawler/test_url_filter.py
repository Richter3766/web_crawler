from urllib.parse import urlparse

import pytest

from app.crawler.url_filter import UrlFilter
from app.crawler.url_selector import UrlSelector
from app.database.sqlite import clear_data_table


@pytest.fixture
def url_filter():
    return UrlFilter("test.db")

@pytest.fixture()
def url_selector():
    return UrlSelector(["1234"])

def test_filter_urls(url_filter, url_selector):
    clear_data_table("url_table", "test.db")
    urls = [
        'https://example.com',
        'https://example.com',
        'https://example.com/123',
        '/555',
    ]
    expected = [
        'https://example.com',
        'https://example.com/123',
        'https://example.com/555',
    ]

    parsed_url = urlparse(urls[0])
    prefix = f"{parsed_url.scheme}://{parsed_url.netloc}"

    result = url_filter.filter_urls(urls, prefix)
    assert result == expected