#import audiovisuaali
#import mysqlfiles
import requests
from bs4 import BeautifulSoup
import re
import json
import math

#TODO
async def chronogg(message, client, arguments):
        # Getting page content
        page3 = requests.get("https://chrono.gg/")
        soup3 = BeautifulSoup(page3.content, "lxml")

        # Filtering <script> for json
        asd = soup3.find('script', text=re.compile('window\._sharedData'))
        json_text = re.search(r'^\s*window\._sharedData\s*=\s*({.*?})\s*;\s*$', asd.string, flags=re.DOTALL | re.MULTILINE).group(1)
        data = json.loads(json_text)

        # Creating message
        percentage = str(math.ceil(100 - (data["sale_price"] / data["normal_price"] * 100)))
        letter = "**New game on sale: " + data["og_description"] + " \nNormally " + str(data["normal_price"]) + "$, " + percentage + "% off!\nhttps://chrono.gg/ **"

        await client.send_message(message.channel, letter)
