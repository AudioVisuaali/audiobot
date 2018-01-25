import audiovisuaali
from random import randint

#TEST
async def test(message, client, arguments):

    on_going = True
    try:
        gamble_amount = arguments[0]
    except:
        gamble_amount = 0

    mini_icon = [":spades:", ":clubs:", ":hearts:", ":diamonds:"][randint(0,3)]
    letter = "{} **| You have started a blackjack game!".format(mini_icon)
    letter += "\nGambling for {} points!".format(gamble_amount)




    letter += "**"
    msg = await client.send_message(message.channel, letter)
    await client.add_reaction(msg, "\U0001f195") #🆕
    await client.add_reaction(msg, "\U0001f197") #🆗
    await client.add_reaction(msg, "\U0001f500") #🔀
    await client.add_reaction(msg, "\U0001f1eb") #🇫


    await client.add_reaction(msg, ["regional_indicator_a", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "regional_indicator_j", "regional_indicator_q", "regional_indicator_k"]) #🇫

#[":regional_indicator_a:", ":two:", "three", "four", "five", "six", "seven", "eight", "nine", "ten", ":regional_indicator_j:", ":regional_indicator_q:", ":regional_indicator_k:"]

#:regional_indicator_a: :two:  :three:  :four: :five: :six: :seven: :eight: :nine: :keycap_ten: :regional_indicator_j: :regional_indicator_q: :regional_indicator_k:
    #while on_going:
#msg = await client.send_message(message.channel, 'React with thumbs up or thumbs down.')
#res = await client.wait_for_reaction(['👍', '👎'], message=msg)
#        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
#add_reaction(message, emoji)
