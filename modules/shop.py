import audiovisuaali
import mysqlfiles
import discord
import math
import asyncio

def generate_menu(message, client, arguments, vision=None, extra=None):

    # Get users resources
    author_wealth_memes= mysqlfiles.users_get_points(message.author.id)[0]
    author_wealth_tokens = mysqlfiles.users_get_total_tokens(message.author.id)[0]

    # Shop header
    letter = ":shopping_cart: **| You have opened the shop menu!**\n"
    letter += "**:money_with_wings: {} | :trophy: {}**\n```".format(author_wealth_memes, author_wealth_tokens)

    # variables and lists
    items = mysqlfiles.shop_get_items()
    item_count = 0
    buy_list_dependent_on_user = []

    # Shop content
    for row in items:

        # Checking if and or price
        if row[4] is 0:

            # OR
            if row[2] and row[3]:
                price = str(row[2]) + "memes / " + str(row[3]) + " tokens"
                buy_list_dependent_on_user.append(row)

            # Memes
            elif row[2] is not None:
                price = str(row[2]) + " memes"
                buy_list_dependent_on_user.append(row)

            # Tokens
            elif row[3] is not None:
                price = str(row[3]) + " tokens"
                buy_list_dependent_on_user.append(row)

        # And      print(row[4])
        else:
            price = str(row[2]) + " memes & " + str(row[3]) + " tokens"
            buy_list_dependent_on_user.append(row)

        letter += str(item_count+1) + ". " + row[0] + "\n    -" + price + "\n"
        item_count += 1

    # Menu end
    letter += "```\n**:moneybag: | You purchase an item by typing the following number in the next 60 seconds!"
    letter += "\n:arrow_right: | Exit menu by typing __exit__\n"

    # Smaller to test TODO change later
    if len(buy_list_dependent_on_user) > 10:
        letter += "\n:fast_forward: | Type next for next page\n\n"

    # extra plot for "after user input"
    # vision = 1, all ok
    # vision = 0, error
    if vision is not None:
        if vision == 0:
            letter += "\n:no_entry_sign: | " + extra + "**"
        elif vision == 1:
            letter += "\n:white_check_mark: | " + extra + "**"
    else: letter += "**"

    # Returning for later use of buying items
    return letter, buy_list_dependent_on_user, item_count


async def shop(message, client, arguments):
    #if message.channel.id in ["404356322595962880","404356266886955009"]:
    #    return
    if message.channel.id != "404356266886955009":

        letter = "You can use shop only in #Golden Frog Casino >>> #shop When it's open"
        await client.send_message(message.channel, letter)
        return

    letter = generate_menu(message, client, arguments)

    # Sending message
    sent_1 = await client.send_message(message.channel, letter[0])

    # Confirming channel
    def confirmation(m):
        if m.channel == message.channel:
            return True
        else:
            return False

    # Making a shop loop
    while True:

        guess = await client.wait_for_message(timeout=60.0, author=message.author, check=True)
        await client.delete_message(sent_1)

        if guess is None:
            letter = ":x: **| Shop has been closed due to inactivity!**"
            sent_1 = await client.send_message(message.channel, letter)
            await asyncio.sleep(10.0)
            await client.delete_message(sent_1)
            return

        elif guess.content == "!shop":
            try:
                await client.delete_message(sent_1)
            except:
                audiovisuaali.send(1, "Not able to open shop prob a restart was issued")
            return

        elif guess.content == "!exit" or guess.content == "exit":
            letter = ":x: **| You have left the shop!**"
            sent_1 = await client.send_message(message.channel, letter)
            await asyncio.sleep(10.0)
            await client.delete_message(sent_1)
            return

        elif guess.content.isdigit():

            # 1. give server group
            # 2. set memes
            # 3. set tokens
            # getting item that user wants to get
            do_stuff = letter[1][int(guess.content)-1]
            switch_type = int(do_stuff[5])

            author_wealth_memes= mysqlfiles.users_get_points(message.author.id)[0]
            author_wealth_tokens = mysqlfiles.users_get_total_tokens(message.author.id)[0]


            if switch_type == 1:
                audiovisuaali.send(1, "State 1")
                if ((author_wealth_memes > do_stuff[2]) and (author_wealth_tokens > do_stuff[3])):

                        for role in message.server.roles:
                            if role.id == do_stuff[6]:
                                give_role_is = role
                        client.add_roles(message.author, give_role_is)
                        mysqlfiles.users_set_tokens_to_minus(str(do_stuff[3]), message.author.id)
                        mysqlfiles.users_set_points_to_minus(str(do_stuff[2]), message.author.id)
                        extra = "You have purchased role {}".format(give_role_is.name)
                        letter = generate_menu(message, client, arguments, 1, extra)
                else:
                    extra = "Get more currency"

                    letter = generate_menu(message, client, arguments, 0, extra)

                sent_1 = await client.send_message(message.channel, letter[0])

            elif switch_type == 2:

                audiovisuaali.send(1, "State 2")
                if ((author_wealth_memes > do_stuff[2]) or (author_wealth_tokens > do_stuff[3])):

                    mysqlfiles.users_set_points_to_plus(str(do_stuff[2]), message.author.id)
                    mysqlfiles.users_set_tokens_to_minus(1, message.author.id)

                    extra = "Item bought"
                    letter = generate_menu(message, client, arguments, 1, extra)


                else:
                    extra = "Get more memes"
                    letter = generate_menu(message, client, arguments, 0, extra)


                sent_1 = await client.send_message(message.channel, letter[0])


            # ITEM BUY TODO
            elif switch_type == 3:

                if author_wealth_memes < do_stuff[2]:
                    extra = "Get more memes!"
                    letter = generate_menu(message, client, arguments, 0, extra)
                    sent_1 = await client.send_message(message.channel, letter[0])


                else:

                    mysqlfiles.users_set_points_to_minus(str(do_stuff[2]), message.author.id)
                    mysqlfiles.users_set_tokens_to_plus(1, message.author.id)

                    extra = "item bought"
                    letter = generate_menu(message, client, arguments, 1, extra)

                    sent_1 = await client.send_message(message.channel, letter[0])


            else:
                error = "Your command was not identified!1"
                letter = generate_menu(message, client, arguments, 0, error)

                sent_1 = await client.send_message(message.channel, letter[0])



        else:
            error = "Your command was not identified!2"
            letter = generate_menu(message, client, arguments, 0, error)

            sent_1 = await client.send_message(message.channel, letter[0])
