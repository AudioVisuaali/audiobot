from audiovisuaali import get_user_instance
from audiovisuaali import send

from requests import get as rget

# Joke
async def avatar(message, client, arguments):

        # Checks if message author or else
        if not arguments:
            user_instance = message.author
        else:
            user_instance = await get_user_instance(message, arguments[0])

        # Stripping link
        print(user_instance.name)
        url = user_instance.avatar_url
        file_name = url.split("/")[len(url.split("/"))-1].split("?")[0]
        print(client.avatar_url)

        # User name depending on given user
        if user_instance.nick is None:
            name = user_instance.name
        else:
            name = user_instance.nick

        # Checks Image url
        with open('./profile/profile_pictures/{}'.format(file_name), 'wb') as handle:
            response = rget(url, stream=True)

            # Something went wrong
            if not response.ok:
                await client.send_message(message.channel, ":thinking: **| Error**")
                return

            # Saves image
            for block in response.iter_content(1024):
                handle.write(block)

        # Send picture to the chat
        await client.send_file(message.channel, "./profile/profile_pictures/{}".format(file_name), filename="./profile/profile_pictures/{}".format(file_name), content="**Profile picture of {}**".format(name), tts=False)
        return
