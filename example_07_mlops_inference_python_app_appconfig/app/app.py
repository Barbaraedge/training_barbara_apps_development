import time
import json
import requests

DATA_ATTR = "Flw"

URL_MODEL_SERVING = "http://127.0.0.1:9084/v1/models/model:predict"

# Main thread will check the appconfig and print messages
while True:
    try:
        # Read data from appconfig
        f = open("/appconfig/appconfig.json")
        app_config_data = json.load(f)

        value = app_config_data["data"][DATA_ATTR]
        print(f"Value: {value}")

        # Make inference
        inference_data = {"instances": [value]}
        inference_json = json.dumps(inference_data)

        # POST model serving
        prediction = requests.post(URL_MODEL_SERVING, data=inference_json)

        if prediction.status_code == 200:
            p_data = prediction.json()
            print(f"Prediction: {p_data}")
        else:
            print("Error al llamar a la API. Código de estado:", prediction.status_code)
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)  # Sleep for 1 second