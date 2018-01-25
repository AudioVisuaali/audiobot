from config import HELP_EXTERNAL_COMMANDS as help_external_commands
from config import COMMAND_START as command_start
from config import OWNER_ID as owner_id
from mysqlfiles import commands_get_all
from mysqlfiles import profile_id_get
from audiovisuaali import send
from dirmap import dirmap

# commands
async def commands_help(message, client, arguments):

    starter = command_start
    if not arguments:
        function_commands = dirmap
        keepo = "**Here are all the commands!!!**\n"
        func_comd_list = []
        for a in function_commands:
            if dirmap[a]["admin"] == False:
                func_comd_list.append(starter +a)
        keepo += "`" + ", ".join(func_comd_list) + "`"

        asd = commands_get_all()
        keepo += "\n\n**Here are all the response commands!!**\n"
        keepo += "`" + ", ".join(starter + b[0] for b in asd) + "`"

        if help_external_commands:
            for pod in help_external_commands:
                keepo += "\n\n**" + pod["commands_heading"] + "**\n"
                keepo += "`" + ", ".join(pod["command_start"] + b for b in pod["commands_list"]) + "`"

        try:
            if message.author.id in owner_id or (profile_id_get(message.author.id)[1] == "3"):
                keepo += "\n\n**Here are all the __ADMIN__ commands!!!** :smirk:\n"
                func_comd_list = []
                for a in function_commands:
                    if dirmap[a]["admin"] == True:
                        func_comd_list.append(starter +a)
                keepo += "`" + ", ".join(func_comd_list) + "`"
        except:
            pass

        keepo += "\n\nFor more help do {}help <command>".format(starter)

        # Sending message
        await client.send_message(message.channel, keepo)

    else:
        # Getting command properties
        source = dirmap[arguments[0]]
        mail = ""
        # Getting pods for examples
        for pod in source["example"]:
            mail += "\n__Input:__ {}{}\n__Output:__ {}\n".format(starter, pod["input"], pod["output"])

        # Creating message
        letter = "**:question: | Help menu for {}\n\n__INFO:__ {}\n__SYNTAX:__ {}{}\n{}**".format(arguments[0],source["info"],starter,source["syntax"],mail)

        # Sengind message
        await client.send_message(message.channel, letter)

    send(1, "Help sent!")
    return
