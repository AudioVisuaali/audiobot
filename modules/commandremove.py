from audiovisuaali import send
from mysqlfiles import command_retrieve
from mysqlfiles import command_remove as mcommand_remove

from config import OWNER_ID as owners

# Remove a command
async def command_remove(message, client, arguments):

    # Checking if the user has enough powers to run the command
    if message.author.id not in owners:
        return

    # Checking if in database
    send_get = command_retrieve(arguments[0], message.server.id)

    # Not in database
    if send_get is None:
        await client.send_message(message.channel, ":information_source:  **| Command doesn't exist!**")
        return

    # Removing
    try:
        mcommand_remove(arguments[0], message.server.id)
        await client.send_message(message.channel, ":white_check_mark: **| Command removed!!**")
    except:
        await client.send_message(message.channel, ":x:  **| Couldn't remove command!!**")
    return
