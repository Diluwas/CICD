from api.weather import format_data


def test_format_weather():
    city = "Los Angeles"
    data = {"weather": [{"description": "sunny"}], "main": {"temp": 25}}
    expected = (
        "The  weather in Los Angeles is sunny "
        "with a temperature of 25 Celcius."
        )
    assert format_data(city, data) == expected

    city = "London"
    data = {"weather": [{"description": "cloudy"}], "main": {"temp": 15}}
    expected = ("The weather in London is cloudy "
                "with a temperature of 15 Celcius."
                )
    assert format_data(city, data) == expected

    city = "Sri Lanka"
    data = {"weather": [{"description": "rainy"}], "main": {"temp": 10}}
    expected = ("The weather in Sri Lanka is rainy "
                "with a temperature of 10 Celcius."
                )
    assert format_data(city, data) == expected
