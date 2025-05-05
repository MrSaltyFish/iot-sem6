import paho.mqtt.client as mqtt
import json
import time

# Define MQTT broker and topic
broker = "localhost"  # Change to cloud broker if needed
port = 1883
topic = "crowd/sector1/sensor123"

# Create MQTT client and connect
client = mqtt.Client()
client.connect(broker, port, 60)

# Publish sensor data periodically
while True:
    message = {
        "sector": "sector1",
        "device_id": "sensor123",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "crowd_density": 85
    }
    client.publish(topic, json.dumps(message), qos=1)
    print(f"Published: {message}")
    time.sleep(5)  # Send data every 5 seconds
