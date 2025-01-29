import os

from flask import Flask

from .database import *
from .routes import *
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DATABASE_URL')
db_manager = DatabaseManager(db_url)

def create_app():
    app = Flask(__name__)

    register_blueprint(app)
    create_db_file()

    return app


def register_blueprint(app):
    app.register_blueprint(health_check_bp)
    app.register_blueprint(web_crawler_bp)


def create_db_file():
    db_manager.create_tables()
    create_url_table()
    create_queue_table()
