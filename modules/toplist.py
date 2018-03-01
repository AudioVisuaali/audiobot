from audiovisuaali import send
from config import OWNER_ID as owners
from mysqlfiles import users_get_top_xp
from discord.utils import get as duget
from config import COMMAND_START as starter

from mysqlfiles import points_stats_get_win_high
from mysqlfiles import points_stats_get_lost_high
from mysqlfiles import users_get_top_points_by_wallet
from mysqlfiles import users_get_top_points_by_bank
from mysqlfiles import users_get_top_points_with_bank
from mysqlfiles import points_stats_get_high
#TODO ADD .fotmat for each row


# Formats username if nick is present or user left the server
def users_name(user_object, row):

    if user_object is None:
        name = "User left the server ID:{}".format(row[0])
    else:
        if user_object.nick is None:
            name =user_object.name
        else:
            name = user_object.nick
    return name

# Number checker
def check_is_number(number):
    try:
        int(number)
        return True
    except:
        return False


# Get points
async def top(message, client, arguments):

    try:
        # No arguments give normal list
        if len(arguments) == 0:

            # header
            rows = "**Ranking top __memes__ order by condescending (wallet + bank)**```py\nRank | Name \n\n"

            # Getting results
            result = users_get_top_points_with_bank(client.user.id, 5)

            number = 1
            # Creating scoreboard
            for row in result:

                user_object = duget(message.server.members, id=row[0])

                # Name
                name = users_name(user_object, row)

                # stat
                rows = rows + "[{}{}] {}\n{}->{} memes ({}+{})\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*8, str(row[3]),str(row[1]),str(row[2]))
                number += 1

            # Creating scoreboard and sending it
            rows += "```\n**Ranking top __xp__ order by condescending**\n```py\nRank | Name\n\n"

            # Getting top users by points
            result, number = users_get_top_xp(client.user.id, 5), 1

            # Creating scoreboard
            for row in result:
                # Gets the users name by id
                user_object = duget(message.server.members, id=row[0])

                # Name
                name = users_name(user_object, row)

                # For space fix TODO
                rows = rows + "[{}{}] {}\n{}->{} xp\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*8, str(row[1]))
                number += 1

            # Creating scoreboard and sending it
            scoreboard = "\n{}```\n**For more information you can do:\n1. {}top points/memes\n2. {}top memes wallet/bank\n3. {}top xp\n4. {}top win/wins\n5. {}top lose/lost/loses\n6. {}top roulette wins/loses\n7. {}top slots wins/loses**".format(rows, starter, starter, starter, starter, starter, starter, starter)

        elif arguments[0] in ["memes", "points"]:

            if len(arguments) in [2,3] and not check_is_number(arguments[1]):

                if len(arguments) == 3:

                    if message.author.id not in owners:
                        return

                    try:
                        rows_amount = int(arguments[2])
                    except:
                        rows_amount = 10

                    if rows_amount > 30:
                        rows_amount = 30

                else:
                    rows_amount = 10

                # Wallet
                if arguments[1] == "wallet":
                    rows = "**Ranking top __memes__ order by condescending (wallet)**\n```py\nRank | Name \n\n"
                    result = users_get_top_points_by_wallet(client.user.id, rows_amount)

                # Bank
                elif arguments[1] == "bank":
                    rows = "**Ranking top __memes__ order by condescending (bank)**\n```py\nRank | Name \n\n"
                    result = users_get_top_points_by_bank(client.user.id, rows_amount)

                # Return bad input
                else:
                    return

                number = 1
                # Creating scoreboard
                for row in result:

                    user_object = duget(message.server.members, id=row[0])

                    # Name
                    name = users_name(user_object, row)

                    # stat
                    rows = rows + "[{}{}] {}\n{}->{} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*8, str(row[1]))
                    number += 1

                scoreboard = rows + "```"

            else:

                if len(arguments) == 2:
                    try:
                        rows_amount = int(arguments[1])
                    except:
                        rows_amount = 10
                else:
                    rows_amount = 10

                # header
                rows = "**Ranking top __memes__ order by condescending (wallet + bank)**\n```py\nRank | Name \n\n"

                # Getting results
                result = users_get_top_points_with_bank(client.user.id, rows_amount)

                number = 1
                # Creating scoreboard
                for row in result:

                    user_object = duget(message.server.members, id=row[0])

                    # Name
                    name = users_name(user_object, row)

                    # stat
                    rows = rows + "[{}{}] {}\n{}->{} memes ({}+{})\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*8, str(row[3]),str(row[1]),str(row[2]))
                    number += 1

                scoreboard = rows + "```"

        elif arguments[0] == "xp":

            if len(arguments) == 2:
                try:
                    rows_amount = int(arguments[1])
                except:
                    rows_amount = 10
            else:
                rows_amount = 10

            # header
            rows, number = "**Ranking top __xp__ order by condescending**```py\nRank | Name \n\n", 1

            # Getting top users by points
            result = users_get_top_xp(client.user.id, rows_amount)

            # Creating scoreboard
            for row in result:
                # Gets the users name by id
                user_object = duget(message.server.members, id=row[0])

                # Name
                name = users_name(user_object, row)

                # For space fix TODO
                rows = rows + "[{}{}] {}\n{}->{} xp\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*8, str(row[1]))
                number += 1

            # Creating scoreboard and sending it
            scoreboard = "\n{}```".format(rows)


        elif arguments[0] in ["win", "wins"]:

            limit = 10

            # header
            rows, number = "**Ranking top __wins__ order by condescending**```py\nRank | Name \n\n", 1

            # Getting top users by points
            result = points_stats_get_win_high(limit)

            # Creating scoreboard
            for row in result:
                # Gets the users name by id
                user_object = duget(message.server.members, id=row[1])

                # Name
                name = users_name(user_object, row)

                # For space fix TODO
                # [01] username \n mode<spacing>
                print(len(result))
                rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(10-len(row[3])),row[6])
                #rows = rows + "[{}{}] {}\n{}->{} xp\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*8, str(row[1]))
                number += 1

            # Creating scoreboard and sending it
            scoreboard = "\n{}```".format(rows)


        elif arguments[0] in ["lose", "lost", "loses"]:


                    limit = 10

                    # header
                    rows, number = "**Ranking top __loses__ order by condescending**```py\nRank | Name \n\n", 1

                    # Getting top users by points
                    result = points_stats_get_lost_high(limit)

                    # Creating scoreboard
                    for row in result:
                        # Gets the users name by id
                        user_object = duget(message.server.members, id=row[1])

                        # Name
                        name = users_name(user_object, row)

                        # For space fix TODO
                        rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(10-len(row[3])),row[6])
                        number += 1

                    # Creating scoreboard and sending it
                    scoreboard = "\n{}```".format(rows)



        elif arguments[0] == "slots":

            if len(arguments) in [2,3] and not check_is_number(arguments[1]):

                if arguments[1] in ["win", "wins"]:
                    rows = "**Ranking top __slots wins__ order by condescending**```py\nRank | Name \n\n"
                    mode = "plus"
                elif arguments[1] in ["lose", "lost", "loses"]:
                    rows = "**Ranking top __slots loses__ order by condescending**```py\nRank | Name \n\n"
                    mode = "minus"
                else:
                    return

                # Limit
                limit = 10

                # header
                number = 1

                # Getting top users by points, 8 for slots
                result = points_stats_get_high(8, mode, limit) #minus

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    user_object = duget(message.server.members, id=row[1])

                    # Name
                    name = users_name(user_object, row)

                    # For space fix TODO
                    # [01] username \n mode<spacing>
                    rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(6-len(row[3])),row[6])
                    number += 1

                # Creating scoreboard and sending it
                scoreboard = "\n{}```".format(rows)

            else:

                # header
                rows, number = "**Ranking top __slots wins__ order by condescending**```py\nRank | Name \n\n", 1

                # Getting top users by points, 8 for slots
                result = points_stats_get_high(8, "plus", 5) #minus

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    user_object = duget(message.server.members, id=row[1])

                    # Name
                    name = users_name(user_object, row)

                    # For space fix TODO
                    rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(6-len(row[3])),row[6])
                    number += 1

                number = 1
                rows = rows + "```\n**Ranking top __slots loses__ order by condescending**\n```py\nRank | Name \n\n"

                # Getting top users by points, 8 for slots
                result = points_stats_get_high(8, "minus", 5) #minus

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    user_object = duget(message.server.members, id=row[1])

                    # Name
                    name = users_name(user_object, row)

                    # For space fix TODO
                    rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(8-len(row[3])),row[6])
                    number += 1

                # Creating scoreboard and sending it
                scoreboard = "\n{}```\n**For more information you can do:\n1. {}top slots wins\n2. {}top slots loses**".format(rows, starter, starter)

        elif arguments[0] == "roulette":

            if len(arguments) in [2,3] and not check_is_number(arguments[1]):

                if arguments[1] in ["win", "wins"]:
                    rows = "**Ranking top __roulette wins__ order by condescending**```py\nRank | Name \n\n"
                    mode = "plus"
                elif arguments[1] in ["lose", "lost", "loses"]:
                    rows = "**Ranking top __roulette loses__ order by condescending**```py\nRank | Name \n\n"
                    mode = "minus"
                else:
                    return

                # Limit
                limit = 10

                # header
                number = 1

                # Getting top users by points, 8 for slots
                result = points_stats_get_high(5, mode, limit) #minus

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    user_object = duget(message.server.members, id=row[1])

                    # Name
                    name = users_name(user_object, row)

                    # For space fix TODO
                    # [01] username \n mode<spacing>
                    rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(6-len(row[3])),row[6])
                    number += 1

                # Creating scoreboard and sending it
                scoreboard = "\n{}```".format(rows)

            else:

                # header
                rows, number = "**Ranking top __roulette wins__ order by condescending**```py\nRank | Name \n\n", 1

                # Getting top users by points, 8 for slots
                result = points_stats_get_high(5, "plus", 5) #minus

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    user_object = duget(message.server.members, id=row[1])

                    # Name
                    name = users_name(user_object, row)

                    # For space fix TODO
                    rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(6-len(row[3])),row[6])
                    number += 1

                number = 1
                rows = rows + "```\n**Ranking top __roulette loses__ order by condescending**\n```py\nRank | Name \n\n"

                # Getting top users by points, 8 for slots
                result = points_stats_get_high(5, "minus", 5) #minus

                # Creating scoreboard
                for row in result:
                    # Gets the users name by id
                    user_object = duget(message.server.members, id=row[1])

                    # Name
                    name = users_name(user_object, row)

                    # For space fix TODO
                    rows = rows + "[{}{}] {}\n{}->{}{} {} memes\n".format(" "*(len(str(len(result)))-len(str(number))), str(number), name, " "*4, row[3], " "*(8-len(row[3])),row[6])
                    number += 1

                # Creating scoreboard and sending it
                scoreboard = "\n{}```\n**For more information you can do:\n1. {}top roulette wins\n2. {}top roulette loses**".format(rows, starter, starter)


        await client.send_message(message.channel, scoreboard)
        send(1, "Toplist sent")
    except:
        return
