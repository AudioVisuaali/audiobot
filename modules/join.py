from config import SELECT_TIME_RAFFLE as select_time_raffle
from config import SELECT_DAY_RAFFLE as select_day_raffle
from config import START_TIME_RAFFLE as start_time_raffle
from config import START_DAY_RAFFLE as start_day_raffle
from config import END_TIME_RAFFLE as end_time_raffle
from config import END_DAY_RAFFLE as end_day_raffle
from mysqlfiles import lotto_join_get_user_tickets
from mysqlfiles import lotto_join_add_user
from audiovisuaali import time_now_today_seconds_so_far
from audiovisuaali import time_format_new
from audiovisuaali import total_weeks
from datetime import datetime

# This is under contstruction _DASDAS
# TODO Not done yet
# Upcoming feature for lotto
#TODO cleanup to def's and stuff all time stuff in time class in audiovisuaali -> then must fix all the other fiesl that use time def's

# Raffle
async def raffle_lotto(message, client, arguments):

    if len(arguments) == 0:
        await client.send_message(message.channel, "ADAASDDSAAASSDA JOIN LOTTO BLAHBAH")


    elif arguments[0] == "lotto":

        # Something
        total_weeks_amount = total_weeks()
        today_time_in_seconds = time_now_today_seconds_so_far()
        weekday_date = datetime.today().weekday()

        #if past
        if weekday_date > end_day_raffle or (weekday_date == end_day_raffle and today_time_in_seconds > end_time_raffle):

            if weekday_date < select_day_raffle or (weekday_date == select_day_raffle and today_time_in_seconds < select_time_raffle):
                time_unitll_asd = time_format_new(select_day_raffle, select_time_raffle)
                days, remainder = divmod(time_unitll_asd, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)

                # Generating time
                if days != 0:
                    time_deff = "{}d {}h {}m {}s".format(days, hours, minutes, seconds)
                elif hours != 0:
                    time_deff = "{}h {}m {}s".format(hours, minutes, seconds)
                elif minutes != 0:
                    time_deff = "{}m {}s".format(minutes, seconds)
                else:
                    time_deff = "{}s".format(seconds)

                await client.send_message(message.channel, ":tickets: **| Winners are going to be released soon!! {}**".format(time_deff))
            else:
                time_unitll_asd = time_format_new(start_day_raffle, start_time_raffle)
                days, remainder = divmod(time_unitll_asd, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)

                # Generating time
                if days != 0:
                    time_deff = "{}d {}h {}m {}s".format(days, hours, minutes, seconds)
                elif hours != 0:
                    time_deff = "{}h {}m {}s".format(hours, minutes, seconds)
                elif minutes != 0:
                    time_deff = "{}m {}s".format(minutes, seconds)
                else:
                    time_deff = "{}s".format(seconds)

                await client.send_message(message.channel, ":tickets: **| Lotto is closed come back next week! Come back in {}**".format(time_deff))
                return

        # if before
        elif weekday_date < start_day_raffle or (weekday_date == start_day_raffle and today_time_in_seconds < start_time_raffle):
            # TODO Add wait D H M format
            time_unitll_asd = time_format_new(start_day_raffle, start_time_raffle)
            days, remainder = divmod(time_unitll_asd, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Generating time
            if days != 0:
                time_deff = "{}d {}h {}m {}s".format(days, hours, minutes, seconds)
            elif hours != 0:
                time_deff = "{}h {}m {}s".format(hours, minutes, seconds)
            elif minutes != 0:
                time_deff = "{}m {}s".format(minutes, seconds)
            else:
                time_deff = "{}s".format(seconds)

            await client.send_message(message.channel, ":tickets: **| Lotto opens in {}**".format(time_deff))
            return

        else:

            get_users_tickets = lotto_join_get_user_tickets(message.server.id, message.author.id, total_weeks_amount)[0]
            if get_users_tickets > 0:
                await client.send_message(message.channel, ":tickets: **| Already joined lotto for the week!**")
            else:
                await client.send_message(message.channel, ":tickets: **| Joined lotto, GL HF!**")
                lotto_join_add_user(message.server.id, message.author.id, total_weeks_amount)
    return
