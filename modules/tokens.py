from audiovisuaali import get_user_instance
from mysqlfiles import users_get_total_tokens

# Get tokens
async def user_tokens(message, client, arguments):

    if not arguments:
        # Getting total tokens generating message
        info = users_get_total_tokens(message.author.id)
        letter = ":trophy: **| You have {} tokens!**".format(info[0])

    else:

        # Getting user object
        user = await get_user_instance(message, arguments[0])

        # User is
        if user is not None:

            info = users_get_total_tokens(user.id)

            # Creating nickname
            if user.nick is None:
                user_name = user.name
            else:
                user_name = user.nick

            letter = ":trophy: **| {} has {} tokens!**".format(user_name, info[0])

        # User is not
        else:
            letter = ":trophy: **| User not found!**"

    # Sending message
    await client.send_message(message.channel, letter)

    return
