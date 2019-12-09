import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


# get the path of ChromeDriverServer
dir = "C:\\Users\\Admin\\PycharmProjects\\rasabot1"
chrome_driver_path = dir + "\\chromedriver.exe"

__author__ = 'Hanon'
class Selenium_Test(unittest.TestCase):
    def test_Selenium_Unit_Test(self):
        # create a new Chrome session
        # options = Options()
        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        #
        # driver = webdriver.Chrome(chrome_driver_path, options=options)

        driver = webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(30)
        driver.maximize_window()

        # chatbot testing simulation
        time.sleep(12)
        driver.get('http://sidwebpage.s3.us-east-2.amazonaws.com/website/index.html')
        print(driver.current_url)
        time.sleep(3)
        driver.refresh()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="webchat"]/div/button').click()
        driver.find_element_by_class_name("new-message")
        wait = WebDriverWait(driver, 10)
        Mousepointer = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="webchat"]/div/div/form/input')))

        print("Mousepointer value{0}".format(Mousepointer.tag_name))
        Mousepointer.send_keys("Hi")

        time.sleep(2)
        Mousepointer.send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="webchat"]/div/div/form/button/img').click()
        time.sleep(5)
        # displaying and validating value
        ExpectedReply = "Hey! How are you Easwar?"
        Reply = driver.find_element_by_xpath('//*[@id="messages"]/div[2]/div/div/div/p/span').text
        print(Reply)

        self.assertEqual(Reply, ExpectedReply)
        print("Success")




if __name__ == '__main__':
    unittest.main()
