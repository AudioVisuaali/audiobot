from audiovisuaali import send
from mysqlfiles import users_get_top_points
from mysqlfiles import users_get_top_xp
from discord.utils import get as duget

#TODO ADD .fotmat for each row

# Get points
async def top(message, client, arguments):

        # Checking for no arguments
        if len(arguments) == 0:

            # Getting top users by points
            result = users_get_top_points(client.user.id)
            rows = "Rank | Name \n\n"
            number = 1

            # Creating scoreboard
            for row in result:
                # Gets the users name by id
                name = str(duget(message.server.members, id=row[0]))
                # For space fix
                if len(str(number)) == 1:
                    rows = rows + "["+str(number)+"]  " + name[:-5] + "\n" + " "*8 + "->" + str(row[1]) + " memes \n"
                else:
                    rows = rows + "["+str(number)+"] " + name[:-5] + "\n" + " "*8 + "->" + str(row[1]) + " memes \n"
                number += 1

            # Creating scoreboard and sending it
            scoreboard = "```py\n" + rows + "```"

        # Checks for point scoreboard
        elif len(arguments) == 1:
            if (arguments[0] == "memes") or (arguments[0] == "points"):

                # Getting top users by points
                result = users_get_top_points(str(client.user.id))
                rows = "Rank | Name \n\n"
                number = 1

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    name = str(duget(message.server.members, id=row[0]))
                    # For space fix
                    if len(str(number)) == 1:
                        rows = rows + "["+str(number)+"]  " + name[:-5] + "\n" + " "*8 + "->" + str(row[1]) + " memes \n"
                    else:
                        rows = rows + "["+str(number)+"] " + name[:-5] + "\n" + " "*8 + "->" + str(row[1]) + " memes \n"
                    number += 1

                # Creating scoreboard and sending it
                scoreboard = "```py\n" + rows + "```"

        # Checks for xp scoreboard
        elif len(arguments) == 1:
            if arguments[0] == "xp":

                # Getting top users by points
                result = users_get_top_xp(client.user.id)
                rows = "Rank | Name \n\n"
                number = 1

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    name = str(duget(message.server.members, id=row[0]))
                    # For space fix
                    if len(str(number)) == 1:
                        rows = rows + "["+str(number)+"]  " + name[:-5] + "\n" + " "*8 + "->" + str(row[1]) + "xp \n"
                    else:
                        rows = rows + "["+str(number)+"] " + name[:-5] + "\n" + " "*8 + "->" + str(row[1]) + "xp \n"
                    number += 1

                # Creating scoreboard and sending it
                scoreboard = "```py\n" + rows + "```"

        await client.send_message(message.channel, scoreboard)
        send(1, "Toplist sent")
