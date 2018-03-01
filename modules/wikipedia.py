from audiovisuaali import send

from json import loads
from urllib.request import quote
from requests import get as rget


# wikipedia
async def wikipedia(message, client, arguments):

    # Setting nickname
    if message.author.nick is None:
        name = messaghe.author.name
    else:
        name = message.author.nick

    # Searching
    search_query = quote(arguments)
    query = "https://en.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch={}".format(quote(search_query))

    # Fetching and checking
    try:
        # Fetch
        response = loads(rget(query).text)
        print(response["query"]["search"][0])
        wikilink = "<https://en.wikipedia.org/wiki/{}>".format(quote(response["query"]["search"][0]["title"]))
        letter = ":bookmark: **| {}, here's your link for: **__{}__\n\n:one: {}\n".format(name, arguments, wikilink)
        try:
            letter += "\n:two: <https://en.wikipedia.org/wiki/{}>\n".format(quote(response["query"]["search"][1]["title"]))
            try:
                letter += "\n:three: <https://en.wikipedia.org/wiki/{}>\n".format(quote(response["query"]["search"][2]["title"]))
            except:
                pass
        except:
            pass
    # Check
    except IndexError:
        letter = ":bookmark: **| {}, we couldn't find a match!**".format(name)

    # Sending response
    await client.send_message(message.channel, letter)
    send(1, "Wikipedia serach complete!")
