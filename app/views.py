from datetime import datetime
from flask import Blueprint, jsonify, current_app as app, request

from app import db
from app.models import Mission, MqttRecord

api_bp = Blueprint('api', __name__)

@api_bp.route('/helloworld')
def helloword():
    return 'greeting from cowbon'


@api_bp.route('/log/<bp>')
def log_bp(bp):
    print("LOG:", bp)
    app.logger.info('loglog')
    return 'hi'


@api_bp.route('/mqtt-record', methods=['POST'])
def add_mqtt_record():
    try:
        topic = request.values['topic']
        payload = request.values['payload']
    except Exception as e:
        print(e)
        raise
    mqtt_record = MqttRecord(topic=topic, payload=payload)
    db.session.add(mqtt_record)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        raise
    return jsonify(result=0, id=mqtt_record.id)


@api_bp.route('/mqtt-records')
def get_all_mqtt_records():
    records = MqttRecord.query.order_by(MqttRecord.created_at.desc()).limit(100)
    r_list = [{'topic': r.topic,
               'payload': r.payload,
               'created_at': r.created_at.isoformat()} for r in records]
    return jsonify(r_list)