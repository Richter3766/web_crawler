from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class CrawledData(Base):
    __tablename__ = 'crawled_data'

    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    contents = Column(Text)
    crawled_date = Column(DateTime, default=datetime.now())

    crawled_index_id = Column(Integer, ForeignKey('crawled_index.id', ondelete='CASCADE'))

    crawled_index = relationship('CrawledIndex', back_populates='crawled_data')