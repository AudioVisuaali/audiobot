from config import OWNER_ID as owners
from audiovisuaali import send

from requests import get as rget

# Set avatar
async def set_avatar(message, client, arguments):

    # Try parsing attachments
    try:
        url = message.attachments[0]["url"]
    except:
        url = arguments[0]

    # Get file name
    file_name = url.split("/")[len(url.split("/"))-1].split("?")[0]

    # Checks Image url
    with open('./profile/bot_profile_pictures/{}'.format(file_name), 'wb') as handle:
        response = rget(url, stream=True)

        # Something went wrong
        if not response.ok:
            await client.send_message(message.channel, ":thinking: **| Invalid url or other error**")
            return

        # Saves image
        for block in response.iter_content(1024):
            handle.write(block)

    # Sending image
    with open('./profile/bot_profile_pictures/{}'.format(file_name), 'rb') as f:

        try:
            await client.edit_profile(avatar=f.read())
        except:
            await client.send_message(message.channel, ":thumbsdown: **| Discord is not liking this try again later!**")
            return


    # Send info
    await client.send_message(message.channel, ":thumbsup: **| Profile picture updated!**")
    send(1, "Bot's profile picture updated!")
