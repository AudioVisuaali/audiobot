from audiovisuaali import day_splitted_by_time
from mysqlfiles import users_daily_redeem_by_day
from mysqlfiles import users_daily_redeem_by_day_add
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import users_get_daily_points
from mysqlfiles import user_add_points
from datetime import datetime
from config import DAILY_AMOUNT_MIN as daily_min
from config import DAILY_AMOUNT_MAX as daily_max
from random import randint
from asyncio import sleep as asleep
from math import floor as mfloor
from config import BANK_KORKO as interest


from mysqlfiles import get_users_lowest_bank_amount
from mysqlfiles import user_add_points_in_bank
from mysqlfiles import get_users_bank_amount
from mysqlfiles import points_stats_insert
from math import ceil as mceil




#TEST
async def test(message, client, arguments):
    asd = """
    users = []

    # Mode_id=10, time="604800", time_type="SECOND"
    bank_update = get_users_lowest_bank_amount(10, "6666", "SECOND")
    for row in bank_update:

        # Split users between (updated this week)
        users.append(row[0])

        # If no money in bank do nothing
        if row[1] != 0:

            # Calculating interest
            add_this_memes = int(mceil(row[1] * interest / 100))

            # Checking if worth of adding
            if add_this_memes != 0:

                # Add memes for user
                user_add_points_in_bank(add_this_memes, row[0])

                # Add logging
                points_stats_insert(message.server.id, row[0], 11, "Interest", 0, "", "+"+str(add_this_memes), "", "Interest", "", "", "", 0, add_this_memes, 0)


    # If bank not updated this week get users' bank amount
    bank_nonupdate = get_users_bank_amount(users)

    # For each user
    for kek in bank_nonupdate:

        # Calculating interest
        add_this_memes = int(mceil(kek[1] * interest / 100))

        # Checking if worth of adding
        if add_this_memes != 0:

            # Add memes for user
            user_add_points_in_bank(add_this_memes, kek[0])

            # Add logging
            points_stats_insert(message.server.id, kek[0], 11, "Interest", 0, "", "+"+str(add_this_memes), "", "Interest", "", "", "", 0, add_this_memes, 0)"""

    asd = 1/0

    await client.send_message(message.channel, "{}".format(message.author.mention))
    error = ""
    try:
        do_for = int(arguments[0])
        if do_for > 111:
            do_for = 111
            error = "**(Max is 111)**"
    except:
        do_for = 10

    state = 0
    times = []
    asd = await client.send_message(message.channel, ":left_right_arrow: **| Ping test to the daiscord servers! {}/{} {}**".format(state, do_for, error))
    delta = datetime.utcnow()
    asd = await client.edit_message(asd,":left_right_arrow: **| Ping test to the discord servers! {}/{} {}\n\n**".format(state, do_for, error))
    for _ in range(do_for):
        #delta = asd.edited_timestamp
        #delta = datetime.utcnow()
        now = datetime.utcnow()
        state += 1
        kek = "```py\n"
        d = now - delta
        times.append(str(d.microseconds)[:3])
        average = 0
        for a in range(len(times)):

            kek += "[{}{}] {}ms\n".format(" "*(len(str(do_for))-len(str(a+1))), a+1, times[a])
            average += int(times[a])
        average = mfloor(average/len(times))
        kek += "```"

        await asleep(0.8)
        delta = datetime.utcnow()
        asd = await client.edit_message(asd,":left_right_arrow: **| Ping test to the discord servers! {}/{} {}\n\n{}\nAverage ping: __{}ms__**".format(state, do_for, error, kek, average))
    asd = await client.edit_message(asd,":left_right_arrow: **| Ping test to the discord servers! {}/{} {} :white_check_mark: \n\n{}\nAverage ping: __{}ms__** :white_check_mark:".format(state, do_for, error, kek, average))
