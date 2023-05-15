from selenium import webdriver
import pickle

import Integrator
import Speech2Txt
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

newdriver = None


def open_whatsapp():
    global newdriver
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\rafik\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # Path to chrome profile
    driver = webdriver.Chrome(executable_path="D:\\Ain Shams University\\Junior\\Semester 6\\Artificial Intelligence\\Project essentials\\chromedriver.exe", options=options)
    driver.get("http://web.whatsapp.com")
    #input()

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

def Open_mic():
    Speech2Txt.listen()
    Integrator.gestureChooser_main("SPIDERMAN SIGN", [False], ["Whatsapp"])
    file = open("Whatsapp.txt", "r")
    lines = file.readlines()
    new_lines = []
    for line in lines:
        if "SPIDERMAN" not in line.strip():
            new_lines.append(line)
    file.close()
    file = open("Whatsapp.txt", "w")
    file.writelines(new_lines)
    file.close()
    with open("Whatsapp.txt") as f_input:
        data = f_input.read().rstrip('\n')
    with open("Whatsapp.txt", 'w') as f_output:
        f_output.write(data)
def send_whatsapp_message_mic(message):
    inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    input_box = newdriver.find_element(By.XPATH, inp_xpath)
    time.sleep(2)
    # input_box.click()
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)