from audiovisuaali import send
from urllib.request import quote
from requests import get as rget
from json import loads
from config import GOOGLE_API_KEY as google_api_key

# geolocation
async def geolocation(message, client, arguments):

    link = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}&language={}".format(quote(arguments[0]), google_api_key, "en")
    response = loads(rget(link).text)
    if response["status"] == "OK":
        lat = str(float("{0:.4f}".format(response["results"][0]["geometry"]["location"]["lat"])))
        lng = str(float("{0:.4f}".format(response["results"][0]["geometry"]["location"]["lng"])))
        letter = ":earth_americas: **| {}\n__LAT:__ {}\n__LNG:__ {}**".format(response["results"][0]["formatted_address"], lat, lng)
    else:
        letter = "Google has some broplems with their servers or my servers connection is scuffed LUL"

    await client.send_message(message.channel, letter)
    send(1, "Geolocationed!")
    return
