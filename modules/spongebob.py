import audiovisuaali

# Capitalizing every 2nd letter
def spongebob_message(m):
    spongebobbed = ""
    i = True  # capitalize
    for char in m:
        if i:
            spongebobbed += char.upper()
        else:
            spongebobbed += char.lower()
        if char != ' ':
            i = not i
    return spongebobbed

# Spongebob text
async def spongebob(message, client, arguments):

    # Creating a list from the message
    splitted = list(arguments)

    #creating message and sending it
    letter = "**<:baus:297862596659249156> | {}**".format(spongebob_message(splitted))
    await client.send_message(message.channel, letter)

    #TODO: logging and CLEAN
