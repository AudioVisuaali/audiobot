from audiovisuaali import send
from requests import get as rget
from json import loads

# random pun
async def pun(message, client, arguments):

    #Starting to fetch a Catfact
    response = loads(rget("http://getpuns.herokuapp.com/api/random").text)["Pun"]

    # Sending message
    await client.send_message(message.channel, "<:honk:309227566680637441> **| {}**".format(response))
    send(1, "Pun sent")
