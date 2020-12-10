from flask import Blueprint, jsonify

from app import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/helloword')
def helloword():
    return 'greeting from cowbon'