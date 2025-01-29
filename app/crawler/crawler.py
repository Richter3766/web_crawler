import queue
import requests

from app import user_agent
from app.crawler import ContentParser


class Crawler:
    def __init__(self, parser: ContentParser):
        self.queue = queue.Queue()
        self.parser = parser

    def request_html(self):
        url = self.queue.get()

        headers = {
            'User-Agent': user_agent
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def add_url(self, url):
        self.queue.put(url)