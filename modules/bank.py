from mysqlfiles import get_users_lowest_bank_amount_by_id
from mysqlfiles import users_set_points_to_minus
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import users_set_bank_to_minus
from mysqlfiles import users_set_bank_to_plus
from mysqlfiles import users_get_bank_points
from mysqlfiles import points_stats_insert
from mysqlfiles import users_get_points
from config import BANK_KORKO as interest
from config import BANK_INTEREST_TIME
from config import BANK_INTEREST_DAY
from audiovisuaali import time_format_new
from math import ceil as mceil

# Transfer points
async def bank(message, client, arguments):

    # wealth
    users_points = users_get_points(message.author.id)[0]
    users_bank = users_get_bank_points(message.author.id)[0]
    add_dir = ["add", "deposit", "put", "give"]
    take_dir = ["take", "withdraw", "remove"]

    # How many memes in bank
    if len(arguments) == 0:

        # Time from interest
        past_time = 604800 - (time_format_new(BANK_INTEREST_DAY, BANK_INTEREST_TIME))

        # Users interest
        users_own_interest = mceil((get_users_lowest_bank_amount_by_id(10, past_time, message.author.id)[0][0]) * interest / 100)

        letter = ":bank: **| You have {} memes in your bank! Interest is {}%, Currently: {} memes\n\nInterest is calculated by the amount of memes you've had in the bank for the past week!\nYou receive interest every Tuesday @ 00:00 **".format(users_bank, interest, users_own_interest)
        await client.send_message(message.channel, letter)
        return

    # if all
    if arguments[1] == "all":
        if arguments[0] in add_dir:
            amount = users_points
        elif arguments[0] in take_dir:
            amount = users_bank

    # if not all try to set amount
    else:
        try:
            arguments[1] = arguments[1].replace("k", "000")
            amount = int(arguments[1])
        except:
            await client.send_message(message.channel, ":bank: **| Invalid amount!**")
            return


    # Must use atleast 10 memes
    if amount < 10:
        await client.send_message(message.channel, ":bank: **| You need to atleast use 10 memes!**")
        return


    # Adding memes
    if arguments[0] in add_dir:

        # Checking if usr has memes
        if amount > int(users_points):
            await client.send_message(message.channel, ":bank: **| You don't have enough memes!**")
            return

        # calculating min amount in bank
        minimum = users_bank

        # Add to history
        points_stats_insert(message.server.id, message.author.id, 10, "Bank", amount, "", "-"+str(amount), "", "To bank", "", "", "", minimum, 0, amount)

        # Set stats
        users_set_bank_to_plus(amount, message.author.id)
        users_set_points_to_minus(amount, message.author.id)

        # letter
        await client.send_message(message.channel, ":bank: **| You have transferred {} memes to bank!\n\nYou now have:\n:purse:: {} memes\n:bank:: {} memes**".format(amount, users_points - amount, users_bank + amount))
        return

    # Taking memes
    elif arguments[0] in take_dir:


        # Checking if enough memes in bank
        if amount > int(users_bank):
            await client.send_message(message.channel, ":bank: **| You don't have that many memes in bank!**")
            return

        # calculating min amount in bank
        minimum = users_bank - amount

        # Add to history
        points_stats_insert(message.server.id, message.author.id, 10, "Bank", amount, "", "+"+str(amount), "", "From bank", "", "", "", minimum, amount, 0)

        # Set stats
        users_set_bank_to_minus(amount, message.author.id)
        users_set_points_to_plus(amount, message.author.id)

        # letter
        await client.send_message(message.channel, ":bank: **| You have transferred {} memes to your wallet!\n\nYou now have:\n:purse:: {} memes\n:bank:: {} memes**".format(amount, users_points + amount, users_bank - amount))
        return
