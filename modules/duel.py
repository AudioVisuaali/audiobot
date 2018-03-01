from audiovisuaali import send
from audiovisuaali import get_user_instance
from mysqlfiles import users_get_daily_points
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import users_set_points_to_minus
from mysqlfiles import points_stats_insert
from asyncio import sleep as asleep
from random import randint


# Duel for 2 users
async def duel(message, client, arguments):

    owner = message.author
    #!
    slave = await get_user_instance(message, arguments[0])

    # Owner name
    if owner.nick is None:
        owner_name = owner.name
    else:
        owner_name = owner.nick

    # Slave name
    if slave.nick is None:
        slave_name = slave.name
    else:
        slave_name = slave.nick

    # Checking currency
    if not arguments[1].isdigit():
        no_currency = "**:crossed_swords: | {}, invalid amount of currency!**".format(owner_name)
        await client.send_message(message.channel, no_currency)
        return

    # Checking if dueling self
    #if owner.id == slave.id:
    #    await client.send_message(message.channel, "**:crossed_swords: | {}, you can't duel yourself!**".format(owner_name))
    #    return

    # Checking if duleing bots
    if slave.bot:
        no_bot_duel = "**:crossed_swords: | {} you can't duel bots!**".format(owner_name)
        await client.send_message(message.channel, no_bot_duel)
        return

    # Getting stats
    owner_points = users_get_daily_points(owner.id) #user1
    slave_points = users_get_daily_points(slave.id) #user2

    # Users do not have enough points to gamble
    if (int(arguments[1]) > int(owner_points[0])) or (int(arguments[1]) > int(slave_points[0])):
        more_points = "**:crossed_swords: | {} get some more points! :thinking:**".format(slave_name)
        await client.send_message(message.channel, more_points)
        return

    # Checking if dueling with less than 10 currency
    if int(arguments[1]) < 10:
        no_memes = "**:crossed_swords: | {} you have to duel atleast 10 memes!**".format(owner_name)
        await client.send_message(message.channel, no_memes)
        return

    # Sending challenge message for dueller
    keepo = "<@{}> You have been **challenged** by **{}** for **{}** memes, you have **20** seconds to accept the duel by typing \n!accept <@{}> or !decline".format(slave.id, owner_name,arguments[1], owner.id)
    message_send = await client.send_message(message.channel, keepo)


    # Waiting for confirmation
    def guess_check(m):
        print(m.content)
        print(message.author.id)
        if str(message.author.id) in m.content:

            return True
        else:
            return False

    # Waiting response form
    guess = await client.wait_for_message(timeout=20.0, author=slave, check=guess_check)

    # Checking if challnged responded
    if guess is None:
        no_response = "**:crossed_swords: | {} did not response to the duel!**".format(slave_name)
        await client.edit_message(message_send, no_response)
        return

    # Checking if challenged accepts
    else:

        if guess.content.startswith("!decline"):
            await client.delete_message(kappa)
            await client.send_message(message.channel, "**:crossed_swords: | {} declined to the duel!**".format(slave_name))
            return

        # Sending message for rolling and deleting a message for clearness
        await client.delete_message(message_send)
        msg = await client.send_message(message.channel, "<:reeee:312321001398730762> **Rolling**")
        await asleep(1.5)
        letter = ""

        #player 1 wins
        if randint(0, 99) < 50:
            # Message content
            print(arguments[1])
            letter = "**:crossed_swords: | {} won {} memes!**"''.format(owner_name, str(int(arguments[1])*2))
            points_stats_insert(message.server.id, message.author.id, 3, "Duel", arguments[1], "", "+"+arguments[1], "", slave_name, "", "", "", 0, int(arguments[1]), 0)
            points_stats_insert(message.server.id, slave.id, 3, "Duel", arguments[1], "", "-"+arguments[1], "", owner_name, "", "", "", 0, 0, int(arguments[1]))
            # Adding/removing points
            users_set_points_to_plus(arguments[1], message.author.id)
            users_set_points_to_minus(arguments[1], slave.id)


        # Player 2 wins
        else:
            # Message content
            print(arguments[1])
            letter = "**:crossed_swords: | {} won {} memes!**"''.format(slave_name, str(int(arguments[1])*2))
            points_stats_insert(message.server.id, message.author.id, 3, "Duel", arguments[1], "", "-"+arguments[1], "", slave_name, "", "", "", 0, 0, int(arguments[1]))
            points_stats_insert(message.server.id, slave.id, 3, "Duel", arguments[1], "", "+"+arguments[1], "", owner_name, "", "", "", 0, int(arguments[1]), 0)
            # Adding/removing points
            users_set_points_to_plus(arguments[1], arguments[1][2:-1])
            users_set_points_to_minus(arguments[1], message.author.id)


        # Posting the result in chat
        await client.edit_message(msg, letter)
