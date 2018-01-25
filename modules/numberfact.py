from audiovisuaali import send
from requests import get as rget
from random import randint

# guess number facts
async def number_fact(message, client, arguments):

    # Random number if user didn't say anything
    if not arguments:
        number = str(randint(0,1000))
    else:
        number = arguments[0]

    # Fetch a numberfact
    query = "http://numbersapi.com/{}/trivia?notfound=floor&fragment".format(number)
    response = rget(query).text

    # Checking if name is valid from response
    #TODO

    # Sending message
    letter = ":alien: **| The number {} is {}**".format(number, response)
    await client.send_message(message.channel, letter)
    send(1, "Numberfact sent!")
