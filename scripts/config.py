# Twitter login info
USER = 'enter your username here'
PASSWORD = 'enter your password here'

#Twitter API Credentials
APP_KEY	= 'enter your app key here'	
APP_SECRET	= 'enter your app secret here'	
OAUTH_TOKEN	= 'enter your oauth token here'	
OAUTH_TOKEN_SECRET= 'enter your oauth token secret here'	


# Paths
DRIVER_PATH = 'enter your driver path here'
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
