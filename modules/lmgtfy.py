from audiovisuaali import send
from urllib.request import quote
import asyncio

# lmgtfy
async def lmgtfy(message, client, arguments):

        # Query
        google = "<http://lmgtfy.com/?q={}>".format(quote(arguments))

        # Sending message
        msg = await client.send_message(message.channel, "<@"+message.author.id+"> Let")
        await asyncio.sleep(0.5)
        await client.edit_message(msg, "<@"+message.author.id+"> Let me")
        await asyncio.sleep(0.5)
        await client.edit_message(msg, "<@"+message.author.id+"> Let me Google")
        await asyncio.sleep(0.5)
        await client.edit_message(msg, "<@"+message.author.id+"> Let me Google that")
        await asyncio.sleep(0.5)
        await client.edit_message(msg, "<@"+message.author.id+"> Let me Google that for")
        await asyncio.sleep(0.5)
        await client.edit_message(msg, "<@"+message.author.id+"> Let me Google that for you!\n"+google)

        send(1, "Lmgtfy processed!")
