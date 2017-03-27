#this is a test flie
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
import time
time.sleep(2)
driver.quit()
#this is not right,and not test
