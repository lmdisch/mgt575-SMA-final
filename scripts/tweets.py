import chromedriver_autoinstaller
import logging
import pandas as pd
import random
import re
from scripts.config import *
from scripts.followers import Network
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import *
from typing import *

__author__ = 'zlisto'


COLUMNS = ['screen_name',
           'handle',
           'created_at',
           'text',
           'emojis',
           'reply_count',
           'retweet_count',
           'like_count',
           'id_str']


class Fetch:

    @classmethod
    def create_driver(cls) -> webdriver.chrome.webdriver.WebDriver:
        """
        Browser-less chromedriver
        """
        chromedriver_path = chromedriver_autoinstaller.install()
        options = Options()
        options.add_argument('--disable-gpu')
        options.headless = True
        options.add_argument('log-level=3')
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)
        driver.set_page_load_timeout(100)
        return driver

    @classmethod
    def construct_query(cls, words: List[str], start_date: str, end_date: str, lang: str = "en",
                        to_account: str = None, from_account: str = None, hashtag: str = None) -> str:
        """
        Create advanced search query
        """
        end_date = pd.datetime.today().strftime('%Y-%m-%d') if not isinstance(end_date, str) else end_date
        words = "(" + str('%20OR%20'.join(str(words).split("//"))) + ")%20" if isinstance(words, str) else ""
        from_account = "(from%3A" + from_account + ")%20" if from_account is not None else ""
        to_account = "(to%3A" + to_account + ")%20" if to_account is not None else ""
        hash_tags = "(%23" + hashtag + ")%20" if hashtag is not None else ""
        lang = 'lang%3A' + lang if lang is not None else ""
        end_date = "until%3A" + end_date + "%20"
        start_date = "since%3A" + start_date + "%20"
        return 'https://twitter.com/search?q=' + words + from_account + to_account + \
               hash_tags + end_date + start_date + lang + '&src=typed_query'

    @classmethod
    def _extract(cls, source, xpath: str) -> str:
        """
        Extract element, otherwise return empty string
        """
        try:
            data = source.find_element_by_xpath(xpath)
        except:
            data = ""
        return data

    @classmethod
    def _extract_emojis(cls, tag: webdriver.remote.webelement.WebElement) -> List[str]:
        """
        Use regex to extract emojis from text
        """
        try:
            filename = tag.get_attribute('src')
            emoji = chr(int(re.search(r'svg\/([a-z0-9]+)\.svg', filename).group(1), base=16))
            return emoji if emoji else ''
        except:
            pass

    @classmethod
    def extract(cls, source) -> pd.Series:
        """
        Extract fields of interest from tweet
        """
        username = Fetch._extract(source, XUSERNAME).text
        handle = Fetch._extract(source, XHANDLE).text
        postdate = Fetch._extract(source, XDATE).get_attribute('datetime')
        comment = Fetch._extract(source, XCOMMENT).text
        responding = Fetch._extract(source, XRESPONSE).text
        text = comment + responding
        like_cnt = Fetch._extract(source, XLIKE).text
        reply_cnt = Fetch._extract(source, XREPLY).text
        retweet_cnt = Fetch._extract(source, XRETWEET).text
        id_str = Fetch._extract(source, XID).get_attribute('href').split('/')[-1]
        emoji_tags = Fetch._extract(source, XEMOJI)
        if isinstance(emoji_tags, webdriver.remote.webelement.WebElement):
            emojis = Fetch._extract_emojis(emoji_tags)
        else:
            emojis = ''
        data = [username, handle, postdate, text, emojis, reply_cnt, retweet_cnt, like_cnt, id_str]
        return pd.Series(dict(zip(COLUMNS, data)))

    @classmethod
    def fetch_tweets(cls, word: str, start_date: str, end_date: str, limit: int = 10,
                    headless: bool = False) -> pd.DataFrame:
        """
        Fetch tweets for tuples of (keyword, start date, end date)
        Usage:
        tweets = Fetch.fetch_tweets(word='coronavirus', start_date = '2021-01-01', end_date = '2021-01-02', limit=5)
        """
        counter, ids, records = 0, [], []
        query = Fetch.construct_query(words=word, start_date=start_date, end_date=end_date)
        driver = Network.fetch_browser() if not headless else Fetch.create_driver()
        driver.get(query)
        last_height = driver.execute_script(XHEIGHT)
        while len(set(ids)) < limit:
            tweets = driver.find_elements_by_xpath(XTWEET)
            for tweet in tweets:
                record = Fetch.extract(tweet)
                tweet_id = record.loc['id_str']
                if tweet_id not in list(set(ids)):
                    records.append(record)
                    ids.append(tweet_id)
            driver.execute_script(XSCROLL)
            sleep(random.expovariate(1 / random.uniform(1, 2)))
            new_height = driver.execute_script(XHEIGHT)
            if new_height == last_height:
                break
            last_height = new_height
        if len(records) > 0:
            return pd.concat(records, axis=1).T.head(limit)
        else:
            logging.error('Failed to scrape, possibly due to rate limit. Please try again.')
