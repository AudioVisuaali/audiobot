


async def userinfo(message, client, arguments):

    #items
    items = ["User", "ID", "Created", "Joined", "Last Seen", "Last Spoke", "Spoken Here", "Roles", "Names"]

    # Longest item in list
    items_max_len = len(max(items, key=len))


    each_step = ["User", "ID", "Created", "Joined", "Last Seen", "Last Spoke", "Spoken Here", "Roles", "Names"]

    # Letter
    letter = "**User information for {}**\n```autohotkey\n".format(message.author.name)


    for state in range(len(items)):

        letter += "{}{}: {}\n".format(" "*(items_max_len - len(items[state])), items[state], each_step[state])

    letter += "```"

    await client.send_message(message.channel, letter)
