from audiovisuaali import send
from audiovisuaali import get_user_instance
from mysqlfiles import users_get_roll_stats
from math import floor as mfloor


async def tuplat(message, client, arguments):

    if len(arguments) == 0:
        # Getting stats
        user = message.author
        stats = users_get_roll_stats(message.author.id)

    else:

        user = await get_user_instance(message, arguments[0])
        try:
            stats = users_get_roll_stats(user.id)
        except:
            send(1, "No user found")
            await client.send_message(message.channel, ":game_die: **| User not found!**")
            return

    # Name
    if user.nick is None:
        name = user.name
    else:
        name = user.nick

    # name
    user_mention = " for: " + name

    # Calculating winrate
    try:
        win_rate = mfloor(int(stats[1]) / int(stats[0]) * 100)
    except:
        win_rate = "0"
    # Memes
    if stats[2] == 0:
        memes = ""
    else:
        try:
            memes = "\n:money_with_wings: Memes gained: {}".format(mfloor(stats[2]))
        except:
            memes = ""

        # Tokens
    if stats[3] == 0:
        tokens = ""
    else:
        try:
            tokens = "\n:trophy: Tokens gained: {}".format(mfloor(stats[3]))
        except:
            tokens = ""

    # Creating message
    letter = ":game_die: **| Roll stats{}\n\n:arrows_counterclockwise: Rolled: {}\n:tada: Doubles: {}\n:thinking: Win-rate: {}%{}{}**".format(user_mention, stats[0], stats[1], win_rate, memes, tokens)

    await client.send_message(message.channel, letter)
