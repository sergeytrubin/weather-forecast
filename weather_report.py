import requests

city = "New York"

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
weather_data = get_weather_data(get_woeid(city))

print(weather_data)