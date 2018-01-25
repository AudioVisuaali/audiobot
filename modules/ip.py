from audiovisuaali import send
from socket import gethostbyname
from json import loads
from urllib.request import quote
from requests import get as rget

# find out ip
async def ip(message, client, arguments):

    ip_address = gethostbyname(arguments[0])
    url = "https://ipinfo.io/%s/json".format(quote(ip_address))
    response = loads(rget(url).text)

    letter = ":printer:  **| We found info for your ip! ```IP: {}\ncity: {}\nregion: {}\ncountry: {}\nloc: {}\norg: {}```**"
    letter.format(response["ip"], response["city"], response["region"], response["country"], response["loc"], response["loc"])

    # Send and log
    await client.send_message(message.channel, letter)
    send(1, "Ip info retrieved")
