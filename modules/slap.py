from audiovisuaali import get_user_instance
from audiovisuaali import send
from audiovisuaali import author_nickanme

# Slap
async def slap(message, client, arguments):

    # Tryiong to get user instance
    user = await get_user_instance(message, arguments[0])
    if user is None:
        return

    # Creating author name
    author_name = author_nickanme(message.author)

    # Creating clients name
    client_name = author_nickanme(user)

    # Sending message
    letter = "**:raised_back_of_hand: | {} sla:b:s {}!**".format(author_name, client_name)
    await client.send_message(message.channel, letter)
    send(1, "Slapped")
