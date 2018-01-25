from audiovisuaali import send
from requests import get as rget
from json import loads

# Joke
async def chuck_norris(message, client, arguments):

    # Starting to fetch a joke
    response = loads(rget("http://api.icndb.com/jokes/random").text)["value"]["joke"]

    # Creating letter
    letter = "<@{}> **| {}**".format(message.author.id, response)
    # Sending message
    await client.send_message(message.channel, letter)
    send(1, "Chuck Norris joke sent!")
