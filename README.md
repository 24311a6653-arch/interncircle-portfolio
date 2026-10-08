# Weather App with Live OpenWeather API

## Project Description

This project is a Python-based Weather App that uses the OpenWeather API to fetch real-time weather information for a city.

## Features

* Fetches real-time weather data using a REST API
* Displays city name
* Displays temperature in Celsius
* Displays humidity
* Displays current weather condition
* Uses JSON response parsing
* Handles invalid city names or API errors
* Keeps the API key secure using a `.env` file

## Technologies Used

* Python
* Requests
* OpenWeather API
* JSON
* python-dotenv

## How to Run

1. Install the required packages:

```bash
pip install requests python-dotenv
```

2. Create a `.env` file and add your OpenWeather API key:

```text
OPENWEATHER_API_KEY=YOUR_API_KEY
```

3. Run the application:

```bash
python weather_app.py
```

4. Enter a city name when prompted.

## Example

```text
Enter city name: Hyderabad

--- Weather Information ---
City: Hyderabad
Temperature: 28 °C
Humidity: 65 %
Weather: clear sky
```

## Security

The API key is stored in the `.env` file and `.env` is included in `.gitignore` so that the private API key is not uploaded to GitHub.

## Expected Outcome

This project demonstrates practical use of REST APIs, HTTP requests, JSON parsing, and real-world cloud API integration using Python.
