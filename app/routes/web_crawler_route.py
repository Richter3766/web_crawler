from flask import request, jsonify

from app.routes import web_crawler_bp
from app.services.web_crawler_service import add_url, get_failed_data_list


@web_crawler_bp.route('/crawler', methods=['POST'])
def post_crawler_url():
    requests_body = request.get_json()
    result = add_url(requests_body['url'])
    return jsonify(result), 200

@web_crawler_bp.route('/crawler/failed', methods=['GET'])
def get_failed_url():
    result = get_failed_data_list()
    return jsonify(result), 200