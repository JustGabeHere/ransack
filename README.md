# Ransack - Instagram Bot

### A bot that scrapes Reddit (the superior site) for memes and then posts them, every 6 hours, on Instagram


### Context:
I don't really like programming in Python, but thought, eh, might as well try make a bot.
I also don't condone this sort of thing since you can get banned for it...

I'm calling this `V1`, even though technically, it is the second version in it's lifetime. Everything in the first version was combined in a single file - making it messy & unrealable - and broke after 4*8+ hours due to incorrect error handling.

For anyone that is actually interested in the code, I've *attempted* to document as much of it as I can, but I can't guarantee that everyone can understand my terrible commenting skills.

Also! Initially, this script was to be kept closed-sourced, but I decided against it because I don't tend to use Instagram as a serious social-media platform and I am fine with people using this code for whatever.

### Prerequisites:
	* Instagram account
	* Reddit account & developer API access (not that hard
	* PRAW - The API Wrapper that I used to get the *funny* memes from the subreddit
	* Instabot - Another API wrapper/emulator that we'll be using to post onto the instagram account

#### Customization of the scrpt isn't that hard, as most of the configuration is within the `config.json` file.

### Features (or whatever I made it do..)
	* Steals ~10 memes from Reddit (r/memes) - Both the amount & subreddit can be changed within the code
	* Posts 1 meme at a time, with a ~6 hour gap between


### Features in the future (?):
	* Implement OCR (Optical Character Recognition) to scan the image for words (like 'Reddit', or 'Instagram') and NOT use that image.  
	* All the variables that may be changed by the user should be transferred over to the `config.json`, instead of some being laid out within the python code itself
	* Alternating captions for images (placed within the config.json) instead of 1, fixed, caption.

