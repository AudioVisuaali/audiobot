from audiovisuaali import send
from urllib.request import quote
from requests import get as rget
from json import loads


# urban (Searches the meaning for a word)
async def urban(message, client, arguments):

    # Fetching data drom urban
    send(1, "Urban starting!")
    query = "http://api.urbandictionary.com/v0/define?term={}".format(quote(arguments))
    response = loads(rget(query).text)

    # Getting items
    item0meaning = response['list'][0]['definition']
    item0example = response['list'][0]['example']
    item1meaning = response['list'][1]['definition']
    item1example = response['list'][1]['example']

    # Creating message and sending it
    send_message = "Definition for: "+arguments+"\n```"+item0meaning+"```"+ "Example: " + item0meaning + "\n\n```"+item1meaning+"```"+ "Example: " + item1example

    # Sending message
    await client.send_message(message.channel, "<@"+message.author.id+"> "+send_message)
    send(1, "Urban complete")
