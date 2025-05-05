import paho.mqtt.client as mqtt

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} from {message.topic}")

# Define MQTT broker and topic
broker = "localhost"
port = 1883
topic = "crowd/sector1/#"  # Subscribe to all devices in Sector 1

# Create MQTT client and connect
client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port, 60)
client.subscribe(topic, qos=1)

# Listen for incoming messages
client.loop_forever()
