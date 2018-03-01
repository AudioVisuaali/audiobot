from discord import Embed

# Server stats
async def server_stats(message, client, arguments):

    # Starting embed
    em=Embed(description="ID: "+message.server.id, colour=0xf99e1a)

    # Setting icon
    em.set_author(name=message.server.name, icon_url=message.server.icon_url)

    # Verification level
    em.add_field(name="Verification Level", value=message.server.verification_level, inline=True)

    # Region
    em.add_field(name="Region", value=message.server.region, inline=True)

    # Members total, offline use:member_count?
    members_online, members_offline = 0, 0
    for state in message.server.members:
        if str(state.status) == "offline":
            members_offline += 1
        else:
            members_online += 1
    em.add_field(name="Users [{}]".format(members_online+members_offline), value=str(members_online)+ " online", inline=True)


    # Channels -> categories,text,voice
    text, voice, category = 0, 0, 0
    for huone in message.server.channels:
        if str(huone.type) == "voice":
            voice += 1
        elif str(huone.type) == "text":
            text += 1
        elif str(huone.type) == "4":
            category += 1
    em.add_field(name="Channels [{}]".format(text+voice+category), value="Text:{}\nVoice:{}\nCategory:{}\n\n".format(text, voice, category), inline=True)

    # Large
    em.add_field(name="Large server", value=message.server.large, inline=True)

    # Emojis
    faces = 0
    for face in message.server.emojis:
        faces += 1
    em.add_field(name="Emojis", value=str(faces), inline=True)

    # Owner
    ownsthis = message.server.owner
    em.add_field(name="Owner", value=ownsthis.name+"#"+str(ownsthis.discriminator), inline=False)

    # Crreation date
    em.add_field(name="Created", value=message.server.created_at, inline=False)

    # Roles
    count_role = 0
    for role in message.server.roles:
        count_role += 1
    em.add_field(name="Roles", value=str(count_role), inline=False)

    # Query by
    em.set_footer(text="Query by: {}".format(message.author.name), icon_url=message.server.icon_url)

    # Thumbnail
    em.set_thumbnail(url=message.server.icon_url)

    # Sending message
    await client.send_message(message.channel, embed=em)
