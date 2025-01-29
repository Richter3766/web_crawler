from dotenv import load_dotenv
from flask import Flask

from .database import *
from .routes import *
from .workers import *

load_dotenv()

def create_app():
    app = Flask(__name__)

    register_blueprint(app)
    create_db_file()
    run_workers(3)

    return app


def register_blueprint(app):
    app.register_blueprint(health_check_bp)
    app.register_blueprint(web_crawler_bp)


def create_db_file():
    db_manager.create_tables()
    create_url_table()
    create_queue_table()


def run_workers(num_threads):
    url_thread = create_threads(url_distribution_worker, num_threads, ())
    crawling_threads = create_threads(crawling_worker, num_threads, (github_blog_crawler,))
    db_threads = create_threads(db_worker, num_threads, ())