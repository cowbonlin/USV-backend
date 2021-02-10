from flask import Blueprint, jsonify, request

from app import db
from database.models import MqttRecord

views_bp = Blueprint('views', __name__)


@views_bp.route('/helloworld')
def helloword():
    return 'greeting from cowbon'


@views_bp.route('/mqtt-record', methods=['POST'])
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


@views_bp.route('/mqtt-records')
def get_all_mqtt_records():
    records = MqttRecord.query \
                        .order_by(MqttRecord.created_at.desc()) \
                        .limit(100)
    r_list = [{'topic': r.topic,
               'payload': r.payload,
               'created_at': r.created_at.isoformat()} for r in records]
    return jsonify(r_list)
