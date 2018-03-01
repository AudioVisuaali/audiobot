from config import COMMAND_START as starter
from requests import get as rget
from datetime import datetime
from bs4 import BeautifulSoup
from random import randint

#Gives the food of the week
async def ao_ruoka(message, client, arguments):

        # Variables
        food, add_food_with_this, letter, count = [], [], "", 0

        # PAge address
        page = rget("https://www.jao.fi/fi/Jyvaskylan-koulutuskuntayhtyma/Asiakaspalvelut/Palvelut-Jyvaskylassa/Opiskelijaravintolat/Lounastuuli")
        soup = BeautifulSoup(page.content, "lxml")
        kappa = soup.find_all("div", {"class": "day"})

        # for each day in week
        for asd in kappa:

            # Adding weekday
            KEEPO = asd.find("span", {"class": "dayname"})
            KAPPA = KEEPO.text.title()
            add_food_with_this.append("__" + KAPPA + "__:")

            # For each lunch in day
            for auto in asd.find_all("span", {"class": "lunch"}):
                auto = auto.text
                add_food_with_this.append(auto)

            # add day
            food.append(add_food_with_this)
            add_food_with_this = []

        if len(arguments) == 0:
            # Format
            for weekday in food:

                # Indent if todays food
                wrapper = ""
                if datetime.today().weekday() == count and count < 5:
                    wrapper = "**"

                    # Wrapping
                    letter += wrapper + "\n".join(weekday) + wrapper + "\n\n__{}ao week__ for the whole week!".format(starter)
                elif datetime.today().weekday() >= 5 and count == 5:
                    letter += wrapper + "\n".join(weekday) + wrapper + "\n\nThis is for the next weeks mondays food!\n__{}ao week__ for the whole week!".format(starter)
                count += 1

        else:
            # Format
            for weekday in food:

                # Indent if todays food
                if count == 5:
                    letter += "**=====================\n\n**"

                # Wrapping
                letter += "\n".join(weekday) + "\n\n"
                count += 1

        # Send message
        if not letter == "":
            await client.send_message(message.channel, letter)

def get_food_for_main():

        # Variables
        food, add_food_with_this, letter, count = [], [], "", 0

        # PAge address
        page = rget("https://www.jao.fi/fi/Jyvaskylan-koulutuskuntayhtyma/Asiakaspalvelut/Palvelut-Jyvaskylassa/Opiskelijaravintolat/Lounastuuli")
        soup = BeautifulSoup(page.content, "lxml")
        kappa = soup.find_all("div", {"class": "day"})

        # for each day in week
        for asd in kappa:

            # Adding weekday
            dayname = asd.find("span", {"class": "dayname"})
            dayname_title = dayname.text.title()
            add_food_with_this.append("__{}__:".format(dayname_title))

            # For each lunch in day
            for auto in asd.find_all("span", {"class": "lunch"}):
                auto = auto.text
                add_food_with_this.append(auto)

            # add day
            food.append(add_food_with_this)
            add_food_with_this = []

                # Format
        for weekday in food:

                    # Indent if todays food
            if datetime.today().weekday() < 5:
                wrapper = ""

                if datetime.today().weekday() == count:
                    wrapper = "**"

                    # Wrapping
                    letter += wrapper + "\n".join(weekday) + wrapper + "\n\n"
            count += 1

        # Send message
        #await client.send_message(message.channel, letter)

        if not letter == "":
            return "{}".format(letter)
