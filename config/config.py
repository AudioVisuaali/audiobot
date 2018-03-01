# BOT AUTH
BOT_TOKEN = ""
OWNER_ID = [""]

# WEATHER API https://openweathermap.org/
WEATHER_API = ""

#OSU api key
#https://osu.ppy.sh/p/api REMEBER TO LOG IN
OSU_KEY = ""

# Google api
GOOGLE_KEY = ""
GOOGLE_KEY_MAPS = ""
GOOGLE_API_KEY = ""
GOOGLE_KEY_SEARCH = ""
DEFAULT_TRANSLATE_LANGUAGE = "en"

#Twitter KEYS
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# COMMANDS
COMMAND_START = "!"
LOGS = "YAY" # YAY OR NAYCOMING SOON

# bank
BANK_KORKO = 5 # 5%
BANK_INTEREST_DAY = 1 # Day monday = 0 ->>
BANK_INTEREST_TIME = 0 # Seconds

# Daily
DAILY_AMOUNT_MIN = 400
DAILY_AMOUNT_MAX = 450
DAILY_WAIT_TIME = 24 #In hours

# Lotto
START_DAY_RAFFLE = 0
START_TIME_RAFFLE = 48600
END_DAY_RAFFLE = 6
END_TIME_RAFFLE = 64800

SELECT_DAY_RAFFLE = 6
SELECT_TIME_RAFFLE = 72000

# message points
MESSAGE_POINTS_MAX = 25
MESSAGE_POINTS_MIN = 15
MESSAGE_MEMES_MIN = 2
MESSAGE_MEMES_MAX = 2
MESSAGE_COMMAND_POINTS_MAX = 15
MESSAGE_COMMAND_POINTS_MIN = 5
MESSAGE_COMMAND_MEMES_MIN = 1
MESSAGE_COMMAND_MEMES_MAX = 1
MESSAGE_POST_LEVEL_ACHIEVEMENT = False

# ROULETTE
ROULETTE_MIN_POINTS = 10 # Min poits to roulette
ROULETTE_WINRATE = 50 #51 = 51% change to win
ROULETTE_SPECIAL_WINRATE = 50 # Multiplier for special rooms RIGGED
ROULETTE_RAND_LOW = 110 # 110 = 110% = 1,1x
ROULETTE_RAND_HIGH = 140 # 130 = 130% = 1,3x
ROULETTE_SPECIAL_CHANNELS = ["404356322595962880"] #channel id here multiple: ["404356322595962880", "404356322595962880"] #TODO BROKEN

# DATABASE CONNECTION INFO
MYSQL_HOST = "localhost"
MYSQL_USERNAME = "audiobot"
MYSQL_PASSWORD = "4COAekWBp6"
MYSQL_ADDRESS = "localhost"
MYSQL_DATABASE = "discord_bilbergia"
MYSQL_PORT = "3306"

EIGHT_BALL_OPTIONS = ["It is certain", "It is decidedly so", "Without a doubt",
                      "Yes definitely", "You may rely on it", "As I see it yes",
                      "Most likely", "Outlook good", "Yes",
                      "Signs point to yes", "Reply hazy try again",
                      "Ask again later", "Better not tell you now",
                      "Cannot predict now", "Concentrate and ask again",
                      "Don't count on it", "My reply is no",
                      "My sources say no", "Outlook not so good",
                      "Very doubtful"]

LENNYFACES = ["( ͡° ͜ʖ ͡°)","( ͠° ͟ʖ ͡°)","( ͡~ ͜ʖ ͡°)",
             "( ͡ʘ ͜ʖ ͡ʘ)","( ͡o ͜ʖ ͡o)","(° ͜ʖ °)",
             "( ‾ʖ̫‾)","( ಠ ͜ʖಠ)","( ͡° ʖ̯ ͡°)",
             "( ͡ಥ ͜ʖ ͡ಥ)","༼ ͡° ͜ʖ ͡° ༽","(▀̿Ĺ̯▀̿ ̿)",
             "( ✧≖ ͜ʖ≖)","(ง ͠° ͟ل͜ ͡°)ง","(͡ ͡° ͜ つ ͡͡°)",
             " [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]","(✿❦ ͜ʖ ❦)","ᕦ( ͡° ͜ʖ ͡°)ᕤ",
             "( ͡° ͜ʖ ͡°)╭∩╮","¯\_( ͡° ͜ʖ ͡°)_/¯",
             "(╯ ͠° ͟ʖ ͡°)╯┻━┻","( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
             "¯\_(ツ)_/¯","ಠ_ಠ"]

HELP_EXTERNAL_COMMANDS = [
    # Pod 1
    {
        # Heading
        "commands_heading": "Music commands!",
        #Prefix
        "command_start": "!",
        #commands
        "commands_list": ["disconnect","pause","play","queue","restart","resume","shutdown","skip","summon","volume"]
    },
]

FISHING_INVENTORY = [
        # 1
        [{
            "name": ":dvd:",
            "display_name": "DVD",
            "value": 200
        },{
            "name": ":cd:",
            "display_name": "CD",
            "value": 150
        },{
            "name": ":medal:",
            "display_name": "Medal",
            "value": 100
        },{
            "name": ":blowfish:",
            "display_name": "Blowfish",
            "value": 80
        },{
            "name": ":fish:",
            "display_name": "Fish",
            "value": 55
        },{
            "name": ":tropical_fish:",
            "display_name": "Tropical Fish",
            "value": 75
        }],

        # 2
        [{
            "name": ":eggplant:",
            "display_name": "Eggplant",
            "value": 20
        },{
            "name": ":peach:",
            "display_name": "Peach",
            "value": 25
        },{
            "name": ":banana:",
            "display_name": "Banana",
            "value": 18
        },{
            "name": ":pizza:",
            "display_name": "Pizza",
            "value": 17
        },{
            "name": ":rice_cracker:",
            "display_name": "Rice Cracker",
            "value": 22
        }],

        # 3
        [{
            "name": ":soccer:",
            "display_name": "Soccer",
            "value": 1
        },{
            "name": ":boot:",
            "display_name": "Boots",
            "value": 5
        },{
            "name": ":coffin:",
            "display_name": "Coffin",
            "value": 4
        },{
            "name": ":paperclip:",
            "display_name": "Paperclip",
            "value": 1
        },{
            "name": ":mag_right:",
            "display_name": "Magnifying Glass",
            "value": 5
        },{
            "name": ":shopping_cart:",
            "display_name": "Shopping Cart",
            "value": 5
        },{
            "name": ":lock:",
            "display_name": "Lock",
            "value": 4
        },{
            "name": ":triangular_ruler:",
            "display_name": "Triangular Ruler",
            "value": 1
        },{
            "name": ":poop:",
            "display_name": "PASKAA",
            "value": 2
        },{
            "name": ":mans_shoe:",
            "display_name": "Shoe",
            "value": 1
        },{
            "name": ":umbrella:",
            "display_name": "Umbrella",
            "value": 4
        }]
]
