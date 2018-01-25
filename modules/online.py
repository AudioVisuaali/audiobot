from audiovisuaali import bot_start_up_time
from datetime import datetime
from math import floor as mfloor
from mysqlfiles import server_stats_restarts

# how long the server has been online
async def online(message, client, arguments):

    # Calc time
    time_now = datetime.now()
    asd = bot_start_up_time()
    time_in_seconds = mfloor((time_now - asd.bot_start_up_time).total_seconds())

    #time
    if time_in_seconds < 60:
        asd = str(time_in_seconds) + " seconds"
    elif time_in_seconds < 3600:
        asd = str(mfloor(time_in_seconds/60)) + " minutes"
    elif time_in_seconds < 86400:
        asd = str(mfloor(time_in_seconds/3600)) + " hours"
    elif time_in_seconds < 604800:
        asd = str(mfloor(time_in_seconds/86400)) + " days"
    elif time_in_seconds < 2419200:
        asd = str(mfloor(time_in_seconds/604800)) + " weeks"
    elif time_in_seconds >= 2419200:
        asd = str(mfloor(time_in_seconds/2419200)) + " months"

    # sending message ///UNDER CONSTRUCTION
    asdaa = server_stats_restarts()
    await client.send_message(message.channel, ":clock10: **| bot has been online for " + asd + " and has been restarted " + asdaa + " times**")

    #TODO MAKE THIS BETTER LMAO
    #TODO MAKE THIS BETTER LMAO
    #TODO MAKE THIS BETTER LMAO
    #TODO MAKE THIS BETTER LMAO
    #TODO MAKE THIS BETTER LMAO
    #TODO MAKE THIS BETTER LMAO
