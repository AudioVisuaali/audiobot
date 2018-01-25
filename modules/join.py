import audiovisuaali
import mysqlfiles
# This is under contstruction _DASDAS
# TODO Not done yet
# Upcoming feature for lotto

async def raffle_lotto(message, client, arguments):


    return
    mysqlfiles.add_user_to_lotto(str(message.server.id),str(message.author.id))
    await client.send_message(message.channel, "You have entered lotto!")

"""    if
        if message.author.id == "149924169801269248":
            letter = "<@{}> has won the lotto with the pot"
            await client.send_message(message.channel, )

        else:
            await client.send_message(message.channel, "You don't have permissions to run this command")"""
