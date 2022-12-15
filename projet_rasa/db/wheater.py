

import requests


def getWeather(city, country):
    apiKey = "8774e3f9abb32dab6ab497b8dcad67fe"
    apiKey2 ="7314e3953eae2c4ff3a6e16597a07273"

    apiUrl_ = "https://api.openweathermap.org/data/2.5/weather?"
    
    #apiUrl_ = "https://api.openweathermap.org/data/2.5/forecast/hourly?"

    querystring_ = {"q": city, "country code": country,
                    "units": "metric", "appid": apiKey}

    response = requests.request("GET", apiUrl_, params=querystring_)

    return response.json()


def getWeatherByHour(city, country):
    apiKey = "8774e3f9abb32dab6ab497b8dcad67fe"
    #apiKey ="7314e3953eae2c4ff3a6e16597a07273"  
    apiUrl_ = "http://api.openweathermap.org/geo/1.0/direct?"
    querystring_ = {"q": city, "limit": 1, "appid": apiKey}

    response = requests.request("GET", apiUrl_, params=querystring_)  
    response=response.json()
    lat=response[0]["lat"]
    lon=response[0]["lon"]
    
    apiUrl_ = "https://api.openweathermap.org/data/2.5/onecall?"

    querystring_ = {"lat": lat, "lon": lon,
                    "exclude": "minute", "units":"metric", "appid": apiKey}

    response = requests.request("GET", apiUrl_, params=querystring_)


    return response.json()



def getPosition(city):
    apiKey = "8774e3f9abb32dab6ab497b8dcad67fe"
    #apiKey ="7314e3953eae2c4ff3a6e16597a07273"    
    apiUrl_ = "http://api.openweathermap.org/geo/1.0/direct?"
    querystring_ = {"q": city, "limit": 1, "appid": apiKey}

    response = requests.request("GET", apiUrl_, params=querystring_)

    return response


