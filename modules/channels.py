# Roles
async def roles(message, client, arguments):

    # Values
    roles_list = ""
    longest_name = 0
    number = 0
    numberlen = 0
    message_sent = 0

    for role in message.server.roles:
        if len(role.name) > longest_name:
            longest_name = len(role.name)
        numberlen += 1

    for role in message.server.roles:
        number += 1
        roles_list = roles_list + "[{}{}] {}{} ID: {} HEX: {}\n".format(str(number), " "*(len(str(numberlen))-len(str(number))), role.name, " "*(longest_name-len(role.name)), role.id, str(role.colour))
        message_sent = 0
        if len(roles_list) >= 1900:
            roles_list = "```py\n" + roles_list.replace("<","").replace(">","") + "```"
            await client.send_message(message.channel, roles_list)
            roles_list = ""
            message_sent = 1

            # If they already have the role1
    if message_sent == 0:
        roles_list = "```py\n" + roles_list.replace("<","").replace(">","") + "```"
        await client.send_message(message.channel, roles_list)
    if len(roles_list) > 2000:
        await client.send_message(message.channel, "Internal error")
