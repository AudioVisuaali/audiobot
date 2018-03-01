print("Starting...")
from mysqlfiles import points_users_memes_add_on_message
from mysqlfiles import points_users_xp_add_on_message
from mysqlfiles import message_last_interval_seconds
from mysqlfiles import get_users_lowest_bank_amount
from mysqlfiles import on_member_remove_room_id
from mysqlfiles import user_status_and_playing
from mysqlfiles import points_users_points_add
from mysqlfiles import user_add_points_in_bank
from mysqlfiles import on_member_join_room_id
from mysqlfiles import get_users_bank_amount
from mysqlfiles import points_users_new_add
from mysqlfiles import points_stats_insert
from mysqlfiles import user_nicknames_add
from mysqlfiles import message_add
from config import SELECT_TIME_RAFFLE as raffle_selection_time
from config import SELECT_DAY_RAFFLE as raffle_selection_day
from config import COMMAND_START as command_starts_with
from config import BOT_TOKEN as bot_token
from config import MESSAGE_POST_LEVEL_ACHIEVEMENT
from config import MESSAGE_COMMAND_POINTS_MAX
from config import MESSAGE_COMMAND_POINTS_MIN
from config import MESSAGE_COMMAND_MEMES_MAX
from config import MESSAGE_COMMAND_MEMES_MIN
from config import MESSAGE_POINTS_MAX
from config import MESSAGE_POINTS_MIN
from config import BANK_INTEREST_TIME
from config import BANK_INTEREST_DAY
from config import MESSAGE_MEMES_MIN
from config import MESSAGE_MEMES_MAX
from audiovisuaali import select_random_user_from_lotto_by_server_by_week
from audiovisuaali import global_cd_list_per_command
from audiovisuaali import logging as chat_logging
from audiovisuaali import time_until_wanted_time
from audiovisuaali import time_format_new
from audiovisuaali import get_format_time
from audiovisuaali import get_room_by_id
from audiovisuaali import level_check
from audiovisuaali import total_weeks
from audiovisuaali import send
from modules.ao_ruoka import get_food_for_main
from discord import Client as Discord_Client
import logging
from asyncio import sleep as asleep
from random import randint
from math import ceil as mceil
import modules
import dirmap

# logging
LOG_FILENAME = 'error_log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.WARNING)

# Client
client = Discord_Client()

# CONNECTION TO SERVER
@client.event
async def on_ready():

    send(1, "Logged in as: {}".format(client.user.name))
    send(1, "Client ID: {}".format(client.user.id))
    send(1, "Listening to the chat!")


# Message when member joins
@client.event
async def on_member_join(member):

    # Getting room
    room_id = on_member_join_room_id()[0]

    # If room exists
    if room_id:
        server = member.server
        fmt = 'Welcome {0.mention} to {1.name}!'
        channel = client.get_channel(room_id)
        await client.send_message(channel, fmt.format(member, server))
        #discord.Object(id='channel_id_here')
    # Room doesn't exist
    else:
        send(1, "Member joined but joined room is not defined!")


# Message when member Leaves
@client.event
async def on_member_remove(member):

    # Getting room
    room_id = on_member_remove_room_id()[0]

    # If room exists
    if room_id:
        server = member.server
        fmt = 'Member {0.mention} left {1.name}!'
        channel = client.get_channel(room_id)
        await client.send_message(channel, fmt.format(member, server))

    # Room doesn't exist
    else:
        send(1, "Member removed but remove room is not defined!")
        #discord.Object(id='channel_id_here')


@client.event
async def on_member_update(before, after):


    # Adding nickname
    if before.nick != after.nick:

        send(1, "Adding nick for {}".format(before.name))

        user_nicknames_add(before.server.id, after.id, after.nick)

    # Adding game or status
    if (before.game != after.game) or (before.status != after.status):

        # Add info
        send(1, "Updating game for {}".format(before.name))

        # Checking game status
        try:
            game_before = before.game.name
        except:
            game_before =""

        # Checking game status
        try:
            game_after = after.game.name
        except:
            game_after = ""

        # Checking game type
        # 0 = no stream
        # 1 = streaming
        try:
            game_type = after.game.type
        except:
            game_type = 0

        # If bad name format don't add name (id still saved)
        try:
            user_status_and_playing(before.server.id, after.id, str(before), game_before, game_after, game_type, str(before.status), str(after.status))
        except:
            try:
                user_status_and_playing(before.server.id, after.id, "", game_before, game_after, game_type, str(before.status), str(after.status))
            except:
                send(3, "Bad format can't add to database")
    return


# CHAT LISTENER
@client.event
async def on_message(message):

    try:
        # Printing to the terminal
        command_line = message.author.name + " >> " + message.content
        send(2, command_line)

        # Logging
        await chat_logging(message, client)

        ########## Adding points
        # How much points we want to add
        if message.content.startswith("!"):
            memes_amount = randint(MESSAGE_COMMAND_MEMES_MIN, MESSAGE_COMMAND_MEMES_MAX)
            xp_amount = randint(MESSAGE_COMMAND_POINTS_MIN, MESSAGE_COMMAND_POINTS_MAX)
        else:
            memes_amount = randint(MESSAGE_MEMES_MIN, MESSAGE_MEMES_MAX)
            xp_amount = randint(MESSAGE_POINTS_MIN, MESSAGE_POINTS_MAX)

        # Checking when last message was sent
        recent_messages = message_last_interval_seconds(message.author.id)

        # Adding points if X amount has passed with no message
        if recent_messages == None:
            points_users_xp_add_on_message(xp_amount, message.author.id)
            points_users_memes_add_on_message(memes_amount, message.author.id)

        # Something ? logging?
        message_add(str(message.author.id), "", "Sent")

        # Checking for levels
        levels = level_check(message.author.id)
        if levels is None:
            pass
        elif levels[0] == "1":
            if MESSAGE_POST_LEVEL_ACHIEVEMENT:
                await client.send_message(message.channel, str(message.author) + "you are now level "+ str(levels[1]))
            pass

        # Check if message is from bot to prevent loop
        if message.author.id == client.user.id:
            return

        # Cooldown for modules for client for not server
        cooldown_module = global_cd_list_per_command()

        ###### COMMAND SECTION #####

        # If not starting with "!" stopping the check
        if not message.content.startswith(command_starts_with):
            return

        # Getting issued command (and args)
        args = message.content.replace(command_starts_with,"",1).split(" ",1)

        # Cleaning info
        command = args[0]

        # If function isn't found in the map -> Get from database if exist
        if not args[0] in dirmap.dirmap:

            #Not in the list
            arguments = args[0]

            # if user can't use the command
            if cooldown_module.global_get_items(message.author.id, "command_retrieve"):
                return

            # Adding to cd list and running the command
            cooldown_module.global_add_item(message.author.id, "command_retrieve")
            await getattr(modules, "command_retrieve")(message, client, arguments)
            send(2, "Done with {}".format("command_retrieve"))

            # Sleeping and removing cd
            await asleep(1.0)
            cooldown_module.global_remove_item(message.author.id, "command_retrieve")
            return

        ##### Commands with no multiple arguments #####

        command_args = dirmap.dirmap[args[0]]["args"]
        command_function = dirmap.dirmap[args[0]]["function"]

        # Checking if delimeter in None
        if command_args["delimeter"] is None:

            #checking if command has the same amount of arguments compared to dirmap
            if (len(args)-1) in command_args["length"]:

                # if length is 0 in config setting args to " ", because assuming args[1] is non existance
                arguments = ""

                # if length is 1 then not splitting, but passing the text input
                if 1 in command_args["length"]:
                    arguments = args[1]

                # if user can't use the command
                if cooldown_module.global_get_items(message.author.id, command_function):
                    return

                # Adding to cd list and running the command
                cooldown_module.global_add_item(message.author.id, command_function)
                await getattr(modules, command_function)(message, client, arguments)
                send(2, "Done with {}".format(command_function))

                # Sleeping and removing cd
                await asleep(1.0)
                cooldown_module.global_remove_item(message.author.id, command_function)
                return

            # If command doesn't fill requests it's a bad request
            send(2, "Bad request from user")
            return

        ###### Commands with delimeter #####

        # Checking if delimeter exists
        if (not command_args["delimeter"] is None):

            # Settingm command to "" if arguments are not set by requester
            arguments = ""

            # Checking if arguments are set
            if len(args) > 1:
                arguments = args[1].split(command_args["delimeter"],command_args["split"])

            # Checking length for right input
            if len(arguments) in command_args["length"]:


                # if user can't use the command
                if cooldown_module.global_get_items(message.author.id, command_function):
                    return

                # Adding to cd list and running the command
                cooldown_module.global_add_item(message.author.id, command_function)
                await getattr(modules, command_function)(message, client, arguments)
                send(2, "Done with {}".format(command_function))

                # Sleeping and removing cd
                await asleep(1.0)
                cooldown_module.global_remove_item(message.author.id, command_function)
                return

        # IF nothing matches = bad request
        send(2, "Bad request from user")
        return

    # Failure
    except Exception as e:

        # logging
        send(3, "Something terrible happened! Check the log file!")
        logging.exception("message")

# TODO CHECK IF USER IN DATABSE IF NOT -> ADD USER, ELSE IGNORE # THIS IS NOT NEEDED IF THAT IS DONE
# For gathering points
async def add_users_new():

    # Checking if client is ready and online
    await client.wait_until_ready()
    while not client.is_closed:
        info = []
        count = 0

        # Going through users
        for server in client.servers:
            for Member in server.members:
                # Adds info to the list
                info.append(Member.id)
                info.append("")# TODO changed to cause id is identifier and name is not needed
                count += 1

        # Creating and executing query
        if len(info) < 2:
            send(1, "Your bot is so dead that it doesn't even have users to check OMG")
            return

        # Creating query and adding users
        query = "INSERT IGNORE INTO points_and_xp (d_id, name) VALUES {} ON DUPLICATE KEY UPDATE d_id=d_id;".format(','.join(['(%s,%s)'] * count))
        points_users_new_add(query, info)

        # sleeping for 60 seconds before running task again
        await asleep(60)

async def post_ao_food_to_channel():

    # Checking if client is ready and online
    await client.wait_until_ready()
    while not client.is_closed:

        # getting time until
        get_this_D = time_until_wanted_time(hour=8, minute=30)
        send(1, "{} seconds until posting food!".format(get_this_D))

        # Getting channel
        get_this_C = await get_room_by_id(client, "279619091055116291", "280756814956724244")
        #get_this_C = await get_room_by_id(client, "279619091055116291", "356423300353884160")
        # Sleeping so it hits the time target

        await asleep(get_this_D)

        # Sending message
        kek = get_food_for_main()
        if kek is not None:
            await client.send_message(get_this_C, kek)
    return

async def post_lotto_winner():

    # Checking if client is ready and online
    await client.wait_until_ready()
    while not client.is_closed:

        keepo = time_format_new(raffle_selection_day, raffle_selection_time)
        send(1, "Sleeping for {} before Lotto!".format(keepo))
        await asleep(keepo)

        # Get current week
        week = total_weeks()

        # TODO DEFINE SERVER
        winner_chicken_dinner = await select_random_user_from_lotto_by_server_by_week(client, "279619091055116291", week)

        # Do something when user is chosen
        print(winner_chicken_dinner.name)

async def bank_interest():

    # Checking if client is ready and online
    await client.wait_until_ready()
    while not client.is_closed:

        # Day, time(s) days start @ 0
        sleep_this = time_format_new(BANK_INTEREST_DAY, BANK_INTEREST_TIME)
        send(2, "Interest in {}".format(sleep_this))
        await asleep(sleep_this)

        users = []

        # Mode_id=10, time="604800", time_type="SECOND"
        bank_update = get_users_lowest_bank_amount(10, "604800")
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
                    points_stats_insert(message.server.id, row[0], 11, "Interest", "", "", "+"+str(add_this_memes), "", "Interest", "", "", "", 0, add_this_memes, 0)

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
                points_stats_insert(message.server.id, kek[0], 11, "Interest", "", "", "+"+str(add_this_memes), "", "Interest", "", "", "", 0, add_this_memes, 0)

# Loops :)
client.loop.create_task(add_users_new())
client.loop.create_task(post_lotto_winner())
client.loop.create_task(post_ao_food_to_channel())
client.loop.create_task(bank_interest())

# RUNS THE BOT
if __name__ == "__main__":
    client.run(bot_token)
