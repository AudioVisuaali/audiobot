from audiovisuaali import send
from random import randint

# Choose (Chooses random answer)
async def choose(message, client, arguments):

    # Choosing a random answer from given choices
    response = arguments[randint(0, len(arguments) - 1)]

    # Sending message to discord
    await client.send_message(message.channel, ":game_die: **| <@{}> {}**".format(message.author.id, response))
    send(1, "Chose one")
    return
