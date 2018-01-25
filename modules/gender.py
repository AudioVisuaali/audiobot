from audiovisuaali import send
from json import loads
from requests import get as rget
from urllib.request import quote
from math import ceil as mceil

# guess gender
async def gender(message, client, arguments):

    #Starting to fetch a Catfact
    url = "https://api.genderize.io/?name={}".format(quote(arguments[0]))
    response = loads(rget(url).text)

    letter = ":alien: **| No data was found for {}!**".format(arguments[0])

    # Checking if name is valid from response
    if response["gender"] != None:
        letter = ":alien: **| There's a {}% of {} being a {}!**".format(str(mceil(response["probability"] * 100)), response["name"].title(), response["gender"])

    # Sending message
    await client.send_message(message.channel, letter)
    send(1, "Gendered :P")
    return
