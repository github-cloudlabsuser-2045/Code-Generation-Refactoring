import requests

API_KEY = "aaa44bd79d77f64918b0de47123ba5d9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city.

    Returns:
        dict: Weather data if successful, or an error message.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use metric units for temperature in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        # Extract relevant weather information
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    print("Welcome to the Weather App!")
    city = input("Enter the name of the city: ")

    weather_data = get_weather(city)

    if "error" in weather_data:
        print(f"Error fetching weather data: {weather_data['error']}")
    else:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description'].capitalize()}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

if __name__ == "__main__":
    main()