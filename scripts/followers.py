from scripts.config_zlisto import *
from multiprocessing import cpu_count, Pool
from selenium import webdriver
from time import sleep
from typing import *


__author__ = 'zlisto'


results = []

class Network:


    @classmethod
    def login(cls, user: str = None, password: str = None, driver=None) -> None:
        """
        Helper function to automatically log-in to Twitter using credentials
        :param user:
        :param password:
        :param driver:
        :return:
        """
        user = USER if not isinstance(user, str) else user
        password = PASSWORD if not isinstance(password, str) else password
        driver.get(TWITTER_LOGIN)
        sleep(3)
        driver.find_element_by_xpath(XLOGIN).send_keys(user)
        driver.find_element_by_xpath(XPASS).send_keys(password)
        driver.find_element_by_xpath(XCLICK).click()

    @classmethod
    def fetch_browser(cls):
        return webdriver.Chrome(executable_path=DRIVER_PATH)

    @classmethod
    def _fetch(cls, user: str) -> List[str]:
        """
        Helper-function for multi-threading
        :param user:
        :return:
        """
        follower_list = []
        driver = Network.fetch_browser()
        Network.login(driver=driver)
        driver.get(FOLLOWER_URL.format(user))
        last_height = driver.execute_script(XHEIGHT)
        while True:
            driver.execute_script(XSCROLL)
            sleep(1)
            new_height = driver.execute_script(XHEIGHT)
            if new_height == last_height:
                break
            last_height = new_height
            following = driver.find_element_by_xpath(XFOLLOWERS)
            usernames = following.find_elements_by_xpath(XFOLLOWERS_LIST)
            for username in usernames:
                username = username.text
                try:
                    if username[0] == '@':
                        follower_list.append(username)
                except:
                    pass
        return list(set(follower_list))

    @classmethod
    def log_result(cls, result) -> None:
        """
        Callback method for joining results
        :param result:
        :return:
        """
        results.append(result)

    @classmethod
    def multi_fetch(cls, users: List[str]) -> Dict[str, List[str]]:
        """

        Usage: data = Network.multi_fetch(users=["zlisto", "J_P_Vielma"])
        :param users:
        :return:
        """
        pool = Pool(processes=cpu_count())
        for k in range(0, len(users)):
            pool.apply_async(Network._fetch, args={users[k]}, callback=Network.log_result)
        pool.close()
        pool.join()
        return dict(zip(users, results))

