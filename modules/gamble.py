from mysqlfiles import points_stats_get_without_server
from audiovisuaali import get_user_instance
from audiovisuaali import send
from audiovisuaali import author_nickanme
from asyncio import sleep as asleep

# Gamble
async def gamble(message, client, arguments):

        # stuff
        rows, state1, state2, state3, limit, owner = [], 6, 7, 9, 20, message.author
        letter = ":closed_book: **| This is your gambling history!**\n"

        # nothing special
        if len(arguments) == 0:
            pass

        # amnount or different user
        elif len(arguments) == 1:
            try:
                if int(arguments[0]) <= 40:
                    limit = int(arguments[0])
                else:
                    limit = 40

            except:
                owner = await get_user_instance(message, arguments[0])
                if owner is None:
                    return

                name = author_nickanme(owner)
                letter = ":closed_book: **| This is {}'s gambling history!**\n".format(name)


        # different user and amount
        elif len(arguments) == 2:
            try:
                if int(arguments[1]) <= 40:
                    limit = int(arguments[1])
                else:
                    limit = 40

                owner = await get_user_instance(message, arguments[0])
                if owner is None:
                    return

                name = author_nickanme(owner)
                letter = ":closed_book: **| This is {}'s gambling history!**\n".format(name)

            except:
                return

        # Get stats
        get = points_stats_get_without_server(owner.id, limit)

        for row in get:

            # Cimplified :) and Name
            temporary, temp1, temp2, temp3 = [], [], [], []
            temporary.append(row[2])

            # stakes
            if not row[3] == "":
                temp1.append(row[3] + "m")
            if not row[4] == "":
                temp1.append(row[4] + "t")
            temporary.append(", ".join(temp1))

            #outcome
            if not row[5] == "":
                temp2.append(row[5] + "m")
            if not row[6] == "":
                temp2.append(row[6] + "t")
            temporary.append(", ".join(temp2))

            #info
            if not row[7] == "":
                temp3.append(row[7].replace(":",""))
            if not row[8] == "":
                temp3.append(row[8].replace(":",""))
            if not row[9] == "":
                temp3.append(row[9].replace(":",""))
            temporary.append(", ".join(temp3))
            rows.append(temporary)

        # Checking largest rows for each section in "exel"
        for row in rows:
            if len(row[0]) > state1:
                state1 = len(str(row[0]))
            if len(row[1]) > state2:
                state2 = len(str(row[1]))
            if len(row[2]) > state3:
                state3 = len(str(row[2]))

        # I like this is simple when you get it
        letter += "```py\nName  {}| Stake  {}| Outcome  {}| Info\n".format(" "*(state1 - 4), " "*(state2 - 5), " "*(state3 - 7))

        # Creating actual table
        for row in rows:
            letter += "{}{}    {}{}    {}{}    {}\n".format(row[0], " "*(state1-len(str(row[0]))), row[1], " "*(state2-len(str(row[1]))), row[2], " "*(state3-len(str(row[2]))), row[3])
        letter += "```\n**Result in order of time,  __m = memes__  and  __t = tokens__\n\nMore options coming in the future for biggest bets etc!**"

        # send
        await client.send_message(message.channel, letter)
        return
