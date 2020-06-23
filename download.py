# === Ransack === #
# === The ultimate script for your botting needs === #

# = download.py = #
#  -- Latter half of the script. Handles the basic stuff of downloading atleast 10 memes from reddit, and that is pretty much it. (much of the work is done via the upload.py file (e.g. uploading, cleaning the memes folder of already posted memes, and also calling this file once the memes folder only hs 1 meme or less)

# --- IMPORTS --- #
import time
import json
import glob
import praw
import random
import requests
import datetime
import os, os.path

# --- VARIABLE DECLARATIONS --- #
MAX_MEMES = 10
reddit = None
subreddit = None
data = None

# --- MAIN ENTRY --- #
# (METHOD) Setup Everything - Config, Reddit, Instagram
def setup():
    print('---[SETUP]---')

    global reddit
    global subreddit
    global data

    # -- Open the config file and define the data variable to contain the data for it
    print('---[SETUP]: Loading config data ---')
    with open("config.json", "r") as file:
        data = json.load(file)

    print('---[SETUP]: Setting up PRAW ---')
    reddit = praw.Reddit(
        client_id = data['reddit']['client-id'],
        client_secret = data['reddit']['client-secret'],
        user_agent = data['reddit']['user_agent']
    )

    subreddit = reddit.subreddit('memes')

# (METHOD) Get MAX_MEMES from r/memes AND Download them
def getMemes():
    subredditMemes = []
    loopFinished = False
    directorySize = len([ name for name in os.listdir('./memes/') if os.path.isfile(name) ])

    print('---[DOWNLOADING THE MEMES]---')
    # -- Loop through each top submission and append to the array
    for submission in subreddit.rising(limit=MAX_MEMES):
        subredditMemes.append(submission)

    # -- Make the directory size
    while loopFinished == False:
        # -- While the directory size hasn't reached MAX_MEMES
        while not directorySize == MAX_MEMES:
            # -- Loop through all of the subreddit memes
            for meme in subredditMemes:
                # -- Download the meme to the folder
                with open('./memes/' + meme.id + '.jpg', 'wb') as handle:
                    # - Get the URL
                    response = requests.get(meme.url, stream=True)

                    # - If the response recieved is not OK
                    if not response.ok:
                        print('[RESPONSE]: ' + response)

                    # - Write the image to the drive
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)

                    directorySize += 1
                    print('[MEME DOWNLOADED]: (ID): {0} ; (LOCATION): {1} ; (URL): {2}'.format(meme.id, './memes/' + meme.id, meme.url))

        loopFinished = True






# (METHOD) Main Entry/Loop
def main():
    print('---[RANSACK - DOWNLOADING THE MEMES RIGHT AWAY]---')

    # -- Call the setup function
    setup()

    # -- Loop
    getMemes()


