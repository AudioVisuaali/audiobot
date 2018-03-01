from audiovisuaali import send
from audiovisuaali import get_user_instance
from config import OWNER_ID as owners

# time Get's current time
async def joined(message, client, arguments):

    # Checking if the user has enough powers to run the command
    if message.author.id not in owners:
        return

    # self or other
    if not arguments:
        owner = message.author
    else:
        owner = await get_user_instance(message, arguments[0])

    # Name
    if owner.nick is None:
        name = owner.name
    else:
        name = owner.nick

    await client.send_message(message.channel, "**:calendar_spiral: | {} joined the server on {}**".format(name, str(owner.joined_at)[:-7]))
    send(1, "Joined done")
