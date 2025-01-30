import queue

from sqlalchemy.orm import Session

from app.database import save_queue_to_db, load_queue_from_db
from app.database.model import CrawledIndex
from app.dto import CrawledDto


class DataProcessor:
    def __init__(self):
        self.queue: queue.Queue[CrawledDto] = queue.Queue()

    def append_dto(self, dto: CrawledDto):
        self.queue.put(dto)

    def get_non_duplicate_data(self, session: Session):
        try:
            data: CrawledDto = self.queue.get(timeout=3)
        except queue.Empty:
            return None

        result = session.query(CrawledIndex).filter(CrawledIndex.hash_value == data.hash_value).first()
        if result is None:
            return data
        return None

    def load_queue(self):
        self.queue = load_queue_from_db("data_processor")

    def save_queue(self):
        save_queue_to_db("data_processor", self.queue)