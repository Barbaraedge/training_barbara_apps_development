import paho.mqtt.client as mqtt
import queue
import threading
import time
import json
import requests

MQTT_URL = "127.0.0.1"
MQTT_USERNAME = "bbruser"
MQTT_PASSWORD = "bbrpassword"
MQTT_SUB_TOPIC = "api/v1/reads/#"
MQTT_PUB_TOPIC = "api/v1/model/predict"

DATA_ATTR = "Flw"

URL_MODEL_SERVING = "http://127.0.0.1:9084/v1/models/model:predict"

messages = queue.Queue()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_SUB_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    messages.put(msg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_URL, 8883, 60)

# Start a new thread that will handle the MQTT client
mqtt_thread = threading.Thread(target=client.loop_start)
mqtt_thread.start()

# Main thread will check the queue and print messages
while True:
    if not messages.empty():
        message = messages.get()
        topic = message.topic
        data = message.payload.decode()
        print(f"Message from {topic}: {data}")

        data_json = json.loads(data)
        value = data_json["data"][DATA_ATTR]
        print(f"Value: {value}")

        # Make inference
        inference_data = {"instances": [value]}
        inference_json = json.dumps(inference_data)

        # POST model serving
        prediction = requests.post(URL_MODEL_SERVING, data=inference_json)

        if prediction.status_code == 200:
            p_data = prediction.json()
            print(f"Prediction: {p_data}")
            client.publish(MQTT_PUB_TOPIC, json.dumps(p_data))
        else:
            print("Error al llamar a la API. Código de estado:", prediction.status_code)

    time.sleep(1)  # Sleep for 1 second