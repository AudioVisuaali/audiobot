from audiovisuaali import send
from urllib.request import quote
from config import GOOGLE_KEY_SEARCH as google_key
from requests import get as rget
from bs4 import BeautifulSoup
import re
from json import loads
# google
async def google(message, client, arguments):

    page = loads(rget("https://www.googleapis.com/customsearch/v1?key={}&cx=008050020608944106700:shzflckcpo4&q={}".format(google_key, quote(arguments))).text)

    letter = ":mag_right: **| Here's your result for: **__{}__\n\n:one: **{}**\n<{}>\n\n:two: **{}**\n<{}>\n\n:three: **{}**\n<{}>\n".format(arguments, page["items"][0]["title"], page["items"][0]["link"], page["items"][1]["title"], page["items"][1]["link"], page["items"][3]["title"], page["items"][3]["link"])

    await client.send_message(message.channel, letter)








    return
    #TODO USE API AND SEND BEST 3
    search = arguments
    google = "https://www.google.com/search?q={}".format(quote(arguments))

    await client.send_message(message.channel, "<@{}> Googled {}\n".format(message.author.id, arguments, google))
    send(1, "Googled")
