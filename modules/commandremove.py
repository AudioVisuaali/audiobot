from audiovisuaali import send
from mysqlfiles import profile_id_get
from mysqlfiles import command_retrieve
from mysqlfiles import command_remove

# Remove a command
async def command_remove(message, client, arguments):

    # Checking if the user has enough powers to run the command
    check = profile_id_get(message.author.id)
    if not check[0] ==  message.author.id:
        await client.send_message(message.channel, "<@"+message.author.id+"> You don't emough powers to run the command!")
        return

    # Checking if in database
    send = command_retrieve(arguments[0])

    # Not in database
    if send is None:
        await client.send_message(message.channel, ":white_check_mark: **| Command not in database, command removed!**")
        return

    # Removing
    command_remove(arguments[0])
    await client.send_message(message.channel, ":white_check_mark: **| Command not in database!**")

    send(1, "Command removed")
    return


#TODO: logging
#TODO: console output
