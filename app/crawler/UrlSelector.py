from collections import deque
import random
import threading

class UrlSelector:
    def __init__(self, startUrl):
        self.high_queue = deque(startUrl)
        self.medium_queue = deque()
        self.low_queue = deque()

        self.seed = startUrl

        self.high_priority_score = 50
        self.medium_priority_score = 20
        self.low_priority_score = 0

        self.condition = threading.Condition()

    def calculate_weight(self):
        random.seed(self.seed)
        weight = random.randint(0, 100)
        return weight


    def append_url(self, url):
        self.seed = url
        weight = self.calculate_weight()
        with self.condition:
            if weight >= self.high_priority_score: self.high_queue.append(url)
            elif weight >= self.medium_priority_score: self.medium_queue.append(url)
            else: self.low_queue.append(url)
            self.condition.notify()


    def select_url(self):
        weight = self.calculate_weight()
        with self.condition:
            while True:
                if weight >= self.high_priority_score and self.high_queue:
                    return self.high_queue.popleft()
                elif weight >= self.medium_priority_score and self.medium_queue:
                    return self.medium_queue.popleft()
                elif weight >= 0 and self.low_queue:
                    return self.low_queue.popleft()
                else:
                    self.condition.wait()
