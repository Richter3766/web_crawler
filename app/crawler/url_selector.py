import queue
import random
import time

from app.database import load_queue_from_db, save_queue_to_db


class UrlSelector:
    def __init__(self, startUrl):
        self.high_queue = queue.Queue()
        self.medium_queue = queue.Queue()
        self.low_queue = queue.Queue()

        self.seed = startUrl[0]

        self.high_priority_score = 50
        self.medium_priority_score = 20
        self.low_priority_score = 0

    def calculate_weight(self):
        random.seed(self.seed)
        weight = random.randint(0, 100)
        return weight

    def append_url(self, url):
        self.seed = url
        weight = self.calculate_weight()

        if weight >= self.high_priority_score:
            self.high_queue.put(url)
        elif weight >= self.medium_priority_score:
            self.medium_queue.put(url)
        else:
            self.low_queue.put(url)

    def select_url(self, total_time_out = 3):
        start_time = time.time()
        weight = self.calculate_weight()
        while True:
            if time.time() - start_time > total_time_out:
                return None

            if weight >= self.high_priority_score and not self.high_queue.empty():
                return self.high_queue.get()
            elif weight >= self.medium_priority_score and not self.medium_queue.empty():
                return self.medium_queue.get()
            elif weight >= 0 and not self.low_queue.empty():
                return self.low_queue.get()
            else:
                time.sleep(1)
                continue

    def load_queue(self):
        self.high_queue = load_queue_from_db("high_queue")
        self.medium_queue = load_queue_from_db("medium_queue")
        self.low_queue = load_queue_from_db("low_queue")


    def save_queue(self):
        save_queue_to_db("high_queue", self.high_queue)
        save_queue_to_db("medium_queue", self.medium_queue)
        save_queue_to_db("low_queue", self.low_queue)
