from audiovisuaali import send
from audiovisuaali import global_cd_list_per_command
from time import time

from config import OWNER_ID as owners


async def purge(message, client, arguments):

    # Starting time
    start_time = time()

    # Checking admin provileges
    if message.author.id not in owners:
        return

    # Roulette cd
    cooldown_lists_all = global_cd_list_per_command()

    # Calculating total items
    option = cooldown_lists_all.global_reset_list(message.author.id)

    # Runtime
    Runtimeme = time()-start_time

    # Send message
    await client.send_message(message.channel, ":fire: **| Purged {} items! Took: {} seconds   **".format(option, time()-start_time))
