from audiovisuaali import get_user_instance
from audiovisuaali import author_nickanme
from config import OWNER_ID as owners
from mysqlfiles import users_get_points
from mysqlfiles import users_get_points_and_bank

# Get points
async def points(message, client, arguments):
        letter = ""

        # Checking your own points
        if len(arguments) == 0:

            # Getting points
            response = users_get_points_and_bank(message.author.id)[0]

            name = author_nickanme(message.author)

            # Sending message
            letter = "**:money_with_wings:  | {} you have {} ({}+{}) memes!** ".format(name, str(response[0]+response[1]), str(response[0]), str(response[1]))

        # Checking someone elses points
        elif len(arguments) == 1:

            if not message.author.id in owners:
                return

            # Getting user
            user = await get_user_instance(message, arguments[0])

            if user is None:
                letter = "**:money_with_wings: | User not found!**"
            else:
                # Getting points
                response = users_get_points_and_bank(message.author.id)[0]

                # Name
                name = author_nickanme(user)

                # Creating message
                letter = "**:money_with_wings:  | {} has {} ({}+{}) memes! ** ".format(name, str(response[0]+response[1]), str(response[0]), str(response[1]))

        # Sending message
        await client.send_message(message.channel, letter)
