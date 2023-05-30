import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
    "eye" : " i"
}

def perform_speech_recognition():


    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=16384)
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

    text_2 = recognized_text.replace(" ", "")
    print(text_2)
    return text_2


   

def convert_special_char(text):
    temp=text
    special_chars = ['dot','underscore','dollar','hash','star','plus','minus','space','dash']
    for character in special_chars:
        while(True):
            pos=temp.find(character)
            if pos == -1:
                break
            else :
                if character == 'dot':
                    temp=temp.replace('dot','.')
                elif character == 'underscore':
                    temp=temp.replace('underscore','_')
                elif character == 'dollar':
                    temp=temp.replace('dollar','$')
                elif character == 'hash':
                    temp=temp.replace('hash','#')
                elif character == 'star':
                    temp=temp.replace('star','*')
                elif character == 'plus':
                    temp=temp.replace('plus','+')
                elif character == 'minus':
                    temp=temp.replace('minus','-')
                elif character == 'space':
                    temp = temp.replace('space', '')
                elif character == 'dash':
                    temp=temp.replace('dash','-')
    return temp



url = "https://eip4bfix.lntecc.com/EIPSCMUI/SOPUI/indent-request/indentReq"
chrome_driver_path = "C:\\Users\\20325730\\Desktop\\ZZZ\\chromedriver_win32\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
driver.maximize_window()

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


my_dict_1 = {
    "1153": '/html/body/div[2]/div[3]/div/div/mat-option/span/span',
    
}

while True:
    try:
        text_2 = perform_speech_recognition()
        
        if text_2 in my_dict_1:
            job.send_keys(text_2)
            break  
            
        else:
            print("Invalid input detected:", text_2)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")


if text_2 in my_dict_1:
    value_1 = my_dict_1[text_2]
    print("Value:", value_1)
else:
    print("Key not found in the dictionary.")
    


job_option = driver.find_element(By.XPATH, value_1)
time.sleep(2)
job_option.click()
warehouse = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCWarehouse"]')
warehouse.click()
time.sleep(1)
my_dict_2 = {

 "1562" : '/html/body/div[2]/div[3]/div/div/mat-option/span/span' ,        
 "1563" : '/html/body/div[2]/div[3]/div/div/mat-option[2]/span',
 "1565" : '/html/body/div[2]/div[3]/div/div/mat-option[3]/span/span',
 "1567" : '/html/body/div[2]/div[3]/div/div/mat-option[4]/span/span',
 "3116" : '/html/body/div[2]/div[3]/div/div/mat-option[5]/span/span',
}
while True:
    try:
        text_4 = perform_speech_recognition()
        
        if text_4 in my_dict_2:
            warehouse.send_keys(text_4)
            break 
            
        else:
            print("Invalid input detected:", text_4)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")

if text_4 in my_dict_2:
    value_2 = my_dict_2[text_4]
    print("Value:", value_2)
else:
    print("Key not found in the dictionary.")


warehouse_option = driver.find_element(By.XPATH, value_2)
warehouse_option.click()
time.sleep(2)  
stock_job = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCAccountingCentre"]')
stock_job.click()
pyautogui.press('backspace')
pyautogui.press('backspace')

my_dict_3 = {
    "1153": '/html/body/div[2]/div[3]/div/div/mat-option/span/span',
    "000011": '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span'
    
}
while True:
    try:
        text_3 = perform_speech_recognition()
        
        if text_3 in my_dict_3:
            stock_job.send_keys(text_3)
            break 
            
        else:
            print("Invalid input detected:", text_3)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")



if text_3 in my_dict_3:
    value_3 = my_dict_3[text_3]
    print("Value:", value_3)
else:
    print("Key not found in the dictionary.")


stock_job_option = driver.find_element(By.XPATH, value_3)
stock_job_option.click()
time.sleep(3)  
indent_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
indent_type.click()
my_dict_4 = {

   "general" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span',
    "plant and machinery" : '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span',
    "Linear Indent" : '/html/body/div[2]/div[3]/div/div/mat-option[3]/span/span',
    "Non Linear" :    '/html/body/div[2]/div[3]/div/div/mat-option[4]/span/span',
    "Maintenance Linear" : '/html/body/div[2]/div[3]/div/div/mat-option[5]/span/span',
    "Maintenance Non Linear" : '/html/body/div[2]/div[3]/div/div/mat-option[6]/span/span'
}
while True:
    try:
        text_5 = perform_speech_recognition()
        
        if text_5 in my_dict_4:
            indent_type.send_keys(text_5)
            break  
            
        else:
            print("Invalid input detected:", text_5)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")

if text_5 in my_dict_4:
    value_4 = my_dict_4[text_5]
    print("Value:", value_4)
else:
    print("Key not found in the dictionary.")

time.sleep(2)

indent_type_option = driver.find_element(By.XPATH, value_4)
indent_type_option.click()

issue_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[2]/eipautocomplete/mat-form-field/div/div[1]/div/input')
issue_type.click()

my_dict_5 = {

"31" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span',
"33" : '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span',
"61" : '/html/body/div[2]/div[3]/div/div/mat-option[3]/span/span',
"63" : '/html/body/div[2]/div[3]/div/div/mat-option[4]/span/span',
"70" : '/html/body/div[2]/div[3]/div/div/mat-option[5]/span',
"101" : '/html/body/div[2]/div[3]/div/div/mat-option/span/span',
"102" : '/html/body/div[2]/div[3]/div/div/mat-option[7]/span/span'
}

while True:
    try:
        text_6 = perform_speech_recognition()
        
        if text_6 in my_dict_5:
            issue_type.send_keys(text_6)
            break  
            
        else:
            print("Invalid input detected:", text_6)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")



if text_6 in my_dict_5:
    value_5 = my_dict_5[text_6]
    print("Value:", value_5)
else:
    print("Key not found in the dictionary.")

time.sleep(2) 
issue_type_option = driver.find_element(By.XPATH, value_5)
issue_type_option.click()
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
my_dict_6 = {

   "3806" : '/html/body/div[2]/div[5]/div/div/mat-option/span/span'

}

while True:
    try:
        text_7 = perform_speech_recognition()
        
        if text_7 in my_dict_6:
            material_group.send_keys(text_7)
            break  
            
        else:
            print("Invalid input detected:", text_7)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")
if text_7 in my_dict_6:
    value_6 = my_dict_6[text_7]
    print("Value:", value_6)
else:
    print("Key not found in the dictionary.")

material_group_option = driver.find_element(By.XPATH,  value_6)
material_group_option.click()
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
my_dict_7 = {
    "diodes": '/html/body/div[2]/div[3]/div/div/mat-option[1]',
    "spark" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span'
    
}
while True:
    try:
        text_8 = perform_speech_recognition()
        
        if text_8 in my_dict_7:
            HSN.send_keys(text_8)
            break  
            
        else:
            print("Invalid input detected:", text_8)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")



if text_8 in my_dict_7:
    value_7 = my_dict_7[text_8]
    print("Value:", value_7)
else:
    print("Key not found in the dictionary.")

HSN_options = driver.find_element(By.XPATH, value_7)
HSN_options.click()
time.sleep(2)
tax_type = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[4]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
tax_type.click()
my_dict_8 = {

   "18" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span',
    "12" : '/html/body/div[2]/div[3]/div/div/mat-option/span/span',
    "5" : '/html/body/div[2]/div[3]/div/div/mat-option/span',
    "0" :    '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span',
    "28" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span',
    "6" : '/html/body/div[2]/div[3]/div/div/mat-option/span/span/span'
}
while True:
    try:
        text_9 = perform_speech_recognition()
        
        if text_9 in my_dict_8:
            tax_type.send_keys(text_9)
            break 
            
        else:
            print("Invalid input detected:", text_9)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")

if text_9 in my_dict_8:
    value_8 = my_dict_8[text_9]
    print("Value:", value_8)
else:
    print("Key not found in the dictionary.")

time.sleep(1)
tax_type_options = driver.find_element(By.XPATH,value_8)
tax_type_options.click()
expand_list = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[10]/div/i')
expand_list.click()
cost_package = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input')
cost_package.click()
time.sleep(1)
my_dict_9 = {

   "acss" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span'
    
}
while True:
    try:
        text_10 = perform_speech_recognition()
        
        if text_10 in my_dict_9:
            cost_package.send_keys(text_10)
            break  
            
        else:
            print("Invalid input detected:", text_10)
            print("Retrying...")
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Retrying...")



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
