import requests
import os
from dotenv import load_dotenv
   
load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("\nCity not found!")
            return None
        else:
            print("\nSomething went wrong.")
            return None

    except requests.exceptions.ConnectionError:
        print("\nNo Internet Connection.")
        return None


def display_weather(data):
    print("\n==============================")
    print("      WEATHER REPORT")
    print("==============================")
    print(f"City        : {data['name']}")
    print(f"Country     : {data['sys']['country']}")
    print(f"Temperature : {data['main']['temp']} °C")
    print(f"Feels Like  : {data['main']['feels_like']} °C")
    print(f"Humidity    : {data['main']['humidity']} %")
    print(f"Pressure    : {data['main']['pressure']} hPa")
    print(f"Weather     : {data['weather'][0]['main']}")
    print(f"Description : {data['weather'][0]['description']}")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")
    print("==============================\n")


def main():
    print("===================================")
    print("      WEATHER CLI APPLICATION")
    print("===================================")

    while True:
        city = input("Enter City Name (or type exit): ")

        if city.lower() == "exit":
            print("\nThank you for using Weather CLI!")
            break

        data = get_weather(city)

        if data:
            display_weather(data)


if __name__ == "__main__":
    main()