import requests
import json
import time
from kafka import KafkaProducer

KAFKA_BROKER = "kafka:29092"
KAFKA_TOPIC = "weather_data"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Producer started...")

while True:
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 52.52, "longitude": 13.41, "current_weather": "true"}
        )
        data = response.json()["current_weather"]
        
        producer.send(KAFKA_TOPIC, data)
        print(f"Sent: {data}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(30)
