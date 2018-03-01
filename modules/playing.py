from audiovisuaali import send
from config import OWNER_ID as owners
from discord import Game
# bot status playing
async def set_bot_playing(message, client, arguments):

    if message.author.id not in owners:
        return
    else:
        await client.change_presence(game=Game(name=arguments))
        send(1, "Updating playing status!")
    return
