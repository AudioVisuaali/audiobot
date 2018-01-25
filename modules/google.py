from audiovisuaali import send
from urllib.request import quote

# google
async def google(message, client, arguments):

    #TODO USE API AND SEND BEST 3
    search = arguments
    google = "https://www.google.com/search?q={}".format(qutoe(arguments))

    await client.send_message(message.channel, "<@{}> Googled {}\n".format(message.author.id, arguments, google))
    send(1, "Googled")
