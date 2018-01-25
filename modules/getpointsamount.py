from audiovisuaali import get_user_instance
from config import OWNER_ID as owner_id
from mysqlfiles import users_get_points
from mysqlfiles import profile_id_get

# Get points
async def points(message, client, arguments):
        letter = ""

        # Checking your own points
        if len(arguments) == 0:

            # Getting points
            response = users_get_points(message.author.id)

            # Sending message
            letter = "**:money_with_wings:  | {} you have {} memes!** ".format(message.author.name, str(response[0]))

        # Checking someone elses points
        elif len(arguments) == 1:

            if not (message.author.id in owner_id or (profile_id_get(message.author.id)[1] == "3")):
                return

            # Getting user
            user = await get_user_instance(message, arguments[0])

            if user is None:
                letter = "**:money_with_wings: | User not found!**"
            else:
                # Getting points
                response = users_get_points(user.id)

                # Creating message
                letter = "**:money_with_wings:  | {} has {} memes! ** ".format(user.name, str(response[0]))

        # Sending message
        await client.send_message(message.channel, letter)
