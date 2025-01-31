import json
import queue

from app.database import load_queue_from_db, save_queue_to_db


class FailedUrlCollector:
    def __init__(self):
        self.queue = queue.Queue()

    def save_queue(self):
        save_queue_to_db("failed_queue", self.queue)

    def load_queue(self):
        self.queue = load_queue_from_db("failed_queue")

    def append_url(self, url: str, e: Exception):
        data = {"url": url, "e": str(e)}
        json_data = json.dumps(data)
        self.queue.put(json_data)

    def get_url(self):
        try:
            data = self.queue.get(timeout=3)
        except queue.Empty:
            return None

        parsed_data = json.loads(data)
        return parsed_data.get("url")  # URL 반환

    def get_data(self):
        return [json.loads(item) for item in list(self.queue.queue)]
