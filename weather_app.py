import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    print("\n--- Weather Information ---")
    print("City:", city)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])

else:
    print("\nUnable to fetch weather data.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)