from mysqlfiles import users_get_daily_points
from mysqlfiles import users_get_daily_redeems
from mysqlfiles import points_daily_redeem
from mysqlfiles import points_users_memes_add_on_message

from config import DAILY_AMOUNT_MIN
from config import DAILY_AMOUNT_MAX
from config import DAILY_WAIT_TIME

from datetime import datetime
from datetime import timedelta

from audiovisuaali import send
from random import randint

# This is daily or #KELA
async def daily(message, client, arguemnts):

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
