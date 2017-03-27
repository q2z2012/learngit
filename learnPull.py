#this is a test flie
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("username").send_keys("selenium")
#this is not right,and not test
