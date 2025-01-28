from flask import Blueprint

health_check_bp = Blueprint('health_check', __name__)
web_crawler_bp = Blueprint('web_crawler', __name__)

from .health_check_route import *
from .web_crawler_route import *