from flask import Blueprint, jsonify, current_app as app

from app import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/helloworld')
def helloword():
    return 'greeting from cowbon'

@api_bp.route('/log/<bp>')
def log_bp(bp):
    print("LOG:", bp)
    app.logger.info('loglog')
