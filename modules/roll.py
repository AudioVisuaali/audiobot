#import audiovisuaali
from random import randint
from mysqlfiles import stats_roll_get_previous
from mysqlfiles import users_set_tokens_to_plus
from mysqlfiles import users_set_points_to_plus
from mysqlfiles import stats_roll_add

#roll (Rolls a random number between 0-100 if special arguments are not given)
async def roll(message, client, arguments):

    first_slot = [0,1,2,3,4,5,6,7,8,9,""]
    second_slot =[0,1,2,3,4,5,6,7,8,9]
    first = str(first_slot[randint(0, 10)])
    second = str(second_slot[randint(0, 9)])
    token, meme, double, memes, tokens = "", "", False, 0, 0

    # Checking if double
    if first == second:
        double = True

    # Getting roll history
    previous = stats_roll_get_previous(message.author.id, 10)

    # Cheking if double, no history(for abuse)
    if first == second:
        if not previous:

            # Add tokens
            if randint(0,1000) == 342: # one in 10000
                tokens = 1
                users_set_tokens_to_plus(tokens, message.author.id)
                meme = " | You have won a token from roll!".format(memes)


            # Add memes
            if randint(1,5) == 2:
                memes = 10
                users_set_points_to_plus(memes, message.author.id)
                token = " | You have won a {}memes from roll!".format(memes)

    # Add roll stats
    stats_roll_add(message.author.id, first, second, double, memes, tokens)

    # Formatting and sending message
    letter = "**{}{}{}{}**".format(first, second, token, meme)
    await client.send_message(message.channel, "<@"+message.author.id+"> "+letter)
    return
