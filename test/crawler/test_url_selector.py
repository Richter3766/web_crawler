import pytest

from app.crawler.url_selector import UrlSelector

@pytest.fixture
def url_selector():
    return UrlSelector("")


@pytest.mark.parametrize("weight", [60, 25, 5])
def test_append_url(mocker, url_selector, weight):
    mocker.patch.object(url_selector, 'calculate_weight', return_value=weight)
    test_url = 'https://example.com'
    url_selector.append_url(test_url)

    if weight == url_selector.high_priority_score:
        assert test_url in url_selector.high_queue
    elif weight == url_selector.medium_priority_score:
        assert test_url in url_selector.medium_queue
    elif weight == url_selector.low_priority_score:
        assert test_url in url_selector.low_queue


@pytest.mark.parametrize("weight", [60, 25, 5])
def test_select_url(mocker, url_selector, weight):
    mocker.patch.object(url_selector, 'calculate_weight', return_value=weight)
    high_url, medium_url, low_url = "high_url", "medium_url", "low_url"
    url_selector.high_queue.put(high_url)
    url_selector.medium_queue.put(medium_url)
    url_selector.low_queue.put(low_url)

    selected_url = url_selector.select_url()

    if weight >= url_selector.high_priority_score:
        assert selected_url == high_url
    elif weight >= url_selector.medium_priority_score:
        assert selected_url == medium_url
    elif weight >= url_selector.low_priority_score:
        assert  selected_url == low_url

