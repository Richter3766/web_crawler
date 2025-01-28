from app.crawler.url_selector import url_selector


def add_url(url: str):
    url_selector.append_url(url)
    return {"message": "successfully add " + url}
