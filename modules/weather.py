from audiovisuaali import send
from urllib.request import quote
from json import loads
from config import WEATHER_API as apikey
from datetime import datetime
from requests import get as rget

# weather
async def weather(message, client, arguments):

    # Fetches weather
    send(1, "Fetching weather data")
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (quote(arguments), apikey)
    data = loads(rget(url).text)

    # Formulating response DO NOT TOUCH WAS PAIN :)
    try:
        definition = data["name"]+"\nCurrently:    "+data["weather"][0]["description"]+"\nWind speed:   "+str(data["wind"]["speed"])+" m/s\nCurrent Temp: "+str(int(data["main"]["temp"]-273.15))+" °C / "+str(int((data["main"]["temp"]-273.15)*9/5+32))+" °F \nMax Temp:     "+str(int(data["main"]["temp_max"]-273.15))+" °C / "+str(int((data["main"]["temp_max"]-273.15)*9/5+32))+" °F \nMin Temp:     "+str(int(data["main"]["temp_min"]-273.15))+" °C / "+str(int((data["main"]["temp_min"]-273.15)*9/5+32))+" °F \nSunrise:      "+datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M:%S')[11:16]+"\nSunset:       "+datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%Y-%m-%d %H:%M:%S')[11:16]+"\nHumidity:     "+str(data["main"]["humidity"])+" %"+"\nPressure:     "+str(data["main"]["pressure"])+"00 Pa"+"\nLon:          "+str(data["coord"]["lon"])+"°\nLat:          "+str(data["coord"]["lat"])+"°\n"
        response = "Weather in: "+data["name"]+", "+data["sys"]["country"]+"```"+definition+"```"
    except KeyError:
        response = "No match was found"

    # Sending message and logging
    await client.send_message(message.channel, ":earth_africa: **| {}**".format(response))
    send(1, "Done with fetching weather data")
