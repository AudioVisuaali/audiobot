import audiovisuaali
from random import randint

# Copied from somewhere
async def guess(message, client, arguments):

    # Sending a message
    await client.send_message(message.channel, '**Guess a number between 1 to 10**')

    # Checking if response is a number
    def guess_check(m):
        return m.content.isdigit()

    guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
    answer = randint(1, 10)

    if guess is None:
        fmt = 'Sorry, you took too long. It was {}.'
        await client.send_message(message.channel, fmt.format(answer))
        return

    if int(guess.content) == answer:
        await client.send_message(message.channel, '**You are right!**')
    else:
        await client.send_message(message.channel, '**Sorry. It is actually {}.**'.format(answer))
