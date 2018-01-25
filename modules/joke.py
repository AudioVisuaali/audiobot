from audiovisuaali import send
from requests import get as rget
from json import loads
from json import load
from random import randint

def get_joke(jokes):
    for _ in range(10):
        funny_joke = jokes[randint(0,len(jokes)-1)]
        if len(funny_joke) < 1500:
            return funny_joke
# Joke
async def joke(message, client, arguments):

    """# Starting to fetch a joke
    response = loads(rget("https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke").text)

    # Creating letter
    letter = "**{}**\n-{}".format(response["setup"], response["punchline"])

    # Sending message
    await client.send_message(message.channel, letter)
    send(1, "Joke sent LUL")

    # Old module
    # In the new module the jokes are with the bot
    """

    # Getting jokes
    data = load(open('./jokes/joke_list.json'))

    # Getting a joke that's not too long for discord 2000 message limit
    asd = get_joke(data)

    # Generating message
    letter = ":joy: **| {}**\n`{}`".format(asd["title"], asd["body"])
    await client.send_message(message.channel, letter)
    send(1, "Joke sent LUL")
