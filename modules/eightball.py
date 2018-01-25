from audiovisuaali import send
from random import randint
from config import EIGHT_BALL_OPTIONS as eightballresponses

# 8ball (gives random answer to requesters question)
async def eight_ball(message, client, arguments):

    # Checking if message is the right length
    if len(message.content) > 8:

        # Choosing a random answer from choices
        respones = eightballresponses[randint(0, len(eightballresponses) - 1)]

        # Sending answer
        await client.send_message(message.channel, ":8ball: **| <@{}> {}**".format(message.author.id, respones))

    send(1, "Eightballed")
    return
