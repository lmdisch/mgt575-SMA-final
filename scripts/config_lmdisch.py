# Twitter login info
USER = 'lmdisch'
PASSWORD = '6FfwnoRn4TgJUrP'

#Twitter API Credentials
APP_KEY	= 'F8Ornv1s0lus0fWhwwJdq3e0f'	
APP_SECRET	= 'gSP1fW8YkFH2zVRvzak91EThOiD5sc7VEmCYeao1D8Qrb2krK2'	
OAUTH_TOKEN	= '1260056478859264006-GAcyXDABFgaTdl1oda5koVbvq9Sje4'	
OAUTH_TOKEN_SECRET= 'COstqVqZgMMoEjm4Hugi3WB7IumyhpIGEW8jF6sLjTAGx'	


# Paths
DRIVER_PATH = 'scripts/chromedriver.exe'
TWITTER_LOGIN = "https://twitter.com/login/"
FOLLOWER_URL = "https://twitter.com/{}/followers/"
FOLLOWING_URL = "https://twitter.com/{}/following/"
USER_URL = 'https://twitter.com/{}/'

# XPaths
## Commands
XHEIGHT = "return document.body.scrollHeight"
XSCROLL = 'window.scrollTo(0, document.body.scrollHeight);'

## Followers
XFOLLOWERS = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div[1]'
XFOLLOWING = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[6]/div/div/div/div[2]/div/div[1]/a/div/div[2]/div/span'
XFOLLOWERS_LIST = '//div[@dir="ltr"]'

## Login
XLOGIN = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
XPASS = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
XCLICK = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'

## Tweets
XTWEET = '//div[@data-testid="tweet"]'
XUSERNAME = './/span'
XHANDLE = './/span[contains(text(), "@")]'
XDATE = './/time'
XCOMMENT = './/div[2]/div[2]/div[1]'
XRESPONSE = './/div[2]/div[2]/div[2]'
XLIKE = './/div[@data-testid="like"]'
XREPLY = './/div[@data-testid="reply"]'
XRETWEET = './/div[@data-testid="retweet"]'
XID = './/a[contains(@href, "/status/")]'
XEMOJI = './/img[contains(@src, "emoji")]'
