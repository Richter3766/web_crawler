import os

from flask import Flask

from .database.db_manager import DatabaseManager
from .routes import health_check_bp, web_crawler_bp
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DATABASE_URL')
db_manager = DatabaseManager(db_url)

user_agent = os.getenv('USER_AGENT')

def create_app():
    app = Flask(__name__)

    app.register_blueprint(health_check_bp)
    app.register_blueprint(web_crawler_bp)
    db_manager.create_tables()

    return app

