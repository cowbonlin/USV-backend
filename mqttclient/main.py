from contextlib import contextmanager

import paho.mqtt.client as mqtt

from database.sa import SessionFactory
from mqttclient import handlers


TOPIC_HANDLER_MAP = {
    'VehState': handlers.create_veh_state,
    'VehStatsAnchor': handlers.create_vehstats_anchor,
    'RVehStateEncounter': handlers.create_rvse,
    'mytopic': handlers.handle_mytopic
}


@contextmanager
def get_session():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()


def on_message(client, userdata, msg):
    print("NEW:", msg.topic, msg.payload)
    with get_session() as session:
        TOPIC_HANDLER_MAP[msg.topic](session, msg.payload)


def on_connect(client, userdata, flags, rc):
    print("[Connected] "+str(rc))
    for topic, _ in TOPIC_HANDLER_MAP.items():
        client.subscribe(topic, qos=1)
    client.subscribe("mytopic")


def run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt", 1883, 60)
    client.loop_forever()
