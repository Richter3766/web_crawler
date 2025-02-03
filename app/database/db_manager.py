import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.model.base import Base

load_dotenv()
db_url = os.getenv('DATABASE_URL')

class DatabaseManager:
    def __init__(self):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()