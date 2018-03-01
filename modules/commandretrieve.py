from mysqlfiles import command_retrieve as m_command_retrieve
from audiovisuaali import send as asend

# command_retrieve redirect and print
async def command_retrieve(message, client, arguments):

    # Searching for response
    send = m_command_retrieve(arguments, message.server.id)

    # Checking if anything to send
    if send is None:
        return

    # Sending message
    await client.send_message(message.channel, send[0].format("<@{}>".format(message.author.id)))
    return
