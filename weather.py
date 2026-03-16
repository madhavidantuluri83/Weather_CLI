import argparse
import requests
import sys

API_KEY = "6342ce3d198ce190689132ce69f2e5ed"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 404:
            print("City not found.")
            sys.exit()

        if response.status_code == 401:
            print("Invalid API key.")
            sys.exit()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["description"]
        }

    except requests.exceptions.RequestException:
        print("Network error. Please check your connection.")
        sys.exit()


def display_weather(weather):
    print("\nWeather Report")
    print("--------------------------")
    print(f"City        : {weather['city']}")
    print(f"Temperature : {weather['temperature']}°C")
    print(f"Humidity    : {weather['humidity']}%")
    print(f"Wind Speed  : {weather['wind_speed']} m/s")
    print(f"Condition   : {weather['condition']}")


def main():
    parser = argparse.ArgumentParser(description="Live Weather CLI Tool")
    parser.add_argument("city", help="City name to get weather report")

    args = parser.parse_args()

    weather = get_weather(args.city)
    display_weather(weather)


if __name__ == "__main__":
    main()