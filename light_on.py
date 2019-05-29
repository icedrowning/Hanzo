#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
#assert "bilibili" in driver.title
elem = driver.find_element_by_xpath(".//*[@id='banner_link']/div[1]/div[1]/form[1]/input")
elem.clear()
elem.send_keys("星星点灯")
elem.send_keys(Keys.RETURN)
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
elem = driver.find_element_by_xpath(".//*[@id='server-search-app']/div[2]/div[2]/div[1]/div[2]/ul[5]/li[1]/a")
elem.send_keys(Keys.RETURN)
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
elem = driver.find_element_by_xpath(".//*[@id='bilibiliPlayer']/div[1]/div[1]/div[8]/video")
#elem.send_keys(Keys.RETURN)
print(elem)
ActionChains(driver).click(elem).perform()

