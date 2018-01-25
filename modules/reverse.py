from audiovisuaali import send

# Reverse text
async def reverse(message, client, arguments):

    #this reverses it LOL
    await client.send_message(message.channel, "**:arrows_counterclockwise: | {}**".format(arguments[::-1]))
    send(1, "Reversed")
