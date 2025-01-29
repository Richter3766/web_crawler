import os

from .sqlite import *
from .db_manager import *

db_url = os.getenv('DATABASE_URL')
db_manager = DatabaseManager(db_url)