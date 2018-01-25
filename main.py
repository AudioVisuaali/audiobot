# Importing modules
from discord import Client as DClient
from asyncio import sleep as asleep
from random import randint

# IMPORTINGMINIGAMES AND MODULES +(CONFIG)
from config import COMMAND_START as command_starts_with
from config import BOT_TOKEN as bot_token

#misc
from audiovisuaali import level_check
from audiovisuaali import send
from audiovisuaali import logging
from audiovisuaali import how_many_seconds_until_midnight

# Commands impot *
import modules
import dirmap

# Client
client = DClient()

# Connecting to database
send(1, "Trying to connect to database")
import mysqlfiles
send(1, "Trying connect to the discord server!")

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
    room_id = mysqlfiles.on_member_join_room_id()[0]

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
    room_id = mysqlfiles.on_member_remove_room_id()[0]

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

        mysqlfiles.user_nicknames_add(before.server.id, after.id, after.nick)

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
            mysqlfiles.user_status_and_playing(before.server.id, after.id, str(before), game_before, game_after, game_type, str(before.status), str(after.status))
        except:
            try:
                mysqlfiles.user_status_and_playing(before.server.id, after.id, "", game_before, game_after, game_type, str(before.status), str(after.status))
            except:
                send(3, "Bad format can't add to database")
    return


# CHAT LISTENER
@client.event
async def on_message(message):

    # Printing to the terminal
    command_line = message.author.name + " >> " + message.content
    send(2, command_line)

    # Logging
    await logging(message, client)

    ########## Adding points
    # How much points we want to add
    xp_amount = randint(15,25)
    memes_amount = 1
    if message.content.startswith("!"):
        memes_amount = 2
        xp_amount = randint(5,15)
    # Checking when last message was sent
    recent_messages = mysqlfiles.message_last_interval_seconds(message.author.id)

    # Adding points if X amount has passed with no message
    if recent_messages == None:
        mysqlfiles.points_users_xp_add_on_message(xp_amount, message.author.id)
        mysqlfiles.points_users_memes_add_on_message(memes_amount, message.author.id)

    mysqlfiles.message_add(str(message.author.id), "", "Sent")

    # Checking for levels
    levels = level_check(message.author.id)
    if levels is None:
        pass
    elif levels[0] == "1":
        #await client.send_message(message.channel, str(message.author) + "you are now level "+ str(levels[1]))
        pass

    # Check if message is from bot to prevent loop
    if message.author.id == client.user.id:
        return

    ########################
    # COMMAND SECTION
    # PLEASE DON'T TOUCH THIS

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
        await getattr(modules, "command_retrieve")(message, client, arguments)
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

            #Calling function with arguments
            await getattr(modules, command_function)(message, client, arguments)
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

            # executing command
            await getattr(modules, command_function)(message, client, arguments)
            return
    # IF nothing matches = bad request
    send(2, "Bad request from user")
    return


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
                info.append(str(Member.id))
                info.append(str(""))# TODO changed to cause id is identifier and name is not needed
                count += 1

        # Creating and executing query
        if len(info) < 2:
            send(1, "No users")
            return
        query = str("INSERT IGNORE INTO points_and_xp (d_id, name) VALUES " + ','.join(['(%s,%s)'] * count) + " ON DUPLICATE KEY UPDATE d_id=d_id;")
        mysqlfiles.points_users_new_add(query, info)

        # sleeping for 60 seconds before running task again
        await asleep(60)


# For gathering xp
async def add_users_xp():

    # Checking if client is ready and online
    await client.wait_until_ready()
    while not client.is_closed:

        # Lists for users
        onepoint, twopoint, trepoint = [], [], []

        # Going through users
        for server in client.servers:
            for Member in server.members:
                mstatus = str(Member.status)
                currentgameplaying = str(Member.game)
                if currentgameplaying == None:
                    currentgameplaying = "None"

                # Checking status
                if mstatus == "online" or mstatus == "dnd" or mstatus == "do_not_disturb" or mstatus == "invisible":
                    trepoint.append(str(Member.id))

                elif mstatus == "idle":
                    twopoint.append(str(Member.id))

                elif mstatus == "offline":
                    onepoint.append(str(Member.id))

        # Adding xp for offline people
        if len(onepoint) > 0:
            onequery = "UPDATE points_and_xp SET xp = xp+1 WHERE d_id IN (" + ','.join(["%s"]*len(onepoint)) + ");"
            one = mysqlfiles.points_users_xp_add(onequery, onepoint)

        # Adding xp for away people
        elif len(twopoint) > 0:
            twoquery = "UPDATE points_and_xp SET xp = xp+2 WHERE d_id IN (" + ','.join(["%s"]*len(twopoint)) + ");"
            two = mysqlfiles.points_users_xp_add(twoquery, twopoint)

        # Adding xp for online people
        elif len(trepoint) > 0:
            trequery = "UPDATE points_and_xp SET xp = xp+3 WHERE d_id IN (" + ','.join(["%s"]*len(trepoint)) + ");"
            tre = mysqlfiles.points_users_xp_add(trequery, trepoint)

        # sleeping for 60 seconds before running task again
        await asleep(60)


# For gathering points
async def add_users_points():

    # Checking if client is ready and online
    await client.wait_until_ready()
    while not client.is_closed:

        # Query for adding 1 point per minute
        onequery = "UPDATE points_and_xp SET points = points+1, available_points = available_points+1;"
        one = mysqlfiles.points_users_points_add(onequery)

        #Sleeping for 1 minute
        await asleep(60)

# For gathering points
async def tax_pot_def():

    # Checking if client is ready and online
    await client.wait_until_ready()
    while not client.is_closed:

        # Query for adding 1 point per minute
        onequery = "UPDATE points_and_xp SET points = points+1, available_points = available_points+1;"
        one = mysqlfiles.points_users_points_add(onequery)

        #Sleeping for 1 minute
        await asleep(60)

#client.loop.create_task(add_users_xp()) # Bad way to record stats :/ (But it works :D)
#client.loop.create_task(add_users_points()) # Also bad way to record stats :/ (But it works :D)
client.loop.create_task(add_users_new())

# RUNS THE BOT
client.run(bot_token)
