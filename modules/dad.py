from audiovisuaali import send
from requests import get as rget
from json import loads

# Joke
async def dad_joke(message, client, arguments):

    # Starting to fetch a joke
    response = loads(rget("https://icanhazdadjoke.com/slack").text)
    # Creating letter
    letter = "<@{}> **| {}**".format(message.author.id, response["attachments"][0]["text"])
    # Sending message
    await client.send_message(message.channel, letter)
    send(1, "Dad joke sent")
    return
