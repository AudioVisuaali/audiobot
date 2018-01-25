from audiovisuaali import send #TODO ADD THIS
from mysqlfiles import profile_id_get
from mysqlfiles import command_retrieve
from mysqlfiles import command_add

async def command_add(message, client, arguments):

    # Checking if the user has enough powers to run the command
    check = profile_id_get(message.author.id)
    print(check)
    if not check[0] ==  message.author.id:
        await client.send_message(message.channel, ":x: | You don't have enough rights to run the command!")
        return

    # Checking if exists
    send = command_retrieve(arguments[0])

    # if exists return
    if send is not None:
        await client.send_message(message.channel, ':x: **| Command already in database!**')
        return

    # Adding command to database
    send = command_add(arguments[0],"".join(arguments)[len(arguments[0]):],"",message.author.id,0)

    # Checking response to know if command succeeded
    if send is None:
        await client.send_message(message.channel, ':white_check_mark: | **Command "__'+arguments[0]+'__" added to the database!**')
        return

    # If command didn't succeed returnin g a error message
    await client.send_message(message.channel, "<@"+message.author.id+"> Couldn't add the command")
    #TODO add logging and error messaging
    return
