import audiovisuaali
import random


# RPS BY WOLFIE <3
async def rps(message, client, arguments):

    #USERINPUT
    userinput = arguments

    #OPTIONS
    options = ["rock", "paper", "scissors"]
    random_number = random.randint(0,2)

    #COMPUTER INPUT
    botinput = options[random_number]

    #VALIDATION
    if not (userinput.lower() in options):
        send_message = "That isn't right!"
        await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)
        return

    #ANSWER - Draw
    if botinput == userinput:
        send_message = "Draw"
        await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)

    #ANSWER - Rock
    elif botinput == "rock":
        if userinput == "paper":
            send_messagesend_message = "Paper beats Rock, you win!"
            await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)
        else:
            send_message = "You lose!"
            await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)

            #ANSWER - Paper
    elif botinput == "paper":
        if userinput == "scissors":
            send_message = "Scissors beats paper, you win!"
            await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)
        else:
            send_message = "You lose!"
            await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)

#ANSWER - Scissors
    elif botinput == "scissors":
        if userinput == "rock":
            send_message = "Rock beats Scissors, you win!"
            await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)
        else:
            send_message = "You lose!"
            await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)
