# webdriver provides interface for interacting with web browsers
# service is used to manage web driver
# by is used to search for elements

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import dotenv_values

config = dotenv_values(".env")
username = config.get("MY_USERNAME")
password = config.get("MY_PASSWORD")

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

#open the login page
driver.get("https://shopee.com.my/user/purchase/")

#select language
language_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "language-selector"))
)
language_dropdown.click()

# wait for the page to load after language selection
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

#select the desired language
language_option = driver.find_element(By.XPATH, "//option[text()='English']")
language_option.click()

# find the username and password fields and login button
username_box = driver.find_element(By.NAME, "username")
password_box = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.NAME, "login")    

# Enter credentials and submit
username_box.send_keys(username)
password_box.send_keys(password)
login_button.click()



# driver.quit