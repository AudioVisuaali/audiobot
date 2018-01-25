from audiovisuaali import send
from config import OSU_KEY as osu_api_key
from json import loads
from urllib.request import quote
from requests import get as rget


# OSU STATS
async def osu_player(message, client, arguments):

    # definitions
    platform = "pc"

    # Fetching user information
    url = "https://osu.ppy.sh/api/get_user?u={}&k={}".format(quote(arguments), osu_api_key)
    data = loads(rget(url).text)
    if not data:
        return

    # Forming message
    send = "Osu stats for "+data[0]["username"]+"```PP"+" "*12+str(round(float(data[0]["pp_raw"])))+" PP\nLevel"+" "*9+str(round(float(data[0]["level"]),1))+" lvl\nGlobal rank"+" "*3+data[0]["pp_rank"]+"\nCountry rank"+" "*2+data[0]["pp_country_rank"]+"\nCountry"+" "*7+data[0]["country"]+"\nAccuracy"+" "*6+str(round(float(data[0]["accuracy"]), 2))+" %\nRanked Score"+" "*2+data[0]["ranked_score"]+"\nTotal Score"+" "*3+data[0]["total_score"]+"```"

    #' '.join([a[i:i+3] for i in range(0, len(a), 3)])
    # FOR CONVERTING LARGE NUMBERS

    await client.send_message(message.channel, "<@"+message.author.id+"> "+send)
    send(1, "Fetching data for osu profile done!")
    return
