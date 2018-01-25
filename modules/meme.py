from audiovisuaali import send
from mysqlfiles import meme_get_random
from mysqlfiles import profile_id_get
from mysqlfiles import meme_get_total_memes
from mysqlfiles import meme_insert_new
from mysqlfiles import meme_get_meme_by_id


# Meme database
async def meme(message, client, arguments):

    if message.author.nick is None:
        name = message.author.name
    else:
        name = message.author.nick

    if arguments == "":
        meme = meme_get_random()

        if meme == None:
            await client.send_message(message.channel, "<@{}> Meme data:b:ase empty!".format(message.author.id))
            return

        # Sending meme
        await client.send_message(message.channel, "**:joy: | {} here's your meme, ID:{}** {}".format(name, str(meme[1]), meme[0]))
        return

    elif arguments[0] == "add":

        # Checking if the user has enough powers to run the command
        check = profile_id_get(message.author.id)
        if not check[0] ==  message.author.id:
            await client.send_message(message.channel, ":x: | You don't have enough rights to run the command!")
            return

        total_memes = meme_get_total_memes()
        if total_memes == None:
            total_memes = 0

        # Variables for insertation of data
        meme_id = int(total_memes[0]) + 1
        adder_d_id = str(message.author.id)
        name = str(message.author)
        server_id = str(message.server.id)
        link = arguments[1]

        meme_insert_new(meme_id, adder_d_id, name, server_id, link)
        await client.send_message(message.channel, "**:joy: | {} meme added with ID:{}**".format(name, str(meme_id)))
    else:

        try:
            meme_id = int(arguments[0])
            meme = meme_get_meme_by_id(meme_id)
            if meme == None:
                await client.send_message(message.channel, "**:joy: | {} no meme with that ID**".format(name))
                return

            await client.send_message(message.channel, "**:joy: | {} here's your meme, ID:{}** {}".format(name,str(meme[1]), meme[0]))
            return

        except TypeError:
            send(3, "TypeError???? ")

    send(1, "Done with meme")
