from audiovisuaali import send
from requests import get as rget
from json import loads

# Yo mama joke
async def yo_mama(message, client, arguments):

    # Starting to fetch a joke
    url = loads(rget("http://api.yomomma.info/").text)
    response = loads(rget(url).text)
    # Creating letter
    letter = ":juggling: **| {}**".format(response["joke"])

    # Sending message
    await client.send_message(message.channel, letter)
    send(1, "Joke received and sent!")
