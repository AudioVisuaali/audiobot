from audiovisuaali import send
import asyncio

# timer
async def timer(message, client, arguments):

    # Checking for input
    try:
        arguments = str(arguments)
        time_to_sleep = int(arguments)
    except:
        await client.send_message(message.channel, ":x: **| Invalid input**")
        return

    # Starting process
    delete_this = await client.send_message(message.channel, ":clock1: **| <@{}> Notifying you in {} seconds!**".format(message.author.id, arguments))
    send(1, "Asked for a timer")

    # after sleep removing previous message for chat clarity
    await asyncio.sleep(time_to_sleep)
    await client.delete_message(delete_this)

    # Sending message and logging
    await client.send_message(message.channel, ":clock1: **| <@{}> Time's up!**".format(message.author.id))
    send(1, "Timer is done!")

    return
