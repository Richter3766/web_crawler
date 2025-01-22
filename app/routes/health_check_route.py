from flask import jsonify
from . import health_check_bp
from ..services.health_check_service import health_service


@health_check_bp.route('/health', methods=['GET'])
def get_health_check():
    return jsonify(health_service.health_check()), 200