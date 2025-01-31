from app import failed_url_collector
from app.crawler import url_selector


def add_url(url: str):
    url_selector.append_url(url)
    return {"message": "successfully add " + url}

def get_failed_data_list():
    failed_data = failed_url_collector.get_data()

    return failed_data
