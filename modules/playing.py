import audiovisuaali
import config
from mysqlfiles import profile_id_get
import discord

# bot status playing
async def set_bot_playing(message, client, arguments):

    # User power level
    power = profile_id_get(message.author.id)

    # Setting playing if power level
    if not int(power[1]) >= 3:
        await client.send_message(message.channel, "**You don't have right to set bot status!**")

    else:
        await client.change_presence(game=discord.Game(name=arguments))

    return
