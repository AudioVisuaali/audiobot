import discord
import asyncio
import pymysql
import mysqlfiles
from datetime import datetime, timedelta
import json

"""
This file is a fiasco
Nothing here isn't commented or explained clearly
This file is a dump file/ TODO later
Includes logging but logging should be in its own library
Clear this up later on
"""

# Wanted to test classes
class message_info:
    info = "[INFO]"
    user = "[USER]"
    error = "[FAIL]"
    timestamp = str("{:[%Y-%m-%d %H:%M:%S.%f}".format(datetime.now())[:-3]+"]")

# Create timestamp, This creation is a bit odd
def timestamp():
    asd = str("[{:%Y-%m-%d %H:%M:%S.%f}".format(datetime.now())[:-3]+"]")
    return asd

class bot_start_up_time:
    bot_start_up_time = datetime.now()


# DO NOT TOUCH CORE OF MANY COMMANDS
# Gives user instance
async def get_user_instance(message, search):

    # Checking for part of the name
    for member in message.server.members:
        if str(search).lower() in member.name.lower():
            return member

    # Checking for part of the nick
    for member in message.server.members:
        try:
            if str(search).lower() in member.nick.lower():
                return member
        except AttributeError:
            pass

    # Checking for users
    if search[:2] == "<@" and search[-1:] == ">" and search[2:-1].isnumeric():
        name = discord.utils.get(message.server.members, id=search[2:-1])
        return name

    # Checking for bots and selfnoti? and serverowner?
    if search[:3] == "<@!" and search[-1:] == ">" and search[3:-1].isnumeric():
        name = discord.utils.get(message.server.members, id=search[3:-1])
        return name

    if len(search) == 18 and search.isnumeric():
        name = discord.utils.get(message.server.members, id=search)
        return name

    return
"""
    f_way = client.get_user_info(search[2:-1])
    if f_way is None:
        f_way = client.get_user_info(search[3:-1])
        if f_way is None:
            return
        else:
            return f_way
    else:
        return f_way"""


#Logging
async def logging(message, client):

    # Values for inserting to logs
    info = []
    private = 0
    deleted = 0
    id_server = ""
    name = str(message.author)
    id_message = str(message.id)
    content = str(message.content)
    id_user = str(message.author.id)
    id_channel = str(message.channel.id)
    image = str(str(message.attachments)[1:-1]).replace("'", '"')

    # id_server & checks if message is private
    try:
        id_server = str(message.server.id)
    except AttributeError:
        id_server = ""
        private = 1

    # Image
    if len(image) > 30:
        image_link = json.loads(image)
        image = image_link["url"]
    else:
        image = ""

    # Query
    query = "INSERT INTO logging_messages (name, d_id, server_id, room_id, message_id, message, image, private, deleted) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"

    #info = (id_user, id_server, id_channel, content, image, private)
    info.append(name)
    info.append(id_user)
    info.append(id_server)
    info.append(id_channel)
    info.append(id_message)
    info.append(content)
    info.append(image)
    info.append(private)
    info.append(deleted)

    # Running query
    mysqlfiles.query(query, info)


def send(value, message):

    message = str(message.encode('utf-8'))[2:-1]

    if value == "info" or value == 1:
        help_type = message_info.info
    elif value == "user" or value == 2:
        help_type = message_info.user
    elif value == "error" or value == 3:
        help_type = message_info.error


    letter = timestamp() + help_type + " " + message
    print(letter)

def level_from_xp(level):
    if level > 40:
        level = 40
    #Scaling level BTW haHAA
    total = 2000 + 200*level
    return total

def level_xp(number):
    onoff = 1
    levl = 0
    while onoff == 1:
        result = level_from_xp(levl)
        if result > number:
            onoff = 0
            asd = []
            asd.append(levl)
            asd.append(number)
            asd.append(result)
            return asd
        number = number - result
        levl += 1

# Checks level :DDD
def level_check(message_author):

    info = mysqlfiles.get_xp_and_level_by_id(message_author)

    if info is None:
        return None
        
    xp = info[0]
    level = info[1]
    response = level_xp(xp)
    rlist = []

    if response[0] > level:
        das = mysqlfiles.users_set_level_to(response[0], message_author)
        rlist.append("1")
        rlist.extend(response)
        return(rlist)
    else:
        return("0")

#mess
def level_check_command(message_author):

    info = mysqlfiles.get_xp_and_level_by_id(message_author)

    xp = info[0]
    level = info[1]
    response = level_xp(xp)
    rlist = []

    rlist.append("1")
    rlist.extend(response)
    return(rlist)

# Seconds until midnight for lotto made out of taxes #this is weekly
# TODO Do this better, it's a mess atm
def how_many_seconds_until_midnight():
    """Get the number of seconds until midnight."""

    # Getting how many days untill sunday
    dd = 6 - datetime.now().weekday()

    # Calculating difference
    tomorrow = datetime.now() + timedelta(dd)

    # date
    sunday6pm = datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=18, minute=0, second=0)

    # difference
    return (sunday6pm - datetime.now()).seconds, str(sunday6pm - datetime.now())
