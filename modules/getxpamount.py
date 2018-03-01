from audiovisuaali import send
from audiovisuaali import level_check_command
from audiovisuaali import get_user_instance
from math import floor as mfloor
from mysqlfiles import users_get_xp
from config import OWNER_ID as owners
# Get points
async def user_xp(message, client, arguments):

    # For user request
    if len(arguments) == 0:

        # Calculating xp and level
        response = users_get_xp(message.author.id)
        levels = level_check_command(message.author.id)
        progress = str(mfloor((levels[2] / levels[3])*100))

        await client.send_message(message.channel, ":b:  **| " + message.author.name + " you are level "+str(levels[1])+" and you have " + str(response[0]) + " xp in total! "+progress+"% done on the current level!**")

    # user request on others
    if len(arguments) == 1:
        if not message.author.id in owners:
            return
        # Getting user
        user = await get_user_instance(message, arguments[0])

        # Getting xp and calculating level for id
        response = users_get_xp(user.id)
        levels = level_check_command(user.id)
        progress = str(mfloor((levels[2] / levels[3])*100))

        # Sending message
        await client.send_message(message.channel, ":b:  **| "+ user.name + " is level "+str(levels[1])+" and has " + str(response[0]) + " xp in total! "+progress+"% done on the current level!**")
