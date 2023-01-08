import requests


def getWeather(city):
    apiKey = "8774e3f9abb32dab6ab497b8dcad67fe"

    apiUrl_ = "https://api.openweathermap.org/data/2.5/weather?&lang=fr"
    
    country=getPosition(city)
    querystring_ = {"q": city, "country code": country,
                    "units": "metric", "appid": apiKey}
    response = requests.request("GET", apiUrl_, params=querystring_)
    response = response.json()['main']
    if(response['feels_like']<12):
        response = f'Il fait froid à {city}, la température est à {response["feels_like"]} dégrée celcius. N oublie pas d apporter des vetements chauds.'
    elif response['feels_like']<18:
        response = f'Il ne fait pas trops froid à {city}, la température est à {response["feels_like"]} dégrée celcius. Vous pouvez apporter des vetements chauds.'
    elif response['feels_like']<24:
        response = f'Il fait un peu chaud  à {city}, la température est à {response["feels_like"]} dégrée celcius.'
    else:
        response = f'Il fait chaud  à {city}, la température est à {response["feels_like"]} dégrée celcius. '
    return response

def getPosition(city):
    apiKey = "8774e3f9abb32dab6ab497b8dcad67fe" 
    apiUrl_ = "http://api.openweathermap.org/geo/1.0/direct?"
    querystring_ = {"q": city, "limit": 1, "appid": apiKey}

    response = requests.request("GET", apiUrl_, params=querystring_)

    return response.json()[0]["country"]

if __name__ == '__main__':
   print( getWeather("Paris","USA"))




