from audiovisuaali import send

# ping <=> response pong! TEST COMMAND
async def ping(message, client, arguments):

    # Name

    if message.author.nick is None:
        name = message.author.name
    else:
        name = message.author.nick

    # Send message
    await client.send_message(message.channel, "**:poop: |{} Pong!**".format(name))
    send(1, "Ping test command")
