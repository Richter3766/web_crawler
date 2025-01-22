import os

from flask import Flask
from dotenv import load_dotenv

from app.routes import health_check_bp

load_dotenv()
app = Flask(__name__)
app.register_blueprint(health_check_bp)
user_agent = os.getenv('USER_AGENT', 'default_user_agent')

if __name__ == '__main__':
    app.run()