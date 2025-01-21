from flask import Flask

from app.routes import health_check_bp

app = Flask(__name__)
app.register_blueprint(health_check_bp)

if __name__ == '__main__':
    app.run()