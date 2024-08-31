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

#wait for the language button to be clickable
language_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'English') and contains(@class, 'shopee-button-outline--primary-reverse')]"))
)

#click the language button
language_button.click()

# wait for the username field to be be present after language selection
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='loginKey']"))
    )

# find and interact with the login fields and button
username_box = driver.find_element(By.NAME, "loginKey")
password_box = driver.find_element(By.NAME, "password")

# Enter credentials and submit
username_box.send_keys(username)
password_box.send_keys(password)

#Wait for the login button to be enabled
login_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.vvOL40.iesrPs.AsFRg8.qCI4rz.ZKayWA.AnY7KS"))

)

login_button.click()



# driver.quit