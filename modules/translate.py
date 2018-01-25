from audiovisuaali import send

from config import DEFAULT_TRANSLATE_LANGUAGE as translate_to_lang
from config import GOOGLE_API_KEY as google_api

from urllib.request import quote
from requests import get as rget
from json import loads

from re import search as rsearch
from re import sub as rsub

# Translate uses google translate
async def translate(message, client, arguments):

    #Cheking if input contains any arguments DO NOT TOUCH WAS PAIN
    try:
        popped = rsearch("--([a-zA-Z0-9])\w+", arguments).group()
    except AttributeError:
        google = quote(str(arguments))
        language = translate_to_lang
    else:
        google = quote(str(rsub(r"--([a-zA-Z0-9])\w+", "", arguments)))
        language = popped[2:]

    #Creating and fetching link
    query = "https://translation.googleapis.com/language/translate/v2?key=%s&target=%s&q=%s" % (google_api, language, google)
    response = loads(rget(query).text)

    # Trying to create message
    try:
        detectedlanguage = response["data"]["translations"][0]["detectedSourceLanguage"]
        translatedtext = response["data"]["translations"][0]["translatedText"]
        letter = ":cloud:  **| " + detectedlanguage.upper() + " -> " + language.upper() + "  `" + translatedtext + "`**"

    # if can't create mesage rteturn error
    except KeyError:
        letter = ":cloud:  **| Invalid language target!**"

    # sending message
    await client.send_message(message.channel, letter)
