from config import GOOGLE_API_KEY as google_api_key
from requests import get as rget
from urllib.request import quote
from math import floor as mfloor
from audiovisuaali import send
from datetime import datetime
from json import loads
from time import time

async def time_new(message, client, arguments):

    if not arguments:
        letter = ":clock11: **| Servers time is " + str(datetime.fromtimestamp(mfloor(time())).strftime('%H:%M')) + "**"
        await client.send_message(message.channel, letter)
        return


    else:
        google = quote(str(arguments))
        query = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}&language={}".format(google, google_api_key, "en")
        response = loads(rget(query).text)

        if response["status"] == "OK":

            # getting lat and lng
            lat = str(float("{0:.4f}".format(response["results"][0]["geometry"]["location"]["lat"])))
            lng = str(float("{0:.4f}".format(response["results"][0]["geometry"]["location"]["lng"])))

            # Getting time by place
            query = "https://maps.googleapis.com/maps/api/timezone/json?location=%s,%s&timestamp=%s&key=%s&language=%s" % (lat, lng, time(), google_api_key, "en")
            time_in_location = loads(rget(query).text)

            # Calculating time
            time_now = str(int(time() + time_in_location["rawOffset"] + time_in_location["dstOffset"]))
            time_in_hour_format = datetime.fromtimestamp(int(time_now)).strftime('%H:%M')
            time_in_weekday = datetime.fromtimestamp(int(time_now)).weekday()

            # Setting weekday
            if time_in_weekday == 0:
                day_is = "Monday"
            elif time_in_weekday == 1:
                day_is = "Tuesday"
            elif time_in_weekday == 2:
                day_is = "Wednesday"
            elif time_in_weekday == 3:
                day_is = "Thursday"
            elif time_in_weekday == 4:
                day_is = "Friday"
            elif time_in_weekday == 5:
                day_is = "Saturday"
            elif time_in_weekday == 6:
                day_is = "Sunday"

            # Sending message
            adsasdadsfdas = ":clock11: **| Time in {} is {} and the day is {}**".format(str(response["results"][0]["formatted_address"]), time_in_hour_format, day_is)
            await client.send_message(message.channel, adsasdadsfdas)
            return

    send(1, "Time done!")
