import os

from dotenv import load_dotenv

from .sqlite import *
from .db_manager import *

load_dotenv()
db_url = os.getenv('DATABASE_URL')
db_manager = DatabaseManager(db_url)