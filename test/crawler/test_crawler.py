import pytest
import requests

from app.crawler import Crawler, GithubBlogParser

@pytest.fixture
def crawler():
    return Crawler(GithubBlogParser())

test_url = 'https://richter3766.github.io/'

def test_request_html(crawler):
    crawler.add_url(test_url)
    data = crawler.request_html()

    assert data is not None


def test_request_html_exception(mocker, crawler):
    mocker.patch('requests.get', side_effect=requests.exceptions.RequestException)
    crawler.add_url(test_url)

    data = crawler.request_html()
    assert data is None

