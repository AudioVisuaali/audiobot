from audiovisuaali import send
#import urllib.request as urllib2

from urllib.request import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Iterating youtube results
def get_yt_links(soup):

    # Lists to store links
    link_list = []
    name_list = []

    # Iterating for videos
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        link_list.append('https://www.youtube.com' + vid['href'])
        name_list.append(vid["title"])

        # Wanted list length
        if len(link_list) >= 3:
            return link_list, name_list
        else:
            pass
    return link_list, name_list


#Youtube search
async def youtube(message, client, arguments):

    # Creating youtube link

    send(1, "Searching for youtube request: **{}**".format(arguments))
    query = "https://www.youtube.com/results?search_query="+quote(arguments)

    # Fetching link
    response = urlopen(query)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")

    # Finding source
    videos = get_yt_links(soup)

    # Creating message
    letter = ":arrow_forward: **| Here are some matches for: {}\n\n:one: | {}\n**<{}>**\n\n:two: | {}\n**<{}>**\n\n:three: | {}**\n<{}>"
    formation = letter.format(arguments, videos[1][0], videos[0][0], videos[1][1], videos[0][1], videos[1][2], videos[0][2])
    await client.send_message(message.channel, formation)
    return
