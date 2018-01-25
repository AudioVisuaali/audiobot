import audiovisuaali
import mysqlfiles
from audiovisuaali import how_many_seconds_until_midnight
# Under construction for lotto made from transfer taxes and casino taxes
# TODO::

# :thinking: D:_
async def tax_pot(message, client, arguments):

    # Getting how much the pot os worth
    pot = mysqlfiles.server_stats_tax_pot_get()[0]
    time_left = how_many_seconds_until_midnight()[1][:-7]
    print(time_left)

    # letter
    letter = ":moneybag: **| Pot is currently {} memes! Time left until pot opens: {}\nJoin by typing: __!join lotto__**".format(pot, time_left)

    # Sending message
    await client.send_message(message.channel, letter)

#TODO FINISH THIS UNDER CONTSTRUCTION
