from mysqlfiles import users_get_daily_points
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import users_set_points_to_minus
from mysqlfiles import points_history_roulette_add

from config import ROULETTE_MIN_POINTS
from config import ROULETTE_WINRATE
from config import ROULETTE_SPECIAL_WINRATE
from config import ROULETTE_RAND_LOW
from config import ROULETTE_RAND_HIGH
from config import ROULETTE_SPECIAL_CHANNELS

from asyncio import sleep as sleepS
from math import floor as mfloor
from audiovisuaali import send
from random import randint


#roulette
async def roulette(message, client, arguments):

    #if not message.channel.id in ["404356322595962880"]:
    #    return
    if len(arguments) == 1:

        #VALUES
        min_points = ROULETTE_MIN_POINTS
        winrate = ROULETTE_WINRATE
        special_winrate = ROULETTE_SPECIAL_WINRATE
        rand_low = ROULETTE_RAND_LOW
        rand_high = ROULETTE_RAND_HIGH
        special_channels = ROULETTE_SPECIAL_CHANNELS

        # Variables
        multiplier_outcome_str = "" # DO NOT TOUCH
        multiplier_outcome_multiplier_str = "" # DO NOT TOUCH
        amount = arguments[0] # DO NOT TOUCH

        # Getting name
        try:
            name = message.author.nick
            if name is None:
                name = message.author.name
        except:
            name = message.author.name

        # Getting the amount of points
        user_points = users_get_daily_points(message.author.id)[0]

        #Validating input and roulette amount
        if amount != "all":

            # all in
            all_in = False

            # Checking for k=1000 points
            if "k" in amount:
                amount = float(arguments[0].lower().replace("k","")) * 1000

            #Checking if number
            try:
                user_gamble = int(amount)
            except ValueError:
                return

        # Assigning users all points for !roulette all
        else:
            user_gamble = user_points
            all_in = True

        # Checking if user gambled mreo than x aoumnt of points
        if user_gamble < min_points:
            await client.send_message(message.channel, "<@{}> **You have to gamble at least {} memes!**".format(message.author.id, min_points))
            return

        # Checking pointsif user_gamble > user_points:
        if user_gamble > user_points:
            await client.send_message(message.channel, "<@{}> **You don't have enough memes to gamble, you need {} memes!**".format(message.author.id, user_gamble - user_points))
            return

        # Cpecial channels
        if message.channel.id in special_channels:
            if randint(1,100) > special_winrate:
                winrate = special_winrate
                # Creating multiplier
                mvalue = float(randint(rand_low, rand_high) / 100)
                moutcome = int(mfloor(user_gamble * mvalue - user_gamble))
                multiplier_outcome_str = "**+" + str(moutcome) + "**"
                multiplier_outcome_multiplier_str = "Multiplier " + str(mvalue)

        # Win
        if randint(1,100) < winrate:

            # Calculations for message formation later on
            outcome_total = user_gamble # + multiplier TODO
            total_points = user_points + outcome_total

            # Adding points and logging event for user
            users_set_points_to_plus(user_gamble, message.author.id)
            points_history_roulette_add(message.author.id, "", user_gamble, "win", all_in)

            # Determine afterfix
            if all_in:
                win_afterfix = ":confetti_ball: :confetti_ball:"
            else:
                win_afterfix = ":confetti_ball:"

            # Creating message
            letter = "** :slot_machine:  | {}, you have won {}{} memes, you now have {} memes! {} {}** ".format(name, outcome_total, multiplier_outcome_str, total_points, win_afterfix, multiplier_outcome_multiplier_str)

        # Lose
        else:

            # Calculations for message formation later on
            outcome_total = user_gamble # + multiplier disabled cause not fair LUL
            total_points = user_points - outcome_total

            # Adding points and logging event for user
            users_set_points_to_minus(user_gamble, message.author.id)
            points_history_roulette_add(message.author.id, "", user_gamble, "lose", all_in)

            # Determine afterfix
            if all_in:
                win_afterfix = "<:angery:280761870447673344>"
            else:
                win_afterfix = "<:feelsrageman:318490463323553795>"

            # Creating message
            letter = "** :slot_machine:  | {}, you have lost {} memes, you now have {} memes! {}** ".format(name, outcome_total, total_points, win_afterfix)

        # Sending message, checking if worth of excitement
        if user_gamble / user_points > 0.8:
            msg = await client.send_message(message.channel, "**<:VenskerChamp:313049600984612865> Rolling **")
            await sleepS(4.0)
            await client.edit_message(msg, letter)
            return
        else:
            await client.send_message(message.channel, letter)
