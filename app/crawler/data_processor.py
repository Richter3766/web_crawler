import queue

from app import db_manager
from app.database import CrawledIndex
from app.dto.crawled_dto import CrawledDto


class DataProcessor:
    def __init__(self):
        self.queue: queue.Queue[CrawledDto] = queue.Queue()
        self.session = db_manager.get_session()

    def append_dto(self, dto: CrawledDto):
        self.queue.put(dto)

    def get_non_duplicate_data(self):
        data: CrawledDto = self.queue.get()
        result = self.session.query(CrawledIndex).filter(CrawledIndex.hash_value == data.hash_value).first()
        if result is None:
            return data
        return None

    def add_data(self, data):
        if isinstance(data, list):
            self.session.add_all(data)
        else:
            self.session.add(data)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def delete_data(self, data_id):
        self.session.delete(data_id)