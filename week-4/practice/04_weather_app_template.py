import os
import requests


def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY is not configured.")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def main():
    city = input("Enter city name: ").strip()

    try:
        data = get_weather(city)

        print("\nWeather Information")
        print("-" * 30)
        print(f"City        : {data['name']}")
        print(f"Temperature : {data['main']['temp']} °C")
        print(f"Feels Like  : {data['main']['feels_like']} °C")
        print(f"Humidity    : {data['main']['humidity']}%")
        print(f"Condition   : {data['weather'][0]['description'].title()}")

    except requests.HTTPError:
        print("Unable to retrieve weather. Check the city/API key.")
    except requests.RequestException as error:
        print(f"Network error: {error}")
    except (KeyError, TypeError):
        print("Unexpected weather API response.")
    except RuntimeError as error:
        print(error)


if __name__ == "__main__":
    main()
