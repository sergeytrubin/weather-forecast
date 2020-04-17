"""
Enter location to show weather forecast: New York
Weather for New York:
2020-04-16          Light Cloud         high 10.1°C         low 5.2°C
2020-04-17          Light Rain          high 10.4°C         low 3.6°C
2020-04-18          Heavy Rain          high 10.4°C         low 7.2°C
2020-04-19          Light Cloud         high 15.9°C         low 5.8°C
2020-04-20          Showers   high 13.9°C         low 9.2°C
2020-04-21          Showers   high 17.1°C         low 5.8°C
Where in the world are you?

TODO:
-Simplify code
-remove unnecessary code
-user_location function is not needed all could be done in show_forecast
-format_string is not needed - api accept case insensitive
"""


import requests

def user_location():
    user_city = input('Enter location to show weather forecast: ')
    if isinstance(user_city, str) and len(user_city) > 0:
        return user_city
    return []

# function that adding %20 to string if there is a space
def format_string(city):
    try:
        location = city.split(" ")
        if len(location) > 1:
            for word in location:
                word = word[0].upper() + word[0:].lower()
            return '%20'.join(location)
        return city
    except AttributeError:
        print(f"No forecast data found")
        user_location()

# sending get request to webapi
def get_webapi_data(url):
    req = requests.get(url)
    return req.json()

# getting the WOEID for user location
def get_woeid(city):
    if city == []:
        print(f"No forecast data found for {city}\n")
        user_location()
    location_string = format_string(city)
    woeid_url = 'https://www.metaweather.com/api/location/search/?query=' + location_string
    woeid_data = get_webapi_data(woeid_url)
    return woeid_data[0]['woeid']

# getting the weather data
def get_weather_data(woeid):
    metaweather_url = 'https://www.metaweather.com/api/location/' + str(woeid)
    return get_webapi_data(metaweather_url)

# presenting the weather data
def show_forecast(city):
    weather_data = get_weather_data(get_woeid(city))
    print(f"Weather for {city}:")
    for forecast in weather_data['consolidated_weather']:
        print(f"{forecast['applicable_date']}\t{forecast['weather_state_name']}\thigh: {forecast['max_temp']:0.2f}\tlow: {forecast['min_temp']:0.2f}")


if __name__ == "__main__":
    city = user_location()
    show_forecast(city)
