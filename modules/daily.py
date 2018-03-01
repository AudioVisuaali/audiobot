from mysqlfiles import users_daily_redeem_by_day
from mysqlfiles import users_daily_redeem_by_day_add
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import users_get_daily_points
from mysqlfiles import points_stats_insert
from config import DAILY_AMOUNT_MIN as daily_min
from config import DAILY_AMOUNT_MAX as daily_max
from audiovisuaali import day_splitted_by_time
from audiovisuaali import author_nickanme
from audiovisuaali import time_format_new
from datetime import datetime
from random import randint

# This is daily or #KELA
async def daily(message, client, arguments):

        # deciding what day since epoch
        day = day_splitted_by_time(46800)

        # Checking for redeems for specific day
        redeems = users_daily_redeem_by_day(message.author.id, day)

        # Getting user points
        user_points = users_get_daily_points(message.author.id)[0]

        # Random
        amount = randint(daily_min, daily_max)

        # name
        name = author_nickanme(message.author)

        # Message
        if not redeems:
            await client.send_message(message.channel, ":moneybag: **| You redeemed your daily points worth of {} memes! You now have {} memes!**".format(amount, user_points+amount))
            points_stats_insert(message.server.id, message.author.id, 2, "Daily", "", "", "+"+str(amount), "", "", "", "", "", 0, amount, 0)
            try:
                users_daily_redeem_by_day_add(message.author.id, name, day, amount)
            except:
                users_daily_redeem_by_day_add(message.author.id, "dailyLUL", day, amount)
            users_set_points_to_plus(amount, message.author.id)
        else:
            await client.send_message(message.channel, ":moneybag: **| Check again when the clock is `15:00`**")



# This is daily or #KELA
async def daily_old(message, client, arguemnts):

    dmin = DAILY_AMOUNT_MIN
    dmax = DAILY_AMOUNT_MAX
    wait_time = DAILY_WAIT_TIME
    daily_amount = str(randint(dmin, dmax))

    points = str(int(users_get_daily_points(message.author.id)[0])+int(daily_amount))
    redeems = users_get_daily_redeems(message.author.id, wait_time)

    if message.author.nick is None:
        name = message.author.name
    else:
        name = message.author.nick

    # Add points
    if not redeems:

        # Adding daily points and history log
        das = points_daily_redeem(message.author.id, "daily", daily_amount)

        # Adding points
        points_users_memes_add_on_message(daily_amount, message.author.id)

        letter = "** :moneybag: | {}, you have redeemed your {} daily memes, you now have {} memes! ** ".format(name, daily_amount, points)

    # Time's not up yet ORDER BY first_contact DESC
    else:

        ## THIS WAS PAIN IN THE A**
        # Calculating how long until you can get daily again
        delta = timedelta(hours=wait_time) - (datetime.now() - redeems[0][4])
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Generating time
        if hours != 0:
            time_deff = "{}h {}m {}s".format(hours, minutes, seconds)
        elif minutes != 0:
            time_deff = "{}m {}s".format(minutes, seconds)
        else:
            time_deff = "{}s".format(seconds)

        # Generating message
        letter = "** :moneybag: | Check back in {}! ** ".format(time_deff)

    # Sending message
    await client.send_message(message.channel, letter)
    send(1, "Daily wrought")
