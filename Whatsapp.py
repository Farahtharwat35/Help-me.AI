
from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


# def open_whatsapp_and_send_message(person, message):
#     driver = open_whatsapp()
#     search_for_contact(person, driver)
#     send_whatsapp_message(message, driver)
newdriver = None

def open_whatsapp():
    global newdriver
    driver = webdriver.Chrome()
    driver.get("http://web.whatsapp.com")
    input()
    newdriver = driver


def search_for_contact(person):
    input_box_search: webelement = WebDriverWait(newdriver, 65).until(EC.presence_of_element_located((By.XPATH,
                         '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]')))

    input_box_search.send_keys(Keys.CONTROL, 'a')
    input_box_search.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    input_box_search.send_keys(person)
    time.sleep(2)
    input_box_search.send_keys(Keys.ENTER)

def send_whatsapp_message(message):
    inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    input_box = newdriver.find_element(By.XPATH, inp_xpath)
    time.sleep(2)
    # input_box.click()
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)