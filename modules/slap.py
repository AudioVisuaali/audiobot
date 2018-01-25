from audiovisuaali import get_user_instance
from audiovisuaali import send

# Slap
async def slap(message, client, arguments):

    # Tryiong to get user instance
    user = await get_user_instance(message, arguments[0])
    if user is None:
        return

    # Creating author name
    if message.author.nick is None:
        author_name = message.author.name
    else:
        author_name = message.author.nick

    # Creating clients name
    if user.nick is None:
        client_name = user.name
    else:
        client_name = user.nick

    # Sending message
    letter = "**:raised_back_of_hand: | {} sla:b:s {}!**".format(author_name, client_name)
    await client.send_message(message.channel, letter)
    send(1, "Slapped")
