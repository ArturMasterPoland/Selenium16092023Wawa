from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/v1/')

time.sleep(2)
print('strona', driver.title)


user = driver.find_element("name", 'user-name')
time.sleep(1)
user.click()
user.clear()
user.send_keys('standard_user')

password = driver.find_element("name", 'password')
password.click()
password.clear()
password.send_keys('secret_sauce')


login_button = driver.find_element("id", 'login-button')
if not login_button.get_attribute('disabled'): # czy przycisk jest aktywny
    login_button.click()

def make_screenshot(okno_przegladarki):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'screen'+ short_date + '.png'
    okno_przegladarki.get_screenshot_as_file(screen_name)


driver.quit()