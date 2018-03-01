from audiovisuaali import send #TODO ADD THIS
from mysqlfiles import command_retrieve
from mysqlfiles import command_add as command_add_mysql

from config import OWNER_ID as owners

async def command_add(message, client, arguments):

    # Checking if the user has enough powers to run the command
    if message.author.id not in owners:
        return

    # Checking if exists
    send = command_retrieve(arguments[0], message.server.id)

    # if exists return
    if send is not None:
        await client.send_message(message.channel, ':x: **| Command already in database!**')
        return

    # ??
    insertation = "".join(arguments)[len(arguments[0]):]

    # Adding command to database
    send = command_add_mysql(message.server.id, arguments[0], insertation, "", message.author.id, 0)

    # Checking response to know if command succeeded
    if send is None:
        await client.send_message(message.channel, ':white_check_mark: | **Command "__'+arguments[0]+'__" added to the database!**')
        return

    # If command didn't succeed returnin g a error message
    await client.send_message(message.channel, "<@"+message.author.id+"> Couldn't add the command")
    return
