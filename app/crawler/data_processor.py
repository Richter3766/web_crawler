import queue

from sqlalchemy.orm import Session

from app.database import CrawledIndex
from app.dto.crawled_dto import CrawledDto


class DataProcessor:
    def __init__(self):
        self.queue: queue.Queue[CrawledDto] = queue.Queue()

    def append_dto(self, dto: CrawledDto):
        self.queue.put(dto)

    def get_non_duplicate_data(self, session: Session):
        data: CrawledDto = self.queue.get()
        result = session.query(CrawledIndex).filter(CrawledIndex.hash_value == data.hash_value).first()
        if result is None:
            return data
        return None