import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
import os
from keyboard import press
import pyaudio
import json
from vosk import Model, KaldiRecognizer
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
r = sr.Recognizer()


audio_file = r'C:\\Users\\20325730\\Desktop\\PROJECT\\yes_no.mp3'
#model = Model('C:\\Users\\20325730\\Desktop\\PROJECT\\vosk-model-en-us-0.42-gigaspeech')
model = Model('C:\\Users\\20325730\\Desktop\\PROJECT\\vosk-model-en-in-0.5')
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
    "twenty": "20",
    "thirty": "30",
    "forty": "40",
    "fifty": "50",
    "sixty": "60",
    "seventy": "70",
    "eighty": "80",
    "ninety": "90",
    "tree": "3",
    "dot": ".",
    "underscore": "_",
    "dollar": "$",
    "hash": "#",
    "star": "*",
    "plus": "+",
    "minus": "-",
    #"space": "",
    "dash": "-",
    "comma": ",",
    "and" : "&"
}



# Returning the value of input
def perform_speech_recognition():
 try:

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

 except Exception as e:
    print("Error during speech recognition:", str(e))
    return None


def input_entry(driver, xpath):
    while True:
        try:
            text_2 = perform_speech_recognition()
            if not text_2:
                # No voice input detected
                continue

            text_bar = driver.find_element(By.XPATH, xpath)
            text_bar.clear()
            text_bar.send_keys(text_2)
            elements = driver.find_elements(By.XPATH, '(//span[@class="mat-option-text"]//span)')

            option_found = False

            for element in elements:
                if text_2.lower() in element.text.lower():
                    element.click()
                    option_found = True
                    break

            if not option_found:
                print("Invalid input detected:", text_2)
                text_bar.clear()
                print("Retrying...")
                continue

            while True:
                # Prompt the user to confirm the selected option
                print("Is the selected option correct? yes or no")
                user_input = perform_speech_recognition().lower()

                if user_input == "no":
                    # Clear the text and retry input
                    text_bar.clear()
                    print("Retrying...")
                    break
                elif user_input == "yes":
                    # Continue with the selected option
                    return

                print("Invalid input. Please enter 'yes' or 'no'.")

        except Exception as e:
            print("An error occurred:", str(e))
            print("Retrying...")
            continue




url = "https://eip4dev.lntecc.com/EIPSCMUI/SOPUI/indent-request/indentReq"
chrome_driver_path = "C:\\Users\\20325730\\Desktop\\PROJECT\\chromedriver_win32\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
#driver.maximize_window()
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Optional: Run the browser in headless mode


other_user = driver.find_element(By.XPATH,'/html/body/app-root/div/div[2]/app-login/div/form/div/div/div[1]/div/div[2]/div[1]/div/div[1]/ul/li[2]/a')
other_user.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.click()
username.send_keys("mmurali")
password = driver.find_element(By.XPATH, '//*[@id="password-field"]')
password.click()
password.send_keys("Phnx@2019")
login = driver.find_element(By.XPATH, '//*[@id="login-submit"]')
login.click()
#time.sleep(3)
#session = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/eipmessagebox/div/div[3]/button')
#session.click()
time.sleep(12)
approver = driver.find_element(By.XPATH, '/html/body/app-root/div/div[2]/app-indent-container/div/dynamic-tabs/dynamic-tab/div/app-indent-landing/div/div/div[2]/kendo-grid/kendo-grid-toolbar/div/div[3]/mat-slide-toggle/label/span[1]/span/span[1]')
approver.click()
time.sleep(3)
create_indent = driver.find_element(By.XPATH, '//*[@id="ibtINDADD"]')
create_indent.click()
time.sleep(2)
job = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[1]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
job.click()


xpath1 = '//*[@id="ActxtboxINDCJob"]'
input_entry(driver, xpath1)
time.sleep(1)

xpath2 = '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[2]/div/eipautocomplete/mat-form-field/div/div[1]/div/input'
input_entry(driver, xpath2)
time.sleep(2)  

stock_job = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCAccountingCentre"]')
stock_job.click()
pyautogui.press('backspace')
pyautogui.press('backspace')

xpath3 = '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[3]/div/eipautocomplete/mat-form-field/div/div[1]/div/input'
input_entry(driver, xpath3)
time.sleep(3)

indent_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
indent_type.click()

xpath4 = '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input'
input_entry(driver, xpath4)

issue_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[2]/eipautocomplete/mat-form-field/div/div[1]/div/input')
issue_type.click()

xpath5 = '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[2]/eipautocomplete/mat-form-field/div/div[1]/div/input'
input_entry(driver, xpath5)

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

xpath6 = '/html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input'
input_entry(driver, xpath6)

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

xpath7 = '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[3]/eipautocomplete/mat-form-field/div/div[1]/div/input'
input_entry(driver, xpath7)
time.sleep(1)

time.sleep(2)
tax_type = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[4]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
tax_type.click()

xpath8 =  '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[4]/div/eipautocomplete/mat-form-field/div/div[1]/div/input'
input_entry(driver, xpath8)

expand_list = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[10]/div/i')
expand_list.click()
cost_package = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input')
cost_package.click()
time.sleep(1)

xpath9 =  '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input'
input_entry(driver, xpath9)
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
