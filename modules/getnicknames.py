from audiovisuaali import send
from mysqlfiles import user_nicknames_get

# get nicknames TODO NOT DONE
async def get_nicknames(message, client, arguments):

    try:
        message.server.id
        message.author.id

        response = user_nicknames_get(message.server.id, message.author.id)
        nick_list = [message.author.name,]

        for nickname in response:
            nick_list.extend(nickname)

        fmt = "**Nicknames:** " + ', '.join(nick_list)
    except AttributeError:
        fmt = "**Command is server specific!**"

    # send and log
    await client.send_message(message.channel, fmt)
    send(1, "Nicknames")
    return
