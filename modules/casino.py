#import audiovisuaali
from mysqlfiles import events_get_state_casino
from mysqlfiles import events_change_state_casino
from config import OWNER_ID as owners
# TODO NOT DONE :DDDD and importing too much extra
# This is still under contstuction
# This allows casino to be toggled on off later on
# This can also be automated

async def casino(message, client, argumets):

    # Checking if the user has enough powers to run the command
    if message.author.id not in owners:
        return

    info = mysqlfiles.events_get_state_casino()

    if info[0] == 0:
        mysqlfiles.events_change_state_casino(1)
        print("aaa")
        letter = "**=========================================\n           :game_die:  | CASINO HAS BEEN OPENED!! | :game_die:\n\nYou have a change to get more when you are gambling!\nYou can access shop!\n\nOnly open for limited time! :point_right:  :ok_hand: :fire: :100:\n=========================================**"
        await client.send_message(message.channel, letter)

        #TODO: Room hide info[1] is room id
        pass

    elif info[0] == 1:
        print("sss")
        mysqlfiles.events_change_state_casino(0)
        letter = "asdasd"
        #letter = "**=========================================\n           :game_die:  | CASINO HAS BEEN OPENED!! | :game_die:\n\nYou have a change to get more when you are gambling!\nYou can access shop!\n\nOnly open for limited time! :point_right:  :ok_hand: :fire: :100:\n=========================================**"
        await client.send_message(message.channel, letter)
        pass
