
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https:/google.com')
time.sleep(3)
print('strona:' , driver.title)

#robimy na dwa rzuty
#wez znajdz ten element
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
# print(button1_accept)
# print(type(button1_accept))
# hej teraz go nacisnij

search_field = driver.find_element("name", 'q')
# name="q"
search_field.send_keys('Ile lat ma Anna Lewandowska ? ')
#
search_field.send_keys(Keys.ENTER)


# klikamy szukaj w google
#search_button = driver.find_element('name', 'btnK')
#search_button.send_keys(Keys.ENTER)

#zrob mi zrzut ekranu

driver.get_screenshot_as_file('_zrzut_ekranu.png')



time.sleep(2)
driver.quit()

