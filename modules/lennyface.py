from audiovisuaali import send
from random import randint
from config import LENNYFACES as lennyfaces

# test trash
async def lennyface(message, client, arguments):

    # Defining which lennyface to use
    number = randint(0,len(lennyfaces)-1)

    # Sending lennyface
    await client.send_message(message.channel, lennyfaces[number])
    send(1, "Lennyfac sent :)")
