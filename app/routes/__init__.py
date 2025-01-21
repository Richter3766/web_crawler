from flask import Blueprint

health_check_bp = Blueprint('health_check', __name__)

from .health_check_route import *