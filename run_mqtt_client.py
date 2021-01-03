import paho.mqtt.client as mqtt
from requests import post

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("mytopic")

def on_message(client, userdata, msg):
    print("NEW MSG:", msg.topic, msg.payload)
    response = post('http://web:8000/mqtt-record', 
                    {"topic": msg.topic, "payload": msg.payload})
    print("RES:", response)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt", 1883, 60)
    client.loop_forever()