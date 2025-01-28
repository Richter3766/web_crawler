from flask import request, jsonify

from app.routes import web_crawler_bp
from app.services.web_crawler_service import add_url


@web_crawler_bp.route('/crawler', methods=['POST'])
def post_crawler_url():
    reqeust_body = request.get_json()
    result = add_url(reqeust_body['url'])
    return jsonify(result), 200