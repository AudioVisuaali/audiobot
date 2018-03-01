dirmapexample = {
    # Name of the function / Name that you use to call the command from chat
    "example": {
        # Function called in python
        "function": "function_name",
        # admin command?
        "admin": 1,
        # Arguments
        "args": {
            # Delimeter / xxx xxx -> ["xxx","xxx"] /splits word with " "
            "delimeter": " ",
            # How many times delimeter in going to be used
            "split": 1,
            # Amount of arguments made from delimeter
            "length": [2],
        },
        # For command info
        "info" : "This is to find out how to make a pancake",
        # Parameters for command
        "syntax": "add <call> <response> // (call must be uniform)",
        # Example
        "example": [
        # Pod 1
        {
            # Example request
            "input": "add example Example response",
            # Example Response
            "output": "@testuser#1234 Command Example has been added!"
        },
        # Pod 2
        {
            # Example request
            "input": "add example Example response",
            # Example Response
            "output": "@testuser#1234 Command Example has been added!"
        }]
    },
}
# ADD YOUR FUNCTION PATHS HERE +\/

# ADD YOUR COMMAND TO IT'S OWN FILE.py
# IMPORT YOUR FILE.py IN /modules/__init__.py

# Directory mapping
dirmap = {
    "add": {
        "function": "command_add",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 1,
            "length": [2],
        },
        "info": "This command is used to add custom commands!",
        "syntax": "add [command] [Message]",
        "example": [{
            "input": "add whitehouse Whitehouse is a white house!",
            "output": ':white_check_mark: **| Command "__dd__" added to the database!**'
        }]
    },


    "purge": {
        "function": "purge",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 1,
            "length": [0],
        },
        "info": "This command is used to clear bots cache",
        "syntax": "purge",
        "example": [{
            "input": "purge",
            "output": ':white_check_mark: **| Bot is now ready start over!**'
        }]
    },

    "remove": {
        "function": "command_remove",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 1,
            "length": [1],
        },
        "info": "This command removes added commands!",
        "syntax": "remove [command]",
        "example": [{
            "input": "remove whitehouse",
            "output": ":white_check_mark: **| Command not in database!"
        }]
    },

    "setavatar": {
        "function": "set_avatar",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "This command changes bots profile image!",
        "syntax": "setavatar <link>",
        "example": [{
            "input": "setavatar <link>",
            "output": ":white_check_mark: **| Profile picture has been updated!"
        }]
    },

    "userinfo": {
        "function": "userinfo",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Gets users info!",
        "syntax": "userinfo",
        "example": [{
            "input": "userinfo",
            "output": ":white_check_mark: **| Profile picture has been updated!"
        }]
    },

    "playing": {
        "function": "set_bot_playing",
        "admin": True,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "This command sets the bots playing status!",
        "syntax": "playing [status]",
        "example": [{
            "input": "playing with bots",
            "output": ':white_check_mark: **| Playing status has been updated to "__with bots__"**'
        }]
    },

    "pot": {
        "function": "tax_pot",
        "admin": True,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "This command gets the pot!",
        "syntax": "pot",
        "example": [{
            "input": "casino",
            "output": "casino"
        }]
    },

    "casino": {
        "function": "casino",
        "admin": True,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "This command toggles casino!",
        "syntax": "casino",
        "example": [{
            "input": "casino",
            "output": "casino"
        }]
    },

    "roles": {
        "function": "roles",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 22,
            "length": [0],
        },
        "info": "This command lists all the roles on the server",
        "syntax": "roles",
        "example": [{
            "input": "roles",
            "output": "´´´[1  ] Viitaniemi                     ID: 335491931599536141 HEX: #b1ffec´\n[2  ] Koson poikabändi               ID: 280704094836883456 HEX: #07f886´´´"
        }]
    },

    "test": {
        "function": "test",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 20,
            "length": [0,1,2,3,4,5,6,7,8,9,10],
        },
        "info": "This command removes added commands!",
        "syntax": "remove [command]",
        "example": [{
            "input": "remove whitehouse",
            "output": ":white_check_mark: **| Command not in database!"
        }]
    },

    "join": {
        "function": "raffle_lotto",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 20,
            "length": [0,1],
        },
        "info": "This command removes added commands!",
        "syntax": "remove [command]",
        "example": [{
            "input": "remove whitehouse",
            "output": ":white_check_mark: **| Command not in database!"
        }]
    },

    "ping": {
        "function": "ping",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Test command, always works when something is broken. Can also be testes if the bot is on!",
        "syntax": "ping",
        "example": [{
            "input": "ping",
            "output": "pong!"
        }]
    },

    "chronogg": {
        "function": "chronogg",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Get's you the daily game from chronoGG",
        "syntax": "chronogg",
        "example": [{
            "input": "chronogg",
            "output": "<chronogg response>"
        }]
    },

    "reverse": {
        "function": "reverse",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "This reverses text order in the message!",
        "syntax": "reverse [message]",
        "example": [{
            "input": "reverse saippuakauppias",
            "output": ":arrows_counterclockwise: ** | saippuakauppias"
        }]
    },

    "spongebob": {
        "function": "spongebob",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Uppercases every second letter!",
        "syntax": "spongebob [message]",
        "example": [{
            "input": "spongebob spongebob",
            "output": ":joy: ** | SpOnGeBoB"
        }]
    },

    "timer": {
        "function": "timer",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Sets up a timer!",
        "syntax": "timer [time]",
        "example": [{
            "input": "notify 12",
            "output": ":clock1: | Notifying you in 12 seconds!"
        }]
    },

    "notify": {
        "function": "timer",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Sets up a timer!",
        "syntax": "notify [time]",
        "example": {
            "input": "notify 12",
            "output": ":clock1: | Notifying you in 12 seconds!"
        }
    },

    "avatar": {
        "function": "avatar",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0,1],
        },
        "info": "Get avatar!",
        "syntax": "avatar ?[user]",
        "example": [{
            "input": "avatar",
            "output": "Profile picture of User"
        },
        {
            "input": "avatar User",
            "output": "Profile picture of User"
        }]
    },

    "math": {
        "function": "math_func",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 3,
            "length": [1],
        },
        "info": "Does basic math operations",
        "syntax": "math [formula]",
        "example": [{
            "input": "math 43 + 26",
            "output": ":cancer: **| It's 69 :eggplant:**"
        }]
    },

    "joke": {
        "function": "joke",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Doesn't get you a joke! :joy:",
        "syntax": "joke",
        "example": [{
            "input": "joke",
            "output": "There's nothing more funnier than this!"
        }]
    },

    "dad": {
        "function": "dad_joke",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Your father so fun I can't get it!",
        "syntax": "dad",
        "example": [{
            "input": "dad",
            "output": "What did one snowman say to the other snow man? Do you smell carrot?"
        }]
    },

    "yomama": {
        "function": "yo_mama",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Yo mama so fat she couldn't fit in to this joke",
        "syntax": "yomama",
        "example": [{
            "input": "yomama",
            "output": "Yo mama so fat, she can't even jump to a conclusion."
        }]
    },


    "chucknorris": {
        "function": "chuck_norris",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Get's you a chuck norris joke!",
        "syntax": "chucknorris",
        "example": [{
            "input": "dad",
            "output": " Chuck Norris eats lightning and shits out thunder."
        }]
    },

    "chuck": {
        "function": "chuck_norris",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Get's you a chuck norris joke!",
        "syntax": "chuck",
        "example": [{
            "input": "dad",
            "output": " Chuck Norris eats lightning and shits out thunder."
        }]
    },

    "norris": {
        "function": "chuck_norris",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Get's you a chuck norris joke!",
        "syntax": "norris",
        "example": [{
            "input": "dad",
            "output": " Chuck Norris eats lightning and shits out thunder."
        }]
    },

    "weather": {
        "function": "weather",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Get's the local weather",
        "syntax": "!weather <place>",
        "example": [{
            "input": "weather suomi",
            "output": "Sun is shining in Finland"
        }]
    },

    "rps": {
        "function": "rps",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Rock, paper, scissors!",
        "syntax": "rps [rock/paper/scissors]",
        "example": [{
            "input": "rps scissors",
            "output": "Scissors beats paper, you win!"
        }]
    },

    "youtube": {
        "function": "youtube",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Searches for youtube",
        "syntax": "youtube <>",
        "example": [{
            "input": "youtube never gonna give you all",
            "output": "<https://www.youtube.com/watch?v=dQw4w9WgXcQ>"
        }]
    },

    "yt": {
        "function": "youtube",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Searches for youtube",
        "syntax": "youtube <>",
        "example": [{
            "input": "youtube never gonna give you all",
            "output": "<https://www.youtube.com/watch?v=dQw4w9WgXcQ>"
        }]
    },

    "slap": {
        "function": "slap",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 1,
            "length": [1],
        },
        "info": "Slaps user",
        "syntax": "slap <user>",
        "example": [{
            "input": "slap user",
            "output": ":raised_back_of_hand: **| Sla:b:s User!**"
        }]

    },

    "stab": {
        "function": "stab",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 1,
            "length": [1],
        },
        "info": "Stab user",
        "syntax": "stab <user>",
        "example": [{
            "input": "stab user",
            "output": ":raised_back_of_hand: **| Sta:b:s User!**"
        }]
    },

    "lmgtfy": {
        "function": "lmgtfy",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Creates a Let Me Google That For You link!",
        "syntax": "lmgtfy <query>",
        "example": [{
            "input": "lmgtfy how to sit",
            "output": "Let me Google that for you!\n<http://lmgtfy.com/?q=how%20to%20sit>"
        }]
    },

    "google": {
        "function": "google",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Creates a google link",
        "syntax": "google <query>",
        "example": [{
            "input": "google how to sit",
            "output": "Googled how to sit <https://google.com/search?q=how%20to%20sit>"
        }]
    },

    "geolocation": {
        "function": "geolocation",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [1],
        },
        "info": "Gets geolocational location",
        "syntax": "geolocation <location>",
        "example": [{
            "input": "geolocation London",
            "output": ":earth_americas: **| London, UK\nLAT: 51.5074\nLNG: -0.1278\n**"
        }]
    },

    "geo": {
        "function": "geolocation",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [1],
        },
        "info": "Gets geolocational location",
        "syntax": "geo <location>",
        "example": [{
            "input": "geo London",
            "output": ":earth_americas: **| London, UK\nLAT: 51.5074\nLNG: -0.1278\n**"
        }]
    },

    "translate": {
        "function": "translate",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Translates input to chosen language!",
        "syntax": "translate ?--<language> <message>",
        "example": [{
            "input": "translate --RU Hello World!",
            "output": ":cloud: **| EN -> RU**  ´Привет мир!´"
        }]
    },

    "time": {
        "function": "time_new",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0,1],
        },
        "info": "Get's the time",
        "syntax": "time ?<location>",
        "example": [{
            "input": "time",
            "output": ":clock11: **| Time in London, UK is 18:35 and the day is Saturday**"
        }]
    },

    "lennyface": {
        "function": "lennyface",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 3,
            "length": [0],
        },
        "info": "Sends a random lennyface",
        "syntax": "time ?<location>",
        "example": [{
            "input": "lennyface",
            "output": "(✿❦ ͜ʖ ❦)"
        },
        {
            "input": "lennyface",
            "output": "(ง ͠° ͟ل͜ ͡°)ง"
        }]
    },

    "points": {
        "function": "points",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Sends a random lennyface",
        "syntax": "time ?<location>",
        "example": [{
            "input": "lennyface",
            "output": "(✿❦ ͜ʖ ❦)"
        },
        {
            "input": "lennyface",
            "output": "( ͠° ͟ʖ ͡°)"
        }]
    },

    "bank": {
        "function": "bank",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,2],
        },
        "info": "Bank management",
        "syntax": "bank ?<(add|deposit|put|give)|(take|withdraw|remove)> ?<amount>",
        "example": [{
            "input": "bank",
            "output": "You have 55 memes in bank!"
        },
        {
            "input": "bank add 55",
            "output": "You have added 55 memes to bank!"
        }]
    },

    "memes": {
        "function": "points",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Gets the amount of memes of user!",
        "syntax": "memes ?<user>",
        "example": [{
            "input": "memes",
            "output": ":money_with_wings: **| You have 420 memes!**"
        },
        {
            "input": "memes User",
            "output": ":money_with_wings: **| User has 690 memes!**"
        }]
    },

    "tokens": {
        "function": "user_tokens",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Gets the amount of tokens of user!",
        "syntax": "memes ?<user>",
        "example": [{
            "input": "memes",
            "output": ":money_with_wings: **| You have 3 tokens!**"
        },
        {
            "input": "memes User",
            "output": ":money_with_wings: **| User has 690 memes!**"
        }]
    },

    "currency": {
        "function": "points",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Currency converter!",
        "syntax": "currencyconverter <> <>??",
        "example": [{
            "input": "currencyconverter 55???",
            "output": ":money_with_wings: **| 55??? is **"
        }]
    },

    "xp": {
        "function": "user_xp",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Reveals users level and total xp",
        "syntax": "xp ?<user>",
        "example": [{
            "input": "xp",
            "output": ":b: **| You are level 14 and you have 50732 xp in total! 94% done on the current level!**"
        },
        {
            "input": "xp User",
            "output": ":b: **| User is level 19 and has 76049 xp in total! 66% done on the current level!**"
        }]
    },

    "wikipedia": {
        "function": "wikipedia",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0,1],
        },
        "info": "Searches wikipedia for the source",
        "syntax": "wikipedia <query>",
        "example": [{
            "input": "wikipedia autonomous car",
            "output": ":bookmark: **| Here's your link! https://en.wikipedia.org/wiki/Autonomous%20car**"
        }]
    },

    "wiki": {
        "function": "wikipedia",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0,1],
        },
        "info": "Searches wikipedia for the source",
        "syntax": "wiki <query>",
        "example": [{
            "input": "wiki autonomous car",
            "output": ":bookmark: **| Here's your link! https://en.wikipedia.org/wiki/Autonomous%20car**"
        }]
    },

    "top": {
        "function": "top",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1,2,3,4],
        },
        "info": "Scoreboard",
        "syntax": "top ?<tokens/xp/memes/points>",
        "example": [{
            "input": "top",
            "output": "Stats for top stats"
        },
        {
            "input": "top memes",
            "output": "Stats for top memes scoreboard"
        }]
    },

    "scoreboard": {
        "function": "top",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Scoreboard",
        "syntax": "scoreboard ?<tokens/xp/memes/points>",
        "example": [{
            "input": "scoreboard",
            "output": "Stats for top stats"
        },
        {
            "input": "scoreboard memes",
            "output": "Stats for top memes scoreboard"
        }]
    },

    "daily": {
        "function": "daily",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Redeem your daily memes",
        "syntax": "daily",
        "example": [{
            "input": "daily",
            "output": ":moneybag: **| You have redeemed 200 memes, you now have 1337 memes! **"
        }]
    },

    "kela": {
        "function": "daily",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Redeem your daily memes",
        "syntax": "kela",
        "example": [{
            "input": "kela",
            "output": ":moneybag: **| You have redeemed 200 memes, you now have 1337 memes! **"
        }]
    },

    "joined": {
        "function": "joined",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Get time when user joined",
        "syntax": "joined",
        "example": [{
            "input": "joined",
            "output": ":calendar_spiral: **| You joined the server on 2017-02-11 23:20:04**"
        },
        {
            "input": "joined User",
            "output": ":calendar_spiral: **| User joined the server on 2017-02-11 23:20:04**"
        }]
    },

    "catfact": {
        "function": "catfact",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Gets you a catfact",
        "syntax": "catfact",
        "example": [{
            "input": "catfact",
            "output": "Cat's are fun!"
        }]
    },

    "cat": {
        "function": "random_cat",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Gets you a picture of a cat",
        "syntax": "cat",
        "example": [{
            "input": "cat",
            "output": "Cat image"
        }]
    },

    "dogfact": {
        "function": "dogfact",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Gets you a dogfact",
        "syntax": "dogfact",
        "example": [{
            "input": "dogfact",
            "output": "Dog's are fun!"
        }]
    },

    "dog": {
        "function": "random_dog",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Gets you a picture of a dog",
        "syntax": "dog",
        "example": [{
            "input": "dog",
            "output": "Dog image"
        }]
    },

    "pun": {
        "function": "pun",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Get's you a pun!",
        "syntax": "pun",
        "example": [{
            "input": "pun",
            "output": "This PUNch wont hurt!"
        }]
    },

    "gender": {
        "function": "gender",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 6,
            "length": [1],
        },
        "info": "Looks up the possibilities of an name being male and female",
        "syntax": "gender <name>",
        "example": [{
            "input": "gender Jessica",
            "output": ":alien: **| There's a 100% of Jessica being a female!**"
        }]
    },

    "gamble": {
        "function": "gamble",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 5,
            "length": [0,1,2],
        },
        "info": "See your gamble history(aka how much you have lost)",
        "syntax": "gamble",
        "example": [{
            "input": "gamble",
            "output": "A list of past gambles"
        },
        {
            "input": "gamble username",
            "output": "A list of past gambles of username"
        },
        {
            "input": "gamble 40",
            "output": "A list of past gambles with 40 results"
        },
        {
            "input": "gamble username 40",
            "output": "A list of past gambles of username with 40 results"
        }]
    },

    "trump": {
        "function": "trump",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Searches what Trump has said",
        "syntax": "trump <query>",
        "example": [{
            "input": "trump women",
            "output": "List of sentences Trump has said"
        }]
    },

    "number": {
        "function": "number_fact",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 6,
            "length": [0,1],
        },
        "info": "Gives you a number fact!",
        "syntax": "number <number>",
        "example": [{
            "input": "number 69",
            "output": ":alien: | The number 69 is the atomic number of thulium, a lanthanide"
        },{
            "input": "number",
            "output": ":alien: | The number 311 is the record number of wickets taken in English cricket season by Tich Freeman in 1928"
        }]
    },

    "numberfact": {
        "function": "number_fact",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 6,
            "length": [0,1],
        },
        "info": "Gives you a number fact!",
        "syntax": "number <number>",
        "example": [{
            "input": "number 69",
            "output": ":alien: | The number 69 is the atomic number of thulium, a lanthanide"
        },{
            "input": "number",
            "output": ":alien: | The number 311 is the record number of wickets taken in English cricket season by Tich Freeman in 1928"
        }]
    },

    "ip": {
        "function": "ip",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 6,
            "length": [1],
        },
        "info": "Gathers information of the given ip!",
        "syntax": "ip <domain/ip>",
        "example": [{
            "input": "ip google.com",
            "output": ":printer:  **| We found info for your ip! ```IP: 216.58.218.238\ncity: Mountain View\nregion: California\ncountry: US\nloc: 37.4192,-122.0574\norg: AS15169 Google LLC```**"
        }]
    },

    "bitcoin": {
        "function": "bitcoin",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 6,
            "length": [0],
        },
        "info": "Find out how much bitcoin is worth at the moment!",
        "syntax": "bitcoin",
        "example": [{
            "input": "bitcoin",
            "output": ":dollar:   **| At the moment one Bitcoin is worth ```USD: $17194.68\nGBP: \xc2\xa312673.94\nEUR: \xe2\x82\xac14294.35```**"
        }]
    },

    "strawpoll": {
        "function": "strawpoll",
        "admin": False,
        "args": {
            "delimeter": "|",
            "split": 99,
            "length": [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
        },
        "info": "Create strawpoll",
        "syntax": "strawpoll <question>|<answer1>|....|<answer19>|<answer20>",
        "example": [{
            "input": "strawpoll Best color?|Blue|Green|White|Yellow",
            "output": "**Here's your poll,** https://www.strawpoll.me/14780850"
        }]
    },

    "8ball": {
        "function": "eight_ball",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Answers your questions",
        "syntax": "8ball <question>",
        "example": [{
            "input": "8ball To be or not to be?",
            "output": "**:8ball: Signs point to yes**"
        }]
    },

    "nicknames": {
        "function": "get_nicknames",
        "admin": True,
        "args": {
            "delimeter": " ",
            "split": 0,
            "length": [0],
        },
        "info": "Get a list of users nicknames!",
        "syntax": "nicknames ?<user>",
        "example": [{
            "input": "nicknames",
            "output": "**Nicknames: Your_name, Your_nickname**"
        },
        {
            "input": "nicknames User",
            "output": "**Nicknames: User_name, User_nickname**"
        }]

    },

    "choose": {
        "function": "choose",
        "admin": False,
        "args": {
            "delimeter": "|",
            "split": 999,
            "length": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        },
        "info": "Make the bot choose for you!",
        "syntax": "choose <option1>|...|<option19>|<option20>",
        "example": [{
            "input": "choose cs:go|LoL|Osu!|Fortnite",
            "output": ":game_die: **| LoL**"
        }]

    },

    "dice": {
        "function": "dice",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Rolls the dice!",
        "syntax": "dice",
        "example": [{
            "input": "dice",
            "output": ":game_die: **| Dice rolled 1**"
        }]

    },

    "online": {
        "function": "online",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 2,
            "length": [0],
        },
        "info": "Shows bots online time and restarts",
        "syntax": "online",
        "example": [{
            "input": "online",
            "output": ":clock10: **| bot has been online for 21 minutes and has been restarted 1337 times**"
        }]
    },

    "server": {
        "function": "server_stats",
        "admin": True,
        "args": {
            "delimeter": None,
            "split": 2,
            "length": [0],
        },
        "info": "Shows information about the server!",
        "syntax": "server",
        "example": [{
            "input": "server",
            "output": "asdasdads **| adsadsasdadsasd**"
        }]

    },

    "meme": {
        "function": "meme",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 4,
            "length": [0,1,2],
        },
        "info": "Get a random meme",
        "syntax": "meme",
        "example": [{
            "input": "meme",
            "output": ":joy: **| Here's your meme, ID:1** https://youtu.be/K_9wZIBXQZo"
        },
        {
            "input": "meme 21",
            "output": ":joy: **| Here's your meme, ID:21** https://youtu.be/LCaNwS1UPVE"
        },
        {
            "input": "meme add https://kjeh.fi/JAegh",
            "output": ":joy: | Meme added with ID:25"
        }]

    },

    "roll": {
        "function": "roll",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1,2],
        },
        "info": "Get a random meme",
        "syntax": "roll",
        "example": [{
            "input": "roll",
            "output": "29"
        },
        {
            "input": "roll 999",
            "output": "373"
        },
        {
            "input": "roll 1000 10000",
            "output": "6311"
        }]
    },

    "tuplat": {
        "function": "tuplat",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Shows your roll stats",
        "syntax": "tuplat",
        "example": [{
            "input": "tuplat",
            "output": ":game_die:  **| <stats>**"
        },
        {
            "input": "tuplat [name]",
            "output": ":game_die:  **| <stats>**"
        }]

    },

    "roulette": {
        "function": "roulette",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [1,2],
        },
        "info": "Roulette your points!",
        "syntax": "roulette <amount>",
        "example": [{
            "input": "roulette 69",
            "output": "** :slot_machine:  | You have lost 69 memes, you now have 1337 memes! <:feelsrageman:318490463323553795>**"
        }]
    },

    "fish": {
        "function": "fishing",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Go fishing and try out your luck!",
        "syntax": "fish <amount>",
        "example": [{
            "input": "fish 20",
            "output": "** ZZZZ**"
        }]
    },

    "bj": {
        "function": "black_jack",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [1],
        },
        "info": "Play blackjack!",
        "syntax": "blackjack <amount>",
        "example": [{
            "input": "blackjack 69",
            "output": "**<Opens blackjack menu>**"
        }]
    },

    "slots": {
        "function": "slot_machine",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
    },

    "shop": {
        "function": "shop",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0],
        },
        "info": "Roulette your points!",
        "syntax": "shop",
        "example": [{
            "input": "shop",
            "output": "Opens the shop menu!"
        }]
    },

    "guess": {
        "function": "guess",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [0],
        },
        "info": "Guess a number, minigame!",
        "syntax": "guess",
        "example": [{
            "input": "guess 4",
            "output": "Sorry. It is actually 6."
        }]
    },

    "transfer": {
        "function": "transfer_points",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 5,
            "length": [0,1,2],
        },
        "info": "Transfer point to another user!",
        "syntax": "transfer <user> <amount>",
        "example": [{
            "input": "!transfer Bot 200",
            "output": ":white_check_mark: **| Transaction successful!**"
        }]
    },

    "duel": {
        "function": "duel",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 5,
            "length": [2],
        },
        "info": "Challenge another user to a duel!",
        "syntax": "duel <user> <amount>",
        "example": [{
            "input": "!duel Bot 200",
            "output": ":crossed_swords: **| Bot won 40 memes!**"
        }]
    },

    "osu": {
        "function": "osu_player",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Get Osu! players information!",
        "syntax": "osu <name>",
        "example": [{
            "input": "osu",
            "output": ":crossed_swords: **| Bot won 40 memes!**"
        }]
    },

    "urban": {
        "function": "urban",
        "admin": False,
        "args": {
            "delimeter": None,
            "split": 0,
            "length": [1],
        },
        "info": "Gets definition from Urban dictionary!",
        "syntax": "urban <query>",
        "example": [{
            "input": "urban urban",
            "output": "**Definition for: urban**"
        }]
    },

    "help": {
        "function": "commands_help",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Opens the help menu!",
        "syntax": "help ?<command>",
        "example": [{
            "input": "help",
            "output": "Shows all commands"
        },
        {
            "input": "help roulette",
            "output": "Shows roulette commands info"
        }]
    },

    "ao": {
        "function": "ao_ruoka",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 2,
            "length": [0,1],
        },
        "info": "Shows the food in jao services!",
        "syntax": "ao ?<week>",
        "example": [{
            "input": "ao",
            "output": "Shows the food of the day!"
        },
        {
            "input": "ao week",
            "output": "Shows the food of the week!"
        }]
    },

    "selfrole": {
        "function": "selfrole",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 3,
            "length": [2],
        },
        "info": "Assign roles to yourself!",
        "syntax": "selfrole ?<role>",
        "example": [{
            "input": "selfrole",
            "output": "Opens Role menu"
        },
        {
            "input": "selfrole nsfw",
            "output": "Role NSFW has been assigned to you!"
        }]
    },

    "ether": {
        "function": "ether",
        "admin": False,
        "args": {
            "delimeter": " ",
            "split": 6,
            "length": [0],
        },
        "info": "Get the price of Ether!",
        "syntax": "ether",
        "example": [{
            "input": "ether",
            "output": "Give you ethers rates!"
        }]
    }
}
