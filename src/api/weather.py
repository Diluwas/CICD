import requests

api_key = "1eb288508efec21247aa848b278a4f42"


def format_data(city, data):
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    return (
        f"The weather in {city} is {weather} "
        f"with a temperature of {temperature} Celcius."
    )


def get_lat_lon(city):
    url = (
        f"http://api.openweathermap.org/geo/1.0/direct?"
        f"q={city}&limit=1&appid={api_key}"
    )

    print(f"Retrieving latitude and longitude for {city}")

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data:
        return data[0]['lat'], data[0]['lon']
    else:
        print("Failed to retrieve latitude and longitude", data)
        return None, None


def get_weather(city):
    lat, lon = get_lat_lon(city)

    if lat is None or lon is None:
        return False, f"Failed to retrieve weather  information for {city}"
    print(f"Got Lat Lon for {city}: Latiture - {lat}, Longitude - {lon}")
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"units=metric&lat={lat}&lon={lon}&appid={api_key}"
    )
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(F"Retrieved weather information for {city}.", data)
        return True, format_data(city, data)
    else:
        print("Failed to retrieve weather information", data)
        return False, "Failed to retrieve weather information"


if __name__ == "__main__":
    city = "Colombo"
    print(get_weather(city))
