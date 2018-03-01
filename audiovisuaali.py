import discord
import asyncio
import pymysql
import mysqlfiles
from datetime import datetime, timedelta
import json
from math import floor as mfloor
from random import randint
from mysqlfiles import lotto_get_users_by_server_by_week
"""
This file is a fiasco
Nothing here isn't commented or explained clearly
This file is a dump file/ TODO later
Includes logging but logging should be in its own library
Clear this up later on
"""

# All cooldown for commands specified
class global_cd_list_per_command():

    # Bot start up time
    bot_start_up_time = datetime.now()

    global_command_list = []

    # RESET pos-1 for this commands stat
    def global_reset_list(self, user):
        pos = 0
        for stat in self.global_command_list:
            pos += 1
            if not stat == user+":purge":
                self.global_command_list.remove(stat)
        return pos-1

    # Get stat
    def global_get_items(self, user, module):
        if user+":"+module in self.global_command_list:
            return True
        else:
            return False

    # Add stat
    def global_add_item(self, user, module):
        self.global_command_list.append(user+":"+module)

    # Remove stat
    def global_remove_item(self, user, module):
        self.global_command_list.remove(user+":"+module)


# Create timestamp, This creation is a bit odd
def timestamp():
    asd = str("[{:%Y-%m-%d %H:%M:%S.%f}".format(datetime.now())[:-3]+"]")
    return asd

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

    # By id
    if len(search) == 18 and search.isnumeric():
        name = discord.utils.get(message.server.members, id=search)
        return name

    return

async def get_user_instance_by_id(client, d_id):

    for server in client.servers:
        for member in server.members:
            if member.id == d_id:
                return member

def author_nickanme(author):

    if author.nick is None:
        return author.name
    else:
        return author.nick

async def select_random_user_from_lotto_by_server_by_week(client, server_id, week):

    all_users_in_lotto = lotto_get_users_by_server_by_week(server_id, week)
    pos = randint(0, len(all_users_in_lotto)-1)

    chosen_one = all_users_in_lotto[0][pos]
    user_instance = await get_user_instance_by_id(client, chosen_one)
    return user_instance


async def get_room_by_id(client, server_id, room_id):

    for server in client.servers:
        if server.id == server_id:
            for channel in server.channels:
                if channel.id == room_id:
                    return channel

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

def get_format_time():

    return str("{:[%Y-%m-%d %H:%M:%S.%f}".format(datetime.now())[:-3]+"]")
def send(value, message):

    message = str(message.encode('utf-8'))[2:-1]

    if value == "info" or value == 1:
        help_type = "[INFO]"
    elif value == "user" or value == 2:
        help_type = "[USER]"
    elif value == "error" or value == 3:
        help_type = "[FAIL]"


    letter = str("{:[%Y-%m-%d %H:%M:%S.%f}".format(datetime.now())[:-3]+"]") + help_type + " " + message
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



#TODO cleanup to def's and stuff all time stuff in time class in audiovisuaali -> then must fix all the other fiesl that use time def's

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


def time_untill_midnight():

    # Time now
    time_now = datetime.today()

    # Time to Running
    time_to_run = time_now.replace(day=time_now.day, hour=8, minute=30, second=0, microsecond=0)

    time_at_the_start_of_this_day = time_now.replace(day=time_now.day, hour=0, minute=0, seconds=0, microsecond=0)

    return

def time_until_next_day_and_time_weekly(day=7, hour=18, minute=0):
    return


def time_until_wanted_time(hour=0, minute=0, second=0, microsecond=0):

    # Time now
    time_now=datetime.today()

    # Time
    time_run = time_now.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    start_of_this_day = time_now.replace(hour=0, minute=0, second=0, microsecond=0)

    # This day so far
    delta_t = time_now - start_of_this_day

    # time from start of the day to runing this program
    delta_c = time_run - start_of_this_day

    # Checking if past the wanted time
    if (delta_c.seconds - delta_t.seconds) < 0:
        this = 86400 - (delta_t.seconds - delta_c.seconds)

    # Sleep here for X :)) vähemmän kuin haluttu aika
    else:
        this = delta_c.seconds - delta_t.seconds

    return this+1

def day_splitted_by_time(in_seconds):
        # how many days until epoch
        epoch = datetime.utcfromtimestamp(0)
        now = datetime.today()
        d = now - epoch

        # time until X time in day
        time_start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        time_diff = now - time_start_of_today

        # Removing day if not reached time yet
        if time_diff.seconds > in_seconds:
            return d.days
        else:
            return d.days - 1

# Offset Epoch started on thrusday so offset=3
def total_weeks(offset=3):

    # Calculating time from epoch
    epoch_start = datetime.utcfromtimestamp(0)
    now = datetime.today()
    delta = now - epoch_start

    # calculating week with offset and returning it
    week_amount = mfloor((delta.days+offset)/7)
    return week_amount


def time_now_today_seconds_so_far():

    now = datetime.today()
    time_start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - time_start_of_today

    return delta.seconds

def time_format_new(day, seconds):

    now = datetime.today()

    # Weekday in number foramt
    total_seconds_this_week_so_far = (now.weekday())*86400 + time_now_today_seconds_so_far()

    # current time ahead
    if ((day * 86400) + seconds) < total_seconds_this_week_so_far:
        return 604800 - (total_seconds_this_week_so_far - (day*86400 + seconds))

    # current time behind now behind
    else:
        return ((day * 86400) + seconds) - total_seconds_this_week_so_far
