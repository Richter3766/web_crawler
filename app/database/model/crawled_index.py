from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.orm import relationship

from app.database.model.base import Base


class CrawledIndex(Base):
    __tablename__ = 'crawled_index'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hash_value = Column(CHAR(64), index=True)
    url = Column(String(2048), index=True)

    crawled_data = relationship('CrawledData', back_populates='crawled_index')
