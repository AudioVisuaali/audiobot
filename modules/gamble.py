from audiovisuaali import send
from mysqlfiles import users_get_gamble_history
from asyncio import sleep as asleep

# Gamble
async def gamble(message, client, arguments):

    # variables
    amount = 30
    spacing = []
    biggest_amount_space = 0
    history = users_get_gamble_history(message.author.id, amount)
    letter = "\nThis is your gambling history!```py\nMode      Outcome\n"
    mode = "roulette"

    # Resolving the biggest space
    for row in history:
        if len(str(row[1])) > biggest_amount_space:
            biggest_amount_space = len(str(row[1]))

    # Creating row for lsit
    for row in history:
        if row[2] == "win":
            out = "+"
        else:
            out = "-"

        if row[3] == 1:
            multiplier = str(row[4])
        else:
            multiplier = ""
        letter += mode + "  " + out + row[1] + " "*(biggest_amount_space-len(str(row[1])) +0) +"\n"#+ multiplier +"\n"

    # finishing and sending message
    letter += "```"
    delete = await client.send_message(message.channel, letter)
    await asleep(20.0)
    await client.delete_message(delete)
    send(1, "Gamble history sent")
    return
