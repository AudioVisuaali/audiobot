# BOT AUTH

# Bot token example: Gfn3NzGXMjk3NzAgNDU2Mzk1.DFLkPA.W0N2kGqj-T0h9G5J8y4e-mirFGw
BOT_TOKEN = ""
OWNER_ID = [""]

# wolframalpha APP ID example: 66SDFG-W87WWW55WW
WOLF_KEY = ""

# WEATHER API https://openweathermap.org/ example: 34g5fvp0ku8j4g5ywfu8jpk
WEATHER_API = ""

#OSU api key
#https://osu.ppy.sh/p/api REMEBER TO LOG IN Example: 4g56ef78jkg64e5fjk87g645e87jk
OSU_KEY = ""

# OMDBAPI API KEY for imdb ratings, Not required
#http://www.omdbapi.com/
#OMDBAPI_KEY =""

# Google api
GOOGLE_KEY = ""
GOOGLE_KEY_MAPS = ""
GOOGLE_API_KEY = ""
DEFAULT_TRANSLATE_LANGUAGE = "en"

#Twitter KEYS
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# COMMANDS
COMMAND_START = "!"
LOGS = "YAY" # YAY OR NAYCOMING SOON # TODO
DAILY_AMOUNT_MIN = 380
DAILY_AMOUNT_MAX = 420
DAILY_WAIT_TIME = 24 #In hours

# ROULETTE
ROULETTE_MIN_POINTS = 10 # Min poits to roulette
ROULETTE_WINRATE = 50 #51 = 51% change to win
ROULETTE_SPECIAL_WINRATE = 50 # Multiplier for special rooms RIGGED
ROULETTE_RAND_LOW = 110 # 110 = 110% = 1,1x
ROULETTE_RAND_HIGH = 140 # 130 = 130% = 1,3x
ROULETTE_SPECIAL_CHANNELS = [""] #channel id here multiple: ["404776322595962880", "404356322533962880"]

# DATABASE CONNECTION INFO
MYSQL_HOST = ""
MYSQL_USERNAME = ""
MYSQL_PASSWORD = ""
MYSQL_ADDRESS = ""
MYSQL_DATABASE = ""
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

# TODO Add help indexing for commands
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
