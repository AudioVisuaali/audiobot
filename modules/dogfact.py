from audiovisuaali import send
from requests import get as rget
from json import loads
from random import randint

# dogfact (Return a random dagfact)
async def dogfact(message, client, arguments):

    #Starting to fetch a Catfact
    print("[INFO] Fecthing a dogfact FrankerZ")
    response = loads(rget("http://dog-api.kinduff.com/api/facts").text)["facts"][0]

    dog = [":dog:", ":dog2:"][randint(0,1)]

    # Sending message
    await client.send_message(message.channel, "{} **| {}**".format(dog, response))
    send(1, "Dogfact received and sent!")
    return
