from audiovisuaali import author_nickanme
from mysqlfiles import users_get_daily_points
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import points_stats_insert
from config import FISHING_INVENTORY as inventory
from asyncio import sleep as asleep
from random import randint

# Checking emoji reaction
def emoji_check(reaction, user):
    return reaction.emoji.startswith(('✅', '❌'))

# Fishing
async def fishing(message, client, arguments):

    # Getting name
    name = author_nickanme(message.author)

    # Sending message
    temporary = await client.send_message(message.channel, ":fishing_pole_and_fish: **| {} is fishing.... (wait)**".format(name))

    # Sleep for
    randomizer_sleep = randint(100, 300)
    await asleep(randomizer_sleep)

    # GET item rand
    randomizer_item = randint(0, 400)

    # What item
    if randomizer_item <= 10:
        spot = 0
    elif randomizer_item >= 10 and randomizer_item < 50:
        spot = 1
    else:
        spot = 2

    # Picking item randomly LUL
    hand = inventory[2][randint(0, len(inventory[0])-1)]

    # Sending message
    await client.delete_message(temporary)
    temporary_reaction = await client.send_message(message.channel, ":fishing_pole_and_fish: **| {}, you got {}! \n\nDo you want to sell it for: {} memes**".format(name, hand["name"], hand["value"]))

    # Add reactions
    for item_emoji in ["✅","❌"]:
        await client.add_reaction(temporary_reaction, item_emoji)

    # Wait for reaction
    react_result = await client.wait_for_reaction(user=message.author, timeout=30, check=emoji_check)

    # Del message
    await client.delete_message(temporary_reaction)

    # If wanting to sell
    try:
        if react_result.reaction.emoji.startswith("✅"):

            # Must get at this point because updates and optimization
            users_wealth = users_get_daily_points(message.author.id)[0]

            users_set_points_to_plus(hand["value"], message.author.id)
            points_stats_insert(message.server.id, message.author.id, 4, "Fishing", "", "", "+"+str(hand["value"]), "", hand["display_name"], "", "", "", 0, hand["value"], 0)
            msg = ":fishing_pole_and_fish: **| {}, you got: {} from fishing! \n\nYou sold it for: {} memes and now have {}**".format(name, hand["name"], hand["value"], users_wealth)

        # AFK or deny to sell
        else:
            msg = ":fishing_pole_and_fish: **| {}, you got {}, {} memes, but you chose to not sell it!**".format(name, hand["name"], hand["value"])
    except:
        msg = ":fishing_pole_and_fish: **| {}, you got {}, {} memes, but you chose to not sell it!**".format(name, hand["name"], hand["value"])

    # Send message
    await client.send_message(message.channel, msg)
