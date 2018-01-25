from audiovisuaali import send
from random import randint

#dice (Random number between 0 and 7)
async def dice(message, client, arguments):

    # Sending message with a number from 1-6
    await client.send_message(message.channel, ":game_die: **| Dice rolled {}**".format(str(randint(1,6))))
    send(1, "Dice rolled")
