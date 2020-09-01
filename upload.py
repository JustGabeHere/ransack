# === Ransack === #
# === The ultimate script for your botting needs === #

# = upload.py = #
#  -- Main half of the whole script. Periodically (every ~6 hours) uploads a meme to instagram using the configuration file while also making sure to call the downloads file once the folder is low on images.. = #

# --- IMPORTS --- #
import time
import json
import glob
import random
import requests
import datetime
import os, os.path

import download as d 

from instabot import Bot

# --- VARIABLE DECLARATIONS --- #
bot = None
data = None
captions = None


# --- MAIN ENTRY --- #
# (METHOD) Setup Everything - Config, Reddit, Instagram
def setup():
    print('---[SETUP]---')

    global reddit
    global bot
    global subreddit
    global data
    global captions

    # -- Open the config file and define the data variable to contain the data for it
    print('---[SETUP]: Loading config data ---')
    with open("config.json", "r") as file:
        data = json.load(file)     
        
    captions = data['instagram']['captions']
    
    print('---[SETUP]: Setting up INSTABOT ---')
    bot = Bot()
    bot.login(
        username = data['instagram']['u'],
        password = data['instagram']['p'],
    )

# (METHOD) Post meme
def postMeme(picture):
    _caption = random.choice(captions) # - Get a random caption from the list in the configuration file
    post = bot.upload_photo(picture, caption=_caption) # Upload it
    
                    # - Check if the upload was successful
    if not post:
        os.remove(picture) # - Remove from the directory
    
    print("[POST]: Picture has been uploaded to instagram")


# (METHOD) Main Entry/Loop
def main():
    loopFinished = False
    sufficientImages = False

    print('---[RANSACK - V1]---\n--[Stealing memes the right way]--')

    # -- Call the setup function
    setup()
    
    # -- Loop
    while loopFinished == False:

        # -- Get the size of the memes directory 
        pics = glob.glob("./memes/*")

        # -- If it is 2 or less, get more memes, else, continue with the script
        if len(pics) <= 2:
            # - Call the `download.py` script
            print('-- [upload.py]: Calling download script --')
            d.main()
        else:
            # -- Loop through each entry in the directory, deleting any image that has a specific suffix
            for pic in pics:
                splittedLength = len(pic.split('.'))
                ext = pic.split('.')[splittedLength-1] # Get the file extension

                # - If the extension is 'REMOVE_ME', then remove the image. (instabot automatically replaces the extension of the file to be 'REMOVE_ME' as the image is posted)
                if ext == 'REMOVE_ME':
                    os.remove(pic) # - Remove the picture from the directory
                    pics.remove(pic) # - Remove the image from the pics list (so we don't accidently use it)
                    print('[IMAGE REMOVAL]: ' + pic)
            print('-- [IMAGE CLEANUP FINISHED] --')

            # - Post the meme
            postMeme(pics[0])

            # - If the last response was NOT OK
            if bot.api.last_response.status_code != 200:
                print("[STATUS CODE]: " + bot.api.last_response)
                break

            # -- Sleep (Once the sleep is over, it will loop
            print("[TIME SLEEP]")
            time.sleep(60 * random.randrange(50, 60) * 6) # Sleep for ~6 hours (to try to break a pattern so Instagram doesn't detect that the bot is automatically posting every 6 hours, straight.
            
# --- Call
main()
