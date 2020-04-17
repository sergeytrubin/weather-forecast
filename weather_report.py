"""
Where in the world are you? New York
Weather for New York:
2020-04-16          Light Cloud         high 10.1°C         low 5.2°C
2020-04-17          Light Rain          high 10.4°C         low 3.6°C
2020-04-18          Heavy Rain          high 10.4°C         low 7.2°C
2020-04-19          Light Cloud         high 15.9°C         low 5.8°C
2020-04-20          Showers   high 13.9°C         low 9.2°C
2020-04-21          Showers   high 17.1°C         low 5.8°C
Where in the world are you? 

Returns:
    [type] -- [description]
"""


import requests

# function that adding %20 to string if there is a space
def format_string(city):
    location = city.split(" ")
    if len(location) > 1:
        return '%20'.join(location)
    return city

# sending get request to webapi
def get_webapi_data(url):
    req = requests.get(url)
    return req.json()

# getting the WOEID for user location
def get_woeid(city):
    location_string = format_string(city)
    woeid_url = 'https://www.metaweather.com/api/location/search/?query=' + location_string
    woeid_data = get_webapi_data(woeid_url)
    return woeid_data[0]['woeid']

def get_weather_data(woeid):
    metaweather_url = 'https://www.metaweather.com/api/location/' + str(woeid)
    return get_webapi_data(metaweather_url)

# getting the weather data

def show_forecast(city):
    weather_data = get_weather_data(get_woeid(city))
    for forecast in weather_data['consolidated_weather']:
        print(f"{forecast['applicable_date']}\t{forecast['weather_state_name']}\thigh: {forecast['max_temp']:0.2f}\tlow: {forecast['min_temp']:0.2f}")


if __name__ == "__main__":
    city = "New York"
    show_forecast(city)
""" city = "New York"
show_forecast(city) """