import requests
import time

API_URL = "https://api.open-meteo.com/v1/forecast"
LATITUDE = 52.52
LONGITUDE = 13.41

def fetch_weather():
    response = requests.get(
        API_URL,
        params={
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "current_weather": "true"
        },
        timeout=10
    )
    response.raise_for_status()
    return response.json()["current_weather"]

if __name__ == "__main__":
    print("Weather API test started...")
    while True:
        try:
            weather = fetch_weather()
            print("Current weather:", weather)
        except Exception as e:
            print("Error:", e)
        time.sleep(30)
