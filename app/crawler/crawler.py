import os
import queue

import requests

from app.database import save_queue_to_db, load_queue_from_db
from app.crawler.parsers import ContentParser

user_agent = os.getenv('USER_AGENT')

class Crawler:
    def __init__(self, parser: ContentParser):
        self.parser = parser
        self.queue = queue.Queue()

    def request_html(self):
        try:
            url = self.queue.get(timeout=3)
        except queue.Empty:
            return None

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

    def load_queue(self):
        self.queue = load_queue_from_db(type(self.parser).__name__)

    def save_queue(self):
        save_queue_to_db(type(self.parser).__name__, self.queue)