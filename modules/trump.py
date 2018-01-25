import audiovisuaali
from urllib.request import quote
from requests import get as rget
from json import loads

# trump
async def trump(message, client, arguments):

    #Starting to fetch a Catfact
    query = "https://api.tronalddump.io/search/quote?query={}".format(quote(arguments))
    response = loads(rget(query).text)

    # Checking if name is valid from response
    if response["total"] == 0:
        letter = "No quotes found"
        return

    # Creating if exists
    else:
        letter = ":rofl: **| Found " + str(response["total"]) + " hits\n```" + response["_embedded"]["quotes"][0]["value"] + "```"
        try:
            letter = letter + "```" + response["_embedded"]["quotes"][1]["value"] + "```"
        except:
            pass
        try:
            letter = letter + "```" + response["_embedded"]["quotes"][2]["value"] + "```"
        except:
            pass

    # Sending message
    await client.send_message(message.channel, letter+"**")
