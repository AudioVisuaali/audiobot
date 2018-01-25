from requests import get as rget
from json import loads

from audiovisuaali import send
from random import randint

# Catfact
async def catfact(message, client, arguments):

    number = str(randint(1, 673))
    url = "https://catfact.ninja/fact"
    fact = loads(rget(url).text)

    # Sending message
    letter = ":cat: **| {}**".format(fact["fact"])
    await client.send_message(message.channel, letter)
    send(1, "Catfact received and sent!")
