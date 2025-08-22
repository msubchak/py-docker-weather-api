import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    response = requests.get(
        f"{URL}?key={api_key}&q={CITY}"
    )
    data = response.json()
    print(f"Location: {data['location']['name']}, {data['location']['country']}")
    print(f"Temperature: {data['current']['temp_c']}")


if __name__ == "__main__":
    get_weather()
