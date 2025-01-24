import os

import pytest

from app.database.db_manager import DatabaseManager
from app.database.model.crawled_data import CrawledData


@pytest.fixture
def database_manager():
    return DatabaseManager(os.getenv('DATABASE_URL'))

def test_database(database_manager: DatabaseManager):
    database_manager.create_tables()
    session = database_manager.get_session()

    result = session.query(CrawledData).all()
    print(result)