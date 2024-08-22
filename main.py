# webdriver provides interface for interacting with web browsers
# service is used to manage web driver
# by is used to search for elements

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")

# #locating and interacting with elements
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("Selenium" + Keys.ENTER)

time.sleep(10)

driver.quit