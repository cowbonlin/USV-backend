import paho.mqtt.client as mqtt
from requests import get

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc), flush=True)
    client.subscribe("mytopic")

def on_message(client, userdata, msg):
    payload = str(msg.payload)
    print(f"{msg.topic} {payload}", flush=True)
    response = get(f'http://web:8000/log/{msg.topic}')
    print(response, flush=True)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt", 1883, 60)
    client.loop_forever()