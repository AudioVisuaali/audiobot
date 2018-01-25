from mysqlfiles import command_retrieve as m_command_retrieve
from audiovisuaali import send as asend

# command_retrieve redirect and print
async def command_retrieve(message, client, arguments):

    # Searching for response
    send = m_command_retrieve(arguments)

    if send is None:
        asend(1, "Command not found anywhere!")
        return

    if asend is None:
        asend(1, "Command not found")
        return

    else:

        # Sending message
        await client.send_message(message.channel, "<@{}> ".format(message.author.id, send[0]))
        send(1, "Command sent!")
        return


    #TODO: logging
    #TODO: add error here
    return
