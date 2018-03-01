from audiovisuaali import send
from random import randint
from random import shuffle

def create_deck():
    return

# Checking emoji reaction
def emoji_check(reaction, user):
    return reaction.emoji.startswith(("🆙", "🔄", "✅"))

def calculate_value_in_hand(hand):

    print(hand)
    card_values = [{":two:": 2, ":three:": 3, ":four:": 4, ":five:": 5, ":six:": 6, ":seven:": 7, ":eight:": 8, ":nine:": 9, ":keycap_ten:": 10, ":regional_indicator_j": 10, ":regional_indicator_q": 10, ":regional_indicator_k": 10, ":regional_indicator_a:": 11}]
    total = 0

    for card in hand:
        total += card_values[0][card]

    if total > 21:
        total = 0
        if card == ":regional_indicator_a":
            total += 1
        else:
            total += card_values[card]

        if total > 21:
            return total# TODO BUST

        else:
            return total


async def black_jack(message, client, arguments):


    deck = [":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:", ":regional_indicator_j:", ":regional_indicator_q:", ":regional_indicator_k:", ":regional_indicator_a:",":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:", ":regional_indicator_j:", ":regional_indicator_q:", ":regional_indicator_k:", ":regional_indicator_a:",":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:", ":regional_indicator_j:", ":regional_indicator_q:", ":regional_indicator_k:", ":regional_indicator_a:",":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:", ":regional_indicator_j:", ":regional_indicator_q:", ":regional_indicator_k:", ":regional_indicator_a:"]

    playing_bj = True
    hand_dealer = []
    hand_player = []

    shuffle(deck)
    hand_dealer.append(deck.pop())
    shuffle(deck)
    hand_player.append(deck.pop())
    shuffle(deck)
    hand_dealer.append(deck.pop())
    shuffle(deck)
    hand_player.append(deck.pop())

    while playing_bj:
        letter = "**DEALER:\n{}\n\nPLAYER:{}\n\n🆙 DOUBLE\n🔄 HIT\n✅ STAND**".format(hand_dealer[0], " ".join(hand_player))
        black_jack_state = await client.send_message(message.channel, letter)

        react_list = ["🆙", "🔄", "✅"]
        for react in react_list:
            await client.add_reaction(black_jack_state, react)

        react_result = await client.wait_for_reaction(user=message.author, timeout=30, check=emoji_check)

        await client.delete_message(black_jack_state)

        if react_result:

            if react_result.reaction.emoji.startswith("✅"):
                playing_bj = False

                # TODO
            elif react_result.reaction.emoji.startswith("🔄"):
                shuffle(deck)
                hand_player.append(deck.pop())
                hand_player_value = calculate_value_in_hand(hand_player)
                if hand_player_value > 21:
                    playing_bj = False


                # TODO
            elif react_result.reaction.emoji.startswith("🆙"):
                # SET BET 2X

                # TODO
                pass

        else:
            # TODO CLOSE GAME
            return

"""    ##
    hand_dealer = []
    hand_player = [[],[]]

    hand_player[0].append(deck.pop(randint(0, len(deck)-1)))
    hand_dealer.append(deck.pop(randint(0, len(deck)-1)))
    hand_player[0].append(deck.pop(randint(0, len(deck)-1)))
    hand_dealer.append(deck.pop(randint(0, len(deck)-1)))
    print(hand_dealer)
    print(hand_player)

    letter = "**DEALER:\n {} :stop_button:\n\n\nPLAYER:\n {}**".format(hand_dealer[0], " ".join(hand_player[0]))
    letter += "\n\n🆙 DOUBLE\n🔄 HIT\n✅ STAND\n🔀 SPLIT\n"
    black_jack_letter = await client.send_message(message.channel, letter)
    await client.add_reaction(black_jack_letter, "🆙")
    await client.add_reaction(black_jack_letter, "🔄")
    await client.add_reaction(black_jack_letter, "✅")
    await client.add_reaction(black_jack_letter, "🔀")

    return"""
