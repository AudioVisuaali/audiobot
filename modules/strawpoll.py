from audiovisuaali import send
from strawpy import create_poll

# strawpoll
async def strawpoll(message, client, arguments):

    # name
    if message.author.nick is None:
        name = message.author.name
    else:
        name = message.author.nick

    # Popping question to it's own variation
    question = arguments.pop(0)

    # Creating poll
    new_poll = create_poll(question, arguments)

    # Sending message
    letter = "**Here's your poll, {}**\n{}".format(name, new_poll.url)
    await client.send_message(message.channel, letter)
    send(1, "Strawpoll finished")
