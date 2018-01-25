from audiovisuaali import send
import nps
from math import ceil

#TODO timeout max 1s
# test trash
async def math_func(message, client, arguments):

    if message.author.nick is None:
        name = message.author.name
    else:
        name = message.author.nick

    # Calling function
    nsp = nps.NumericStringParser()
    result = nsp.eval(arguments)

    # removing .0 when value is int
    try:
        b = ceil(result)
        if result == b:
            result = b
    except:
        pass

    # Checking for 69
    if result == 69 or result == 69.69:
        eggplant = ":eggplant:"
    else:
        eggplant = ""

    # Creating message
    letter = ":cancer: **| {} it's {} {}**".format(name, str(result), eggplant)
    await client.send_message(message.channel, letter)
    send(1, "Math done")
