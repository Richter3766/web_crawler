import queue
import random
import time


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

    def select_url(self):
        weight = self.calculate_weight()
        while True:
            if weight >= self.high_priority_score and not self.high_queue.empty():
                return self.high_queue.get()
            elif weight >= self.medium_priority_score and not self.medium_queue.empty():
                return self.medium_queue.get()
            elif weight >= 0 and not self.low_queue.empty():
                return self.low_queue.get()
            else:
                time.sleep(1)
                continue