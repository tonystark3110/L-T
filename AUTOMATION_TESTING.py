import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import os
from keyboard import press, release
r = sr.Recognizer()
from vosk import Model, KaldiRecognizer
import pyaudio
import json


model = Model('C:\\Users\\20325730\\Desktop\\speech_rec\\vosk-model-en-in-0.5')
recognizer = KaldiRecognizer(model, 16000)

word_replacements = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "eye": "i",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "2",
    "thirty": "3",
    "forty": "4",
    "fifty": "5",
    "sixty": "6",
    "seventy": "7",
    "eighty": "8",
    "ninety": "9",
    "eye" : " i",
    "tree" : "3"
}

def perform_speech_recognition():


    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    

    print("Listening...")

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break

        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_json = json.loads(result)
            recognized_text = result_json["text"]

            # Convert recognized words to integers and apply word replacements
            recognized_numbers = recognized_text.split()
            for i, word in enumerate(recognized_numbers):
                if word.isdigit():
                    recognized_numbers[i] = str(int(word))
                elif word in word_replacements:
                    recognized_numbers[i] = word_replacements[word]

            # Print the recognized text with spaces
            recognized_text = " ".join(recognized_numbers)
            break

    text_1 = recognized_text.replace(" ", "")
    print(text_1)
    return text_1


   

def convert_special_char(text):
    special_char_map = {
        'dot': '.',
        'underscore': '_',
        'dollar': '$',
        'hash': '#',
        'star': '*',
        'plus': '+',
        'minus': '-',
        'space': '',
        'dash': '-'
    }

    for character, replacement in special_char_map.items():
        text = text.replace(character, replacement)

    return text


url = "https://eip4bfix.lntecc.com/EIPSCMUI/SOPUI/indent-request/indentReq"
chrome_driver_path = "C:\\Users\\20325730\\Desktop\\ZZZ\\chromedriver_win32\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
driver.maximize_window()
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Optional: Run the browser in headless mode


other_user = driver.find_element(By.XPATH,'/html/body/app-root/div/div[2]/app-login/div/form/div/div/div[1]/div/div[2]/div[1]/div/div[1]/ul/li[2]/a')
other_user.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.click()
username.send_keys("nmanikandan")
password = driver.find_element(By.XPATH, '//*[@id="password-field"]')
password.click()
password.send_keys("E210a#04P1e&bfix")
login = driver.find_element(By.XPATH, '//*[@id="login-submit"]')
login.click()
time.sleep(3)
session = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/eipmessagebox/div/div[3]/button')
session.click()
time.sleep(5)
create_indent = driver.find_element(By.XPATH, '//*[@id="ibtINDADD"]')
create_indent.click()
time.sleep(2)
job = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[1]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
job.click()



while True:
    try:
        text_2 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCJob"]')  
        Jobcode.clear()
        Jobcode.send_keys(text_2)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_2 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_2)
            Jobcode = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCJob"]')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue



time.sleep(1)

warehouse = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCWarehouse"]')
warehouse.click()
time.sleep(1)
while True:
    try:
        text_3 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[2]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
        Jobcode.clear()
        Jobcode.send_keys(text_3)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_3 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_3)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[2]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue

time.sleep(2)  
stock_job = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCAccountingCentre"]')
stock_job.click()
pyautogui.press('backspace')
pyautogui.press('backspace')

while True:
    try:
        text_4 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[3]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
        Jobcode.clear()
        Jobcode.send_keys(text_4)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_4 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_4)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[3]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue
time.sleep(3)  
indent_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
indent_type.click()

while True:
    try:
        text_5 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
        Jobcode.clear()
        Jobcode.send_keys(text_5)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_5 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_5)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue

issue_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[2]/eipautocomplete/mat-form-field/div/div[1]/div/input')
issue_type.click()

while True:
    try:
        text_6 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[2]/eipautocomplete/mat-form-field/div/div[1]/div/input')
        Jobcode.clear()
        Jobcode.send_keys(text_6)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_6 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_6)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[2]/eipautocomplete/mat-form-field/div/div[1]/div/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue

time.sleep(2) 

#priority = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[3]/eipautocomplete/mat-form-field/div/div[1]/div/input')
#priority.click()                          
#time.sleep(1)
#priority_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span')
#priority_option.click()                         
#time.sleep(2)
next = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[3]/div/div/button[2]')
next.click()
cart = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td/div/div/i')
time.sleep(1)
cart.click()
time.sleep(1)
material_group = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
time.sleep(1)
material_group.click()
while True:
    try:
        text_7 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
        Jobcode.clear()
        Jobcode.send_keys(text_7)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_7 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_7)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue

time.sleep(1)
select  = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[2]/eipgeneralcart/div/div/div[1]/div/div[2]/mat-selection-list/mat-list-option/div/div[2]')
select.click()
time.sleep(1)
select_all = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[2]/eipgeneralcart/div/div/div[1]/div/div[2]/div/div[2]/div/button[1]/i')
select_all.click() 
time.sleep(1)
post = driver.find_element(By.XPATH, ' /html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[2]/eipgeneralcart/div/div/div[2]/div/div[3]/button')       
post.click()     
time.sleep(2)                     
HSN = driver.find_element(By.XPATH, ' /html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[3]/eipautocomplete/mat-form-field/div/div[1]/div/input')
HSN.click()
while True:
    try:
        text_8 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[3]/eipautocomplete/mat-form-field/div/div[1]/div/input')
        Jobcode.clear()
        Jobcode.send_keys(text_8)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_8 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_8)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[3]/eipautocomplete/mat-form-field/div/div[1]/div/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue

time.sleep(2)
tax_type = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[4]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
tax_type.click()
while True:
    try:
        text_9 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[4]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
        Jobcode.clear()
        Jobcode.send_keys(text_9)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_9 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_9)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[4]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue

expand_list = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[10]/div/i')
expand_list.click()
cost_package = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input')
cost_package.click()
time.sleep(1)
while True:
    try:
        text_10 = perform_speech_recognition()
        Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input')
        Jobcode.clear()
        Jobcode.send_keys(text_10)
        elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

        for element in elements:
            if text_10 in element.text:
                element.click()
                break
        else:
            print("Invalid input detected:", text_10)
            Jobcode = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input')
            Jobcode.clear()
            print("Retrying...")
            continue

        # If the loop reaches here, the input was found successfully
        break

    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
        continue
time.sleep(2)
press('enter')

time.sleep(1)
indent_qty = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[4]/mat-form-field/div/div[1]/div/input')
indent_qty.click()
while True:
    try:
        qty = perform_speech_recognition()
        indent_qty.send_keys(qty)
        break  
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")


time.sleep(1)
next_next = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[3]/div/div/button[3]')
next_next.click()
time.sleep(2)
submit = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[3]/div/div/button[3]')
submit.click()

time.sleep(500)
