from audiovisuaali import send
from audiovisuaali import get_user_instance

from mysqlfiles import users_get_points
from mysqlfiles import users_set_points_to_minus
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import tax_pot_history_add
from mysqlfiles import server_stats_tax_pot_add
from mysqlfiles import points_stats_insert

from math import floor as mfloor

# Waiting for confirmation
def guess_check(m):
    if m.content == "PENIS":
        return True
    else:
        return False

# Transfer points
async def transfer_points(message, client, arguments):

        # not enough cureency
        user = users_get_points(message.author.id)[0]

        #!? give all points
        if arguments[1] == "all":
            arguments[1] == str(user)

        try:
            int(arguments[1])
        except ValueError:
            await client.send_message(message.channel, "Invalid amount")
            return

        if user < int(arguments[1]):
            await client.send_message(message.channel, "You don't have enough memes!")
            return

        # less than 10
        if int(arguments[1]) < 10:
            await client.send_message(message.channel, "transfer at least 10 memes!")
            return

        # Transferring to user instance
        user_getting = await get_user_instance(message, arguments[0])
        if user_getting is None:
            await client.send_message(message.channel, "can't find user")
            return

        # checking if sending money toself
        if user_getting == message.author:
            await client.send_message(message.channel, "Can't send money to yourself!")
            return

        letter = ":no_entry:** Olet siirtämässä __" + arguments[1] + "__ meemiä käyttäjälle " + user_getting.name + "!**\n\nTAX: **" + arguments[1] + ":money_with_wings: - " + "20% => " + str(mfloor(int(arguments[1]) * 80 / 100)) + ":money_with_wings:**\nSinun meemisi: " + "**" + str(user) + ":money_with_wings: -> " + str(int(user)-int(arguments[1])) + ":money_with_wings:**\n\n **Hyväksy** seuraavan 20 sekunnin aikana **kirjoittamalla: __PENIS__**"
        keepo = await client.send_message(message.channel, letter)

        # Waiting for right response from user
        guess = await client.wait_for_message(timeout=20.0, author=message.author, check=guess_check)

        # After time passes
        if guess is None:
            letter = ":no_entry_sign: **| Transaction cancelled!**"
            await client.edit_message(keepo, letter)

        # After confirmed
        elif guess.content == "PENIS":
            # adding and removing points SOME NASTY MATH
            users_set_points_to_minus(arguments[1], message.author.id)
            users_set_points_to_plus(str(mfloor(int(arguments[1]) * 80 / 100)), user_getting.id)
            tax_pot_history_add(message.server.id, message.author.id, int(mfloor(int(arguments[1]) * 20 / 100)))
            server_stats_tax_pot_add(int(mfloor(int(arguments[1]) * 20 / 100)))

            # Sending message
            await client.delete_message(keepo)
            await client.send_message(message.channel, ":white_check_mark: **| Siirto onnistui!**")
            points_stats_insert(message.server.id, message.author.id, 7, "Transfer", arguments[1], "", "-"+arguments[1], "", user_getting.name, "", "", "", 0, 0, int(arguments[1]))

        # Logging
        send(1, "Transfer request done!")
        return
