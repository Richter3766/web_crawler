import sys

from dotenv import load_dotenv
from flask import Flask

from .crawler import *
from .database import *
from .routes import *
from .workers import *

load_dotenv()

def create_app():
    app = Flask(__name__)

    create_db_file()
    register_blueprint(app)
    load_status()
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
    worker_manager.create_threads(db_worker, num_threads, (), "db")
    worker_manager.create_threads(url_distribution_worker, num_threads, (), "url 분배")
    worker_manager.create_threads(crawling_worker, num_threads, (github_blog_crawler,), "크롤링")


def load_status():
    failed_url_collector.load_queue()
    url_selector.load_queue()
    data_processor.load_queue()
    github_blog_crawler.load_queue()



def signal_handler(sig, frame):
    print("======================= 앱 종료 시작 =======================")
    worker_manager.wait_threads()
    save_status()
    print("======================= 앱 종료 완료 =======================")
    sys.exit(0)


def save_status():
    print("-------------------- 상태 저장 시작 --------------------")
    url_selector.save_queue()
    data_processor.save_queue()
    github_blog_crawler.save_queue()
    failed_url_collector.save_queue()
    print("-------------------- 상태 저장 완료 --------------------")