from audiovisuaali import send
from json import loads
from urllib.request import urlretrieve
from urllib.request import urlopen
from requests import get as rget
from json import loads
from os import remove as osremove
# Randomcat (Get's a random cat)
async def random_cat(message, client, arguments):

    # Fetching data drom urban
    url = 'http://random.cat/meow'
    response = loads(rget(url).text)["file"]
    urlretrieve(response, "./download/cats/"+response[20:])

    # Sending message
    await client.send_file(message.channel, "./download/cats/"+response[20:],filename="./download/cats/"+response[20:], content="<@"+message.author.id+"> ", tts=False)
    osremove("./download/cats/"+response[20:])
    send(1, "Wild cat received!")
    return
