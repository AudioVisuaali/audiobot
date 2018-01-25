from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.request import quote
from audiovisuaali import send


# random_dog (Get's a random dog)
async def random_dog(message, client, arguments):

    # Getting a picture not a video or gif
    loop = 1
    response = ""
    while loop == 1:
        response = str(urlopen("https://random.dog/woof").read())[2:-1]
        if response[-3:] == ("jpg" or "png"):
            loop = 0
    urlretrieve("https://random.dog/{}".format(quote(response)), "./download/dogs/"+response)

    # Sending picture
    await client.send_file(message.channel, "./download/dogs/"+response,filename="./download/dogs/"+response, content="<@"+message.author.id+"> ", tts=False)
    send(1, "Top Dog received!")
    return
