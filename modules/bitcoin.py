from audiovisuaali import send
from json import loads
from requests import get as rget
# find out ip
async def bitcoin(message, client, arguments):

    #Starting to fetch a Catfact
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = loads(rget(url).text)

    # Checking if name is valid from response
    # Sending message
    USD = "%.2f" % response["bpi"]["USD"]["rate_float"]
    GBP = "%.2f" % response["bpi"]["GBP"]["rate_float"]
    EUR = "%.2f" % response["bpi"]["EUR"]["rate_float"]

    letter = ":dollar: **| At the moment one Bitcoin is worth ```USD: ${}\nGBP: £{}\nEUR: €{}```**".format(USD, GBP, EUR)
    await client.send_message(message.channel, letter)
    send(1, "Bitcoin info sent")
