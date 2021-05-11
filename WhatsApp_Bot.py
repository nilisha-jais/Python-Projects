#Example of web automation

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random
chrome=webdriver.Chrome(ChromeDriverManager().install())

time.sleep(2)

chrome.get("https://web.whatsapp.com")
print("start scan")

time.sleep(20)

print("Scan completed")
search_box = chrome.find_element_by_class_name("_2_1wd")
search_box.send_keys("User_name")
search_box.send_keys(Keys.ENTER)
emoji = [":-)", ";-)", ">_<", ":-(","^_^"]

for i in range(0,20):
    message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys(random.choice(emoji))
    message_box.send_keys(Keys.ENTER)