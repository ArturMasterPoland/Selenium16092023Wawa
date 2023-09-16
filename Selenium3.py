from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon

#funkcja bedzie czekac na id

def czekaj_na_id (element_id):
    timeout = 5 #czekaj do 5 sekund i jak przekroczysz to komunikat
    timeout_message = f'Element o ID {element_id} nie pojawil sie w czasie {timeout} s.'# info jak sie nie pojawi
    lokalizator = (By.ID, element_id) # krotka dwu elementowa
    znaleziono = excon.visibility_of_element_located(lokalizator) # spr czy element jest znaleizony
    oczekiwator = WebDriverWait(driver, timeout) # jak dlugo masz czkeac i gdzie
    return oczekiwator.until(znaleziono, timeout_message) # zwrotka

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com')

try:
    login_button = czekaj_na_id('login-button')
except TimeoutException:
    print('Nie znaleziono')
else:
    print('Znaleziono')
finally:

    driver.quit()


