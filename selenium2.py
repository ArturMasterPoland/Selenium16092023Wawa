from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementExceptione
selenium.webdriver.common.keys import Keys
import time


def make_screenshot(driver):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'screen'+ short_date + '.png'
    driver.get_screenshot_as_file(screen_name)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/v1/')

try:
    user = driver.find_element("name", 'user-name2')
except :
    print('nie znaleziono')
    user = driver.find_element("name", 'user-name')
    make_screenshot(driver)

time.sleep(1)
user.click()
user.clear()
user.send_keys('standard_user')
try:
    password = driver.find_element(By.NAME , 'password') # lub 'name'
except:
    make_screenshot(driver)
    print('nie znaleziona slowa z haslem')
    raise
password.click()
password.clear()
password.send_keys('secret_sauce')


login_button = driver.find_element("id", 'login-button')
if not login_button.get_attribute('disabled'): # czy przycisk jest aktywny
    login_button.click()



make_screenshot(driver)


driver.quit()