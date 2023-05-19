import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from gtts import gTTS
import os
from playsound import playsound
from keyboard import press
r = sr.Recognizer()
from vosk import Model, KaldiRecognizer
import pyaudio
import json

#text_2 = "FCWI1153"
text_3 = "FCWI1153"
text_4 = "1562"
text_5 = "general"
#spot="fcw"


model = Model('C:\\Users\\20325730\\Desktop\\speech_rec\\vosk-model-en-us-0.22')
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
    "nine": "9"
    # Add more word replacements as needed
}

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




# predefined URL
url = "https://eip4bfix.lntecc.com/EIPSCMUI/SOPUI/indent-request/indentReq"
driver = webdriver.Chrome(executable_path="C:\\Users\\20325730\\Desktop\\ZZZ\\chromedriver_win32\\chromedriver.exe")
driver.get(url)
driver.maximize_window()
#time.sleep(1000)

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

text_2 = recognized_text.replace(" ","")

job.send_keys(text_2)
time.sleep(2)
#
#
#my_dict_1 = {
#"FGADM019" :  '/html/body/div[2]/div[3]/div/div/mat-option[1]/span  '     , 
#"FGADM043" :  '/html/body/div[2]/div[3]/div/div/mat-option[2]/span',
#"FGASP012" :  '/html/body/div[2]/div[3]/div/div/mat-option[3]/span/span',
#"AZ000011" :  '/html/body/div[2]/div[3]/div/div/mat-option[4]/span/span',
#"FBFD1178" :  '/html/body/div[2]/div[3]/div/div/mat-option[5]/span/span',
#"LE16D156" :  '/html/body/div[2]/div[3]/div/div/mat-option[6]/span/span',
#"FOFAC147" :  '/html/body/div[2]/div[3]/div/div/mat-option[7]/span/span',
#"LE16D099" :  '/html/body/div[2]/div[3]/div/div/mat-option[8]/span/span',
#"LZ000010" :  '/html/body/div[2]/div[3]/div/div/mat-option[9]/span/span',
#"FCBAF014" :  '/html/body/div[2]/div[3]/div/div/mat-option[10]/span/span',
#"FKBMH011" :  '/html/body/div[2]/div[3]/div/div/mat-option[11]/span/span',
#"CZ000011" :  '/html/body/div[2]/div[3]/div/div/mat-option[12]/span/span',
#"FGMAP014" :  '/html/body/div[2]/div[3]/div/div/mat-option[13]/span/span',
#"MZ000010" :  '/html/body/div[2]/div[3]/div/div/mat-option[14]/span/span',
#"LE090263" :  '/html/body/div[2]/div[3]/div/div/mat-option[15]/span/span',
#"FGADM051" :  '/html/body/div[2]/div[3]/div/div/mat-option[16]/span/span',
#"LE090414" :  '/html/body/div[2]/div[3]/div/div/mat-option[17]/span',
#"LE130461" :  '/html/body/div[2]/div[3]/div/div/mat-option[18]/span',
#"LE090262" :  '/html/body/div[2]/div[3]/div/div/mat-option[19]/span/span',
#"LE090415" :  '/html/body/div[2]/div[3]/div/div/mat-option[20]/span',
#"LE120641" :  '/html/body/div[2]/div[3]/div/div/mat-option[18]/span/span',
#"LE120642" :  '/html/body/div[2]/div[3]/div/div/mat-option[22]/span',
#"LE090413" :  '/html/body/div[2]/div[3]/div/div/mat-option[23]/span/span',
#"LE120591" :  '/html/body/div[2]/div[3]/div/div/mat-option[24]/span/span',
#"LE120643" :  '/html/body/div[2]/div[3]/div/div/mat-option[25]/span/span',
#"LE120590" :  '/html/body/div[2]/div[3]/div/div/mat-option[26]/span/span',
#"LE120644" :  '/html/body/div[2]/div[3]/div/div/mat-option[27]/span/span',
#"LE110335" :  '/html/body/div[2]/div[3]/div/div/mat-option[28]/span/span',
#"LE120589" :  '/html/body/div[2]/div[3]/div/div/mat-option[29]/span/span',
#"FOLD1162" :  '/html/body/div[2]/div[3]/div/div/mat-option[30]/span/span',
#"FSEDR014" :  '/html/body/div[2]/div[3]/div/div/mat-option[31]/span/span',
#"FBFD1180" :  '/html/body/div[2]/div[3]/div/div/mat-option[32]/span/span',
#"FGFAC014" :  '/html/body/div[2]/div[3]/div/div/mat-option[31]/span/span',
#"FOFAC062" :  '/html/body/div[2]/div[3]/div/div/mat-option[34]/span/span',
#"FGRMO010" :  '/html/body/div[2]/div[3]/div/div/mat-option[35]/span/span',
#"FGRMO029" :  '/html/body/div[2]/div[3]/div/div/mat-option[36]/span/span',
#"FGFAA036" :  '/html/body/div[2]/div[3]/div/div/mat-option[37]/span/span',
#"FOFAA025" :  '/html/body/div[2]/div[3]/div/div/mat-option[38]/span/span',
#"FGFAA015" :  '/html/body/div[2]/div[3]/div/div/mat-option[39]/span/span',
#"FOLD1170" :  '/html/body/div[2]/div[3]/div/div/mat-option[40]/span/span',
#"FCWI1152" :  '/html/body/div[2]/div[3]/div/div/mat-option[41]/span',
#"LE080228" :  '/html/body/div[2]/div[3]/div/div/mat-option[42]/span/span',
#"FZ000011" :  '/html/body/div[2]/div[3]/div/div/mat-option[43]/span/span',
#"LE120466" :  '/html/body/div[2]/div[3]/div/div/mat-option[44]/span/span',
#"FOFAC070" :  '/html/body/div[2]/div[3]/div/div/mat-option[45]/span/span',
#"FGADM027" :  '/html/body/div[2]/div[3]/div/div/mat-option[46]/span/span',
#"FGADM035" :  '/html/body/div[2]/div[3]/div/div/mat-option[47]/span',
#"FGADM065" :  '/html/body/div[2]/div[3]/div/div/mat-option[48]/span/span',
#"HZ000011" :  '/html/body/div[2]/div[3]/div/div/mat-option[49]/span',
#"FOFAC151" :  '/html/body/div[2]/div[3]/div/div/mat-option[50]/span/span',
#"FGINS016" :  '/html/body/div[2]/div[3]/div/div/mat-option[51]/span/span',
#"LE120461" :  '/html/body/div[2]/div[3]/div/div/mat-option[52]/span/span',
#"LE170412" :  '/html/body/div[2]/div[3]/div/div/mat-option[53]/span',
#"LE140305" :  '/html/body/div[2]/div[3]/div/div/mat-option[54]/span/span',
#"FCWI1153" :  '/html/body/div[2]/div[3]/div/div/mat-option[55]/span',
#"FGISD010" :  '/html/body/div[2]/div[3]/div/div/mat-option[56]/span/span',
#"FGFGS017" :  '/html/body/div[2]/div[3]/div/div/mat-option[57]/span/span',
#"FGMDS012" :  '/html/body/div[2]/div[3]/div/div/mat-option[58]/span/span',
#"FGMDS020" :  '/html/body/div[2]/div[3]/div/div/mat-option[59]/span/span',
#"LE100420" :  '/html/body/div[2]/div[3]/div/div/mat-option[60]/span',
#"FGMAP030" :  '/html/body/div[2]/div[3]/div/div/mat-option[61]/span',
#"FGMAP022" :  '/html/body/div[2]/div[3]/div/div/mat-option[62]/span',
#"BZ000011" :  '/html/body/div[2]/div[3]/div/div/mat-option[63]/span/span',
#"FGPOD010" :  '/html/body/div[2]/div[3]/div/div/mat-option[64]/span/span',
#"FOFAC097" :  '/html/body/div[2]/div[3]/div/div/mat-option[65]/span',
#"FOFAC125" :  '/html/body/div[2]/div[3]/div/div/mat-option[66]/span',
#"FGPAM013" :  '/html/body/div[2]/div[3]/div/div/mat-option[67]/span/span',
#"FGPDN017" :  '/html/body/div[2]/div[3]/div/div/mat-option[68]/span',
#"FGFAC030" :  '/html/body/div[2]/div[3]/div/div/mat-option[69]/span',
#"FOFAC089" :  '/html/body/div[2]/div[3]/div/div/mat-option[70]/span/span',
#"FOFAC138" :  '/html/body/div[2]/div[3]/div/div/mat-option[71]/span/span',
#"FOFAC111" :  '/html/body/div[2]/div[3]/div/div/mat-option[72]/span/span',
#"LE100419" :  '/html/body/div[2]/div[3]/div/div/mat-option[73]/span/span',
#"FGPTO011" :  '/html/body/div[2]/div[3]/div/div/mat-option[74]/span/span',
#"OZ000010" :  '/html/body/div[2]/div[3]/div/div/mat-option[75]/span/span',
#"LE15D067" :  '/html/body/div[2]/div[3]/div/div/mat-option[76]/span/span',
#"FGQCA025" :  '/html/body/div[2]/div[3]/div/div/mat-option[77]/span/span',
#"LE100421" :  '/html/body/div[2]/div[3]/div/div/mat-option[78]/span/span',
#"FGQCA017" :  '/html/body/div[2]/div[3]/div/div/mat-option[79]/span/span',
#"FOFAC150" :  '/html/body/div[2]/div[3]/div/div/mat-option[80]/span/span',
#"FGFMO010" :  '/html/body/div[2]/div[3]/div/div/mat-option[81]/span/span',
#"FOFAC146" :  '/html/body/div[2]/div[3]/div/div/mat-option[82]/span/span',
#"FGRPG015" :  '/html/body/div[2]/div[3]/div/div/mat-option[83]/span/span',
#"FGSAF015" :  '/html/body/div[2]/div[3]/div/div/mat-option[84]/span      ',
#"SZ000010" :  '/html/body/div[2]/div[3]/div/div/mat-option[85]/span/span',
#"LE150322" :  '/html/body/div[2]/div[3]/div/div/mat-option[86]/span/span',
#"LE190131" :  '/html/body/div[2]/div[3]/div/div/mat-option[87]/span/span',
#"LE181290" :  '/html/body/div[2]/div[3]/div/div/mat-option[88]/span',
#"LE160264" :  '/html/body/div[2]/div[3]/div/div/mat-option[89]/span/span',
#"FGTAX018" :  '/html/body/div[2]/div[3]/div/div/mat-option[90]/span/span',
#"FGTRC010" :  '/html/body/div[2]/div[3]/div/div/mat-option[91]/span/span',
#"LE100286" :  '/html/body/div[2]/div[3]/div/div/mat-option[92]/span/span',
#"FWWET016" :  '/html/body/div[2]/div[3]/div/div/mat-option[93]/span/span',
#"FOFAC103" :  '/html/body/div[2]/div[3]/div/div/mat-option[94]/span/span'
#  }
#
#
#if text_2 in my_dict_1:
#    value_1 = my_dict_1[text_2]
#    print("Value:", value_1)
#else:
#    print("Key not found in the dictionary.")
#
#
#
#time.sleep(2)
 
my_dict_1 = {
    "1153": '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span'
    
    
}

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
time.sleep(2)
my_dict_2 = {

 "1562" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span' ,        
 "1563" : '/html/body/div[2]/div[3]/div/div/mat-option[2]/span',
 "1565" : '/html/body/div[2]/div[3]/div/div/mat-option[3]/span/span',
 "1567" : '/html/body/div[2]/div[3]/div/div/mat-option[4]/span/span',
 "3116" : '/html/body/div[2]/div[3]/div/div/mat-option[5]/span/span',
}

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
time.sleep(2)

my_dict_3 = {
    "FCWI1153": '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span',
    "FZ000011": '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span'
    
}


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

if text_5 in my_dict_4:
    value_4 = my_dict_4[text_5]
    print("Value:", value_4)
else:
    print("Key not found in the dictionary.")

time.sleep(2)

indent_type_option = driver.find_element(By.XPATH, value_4)
indent_type_option.click()
time.sleep(2)
issue_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[2]/eipautocomplete/mat-form-field/div/div[1]/div/input')
issue_type.click()
time.sleep(2)
issue_type_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/mat-option[6]/span')
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
material_group.send_keys("rope")
material_group_option = driver.find_element(By.XPATH, ' /html/body/div[2]/div[5]/div/div/mat-option/span/span/span')
material_group_option.click()
select_all = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[2]/eipgeneralcart/div/div/div[1]/div/div[2]/div/div[2]/div/button[2]/i')
select_all.click() 
time.sleep(1)
post = driver.find_element(By.XPATH, ' /html/body/div[2]/div[4]/div/mat-dialog-container/app-general-cart-popup/div[2]/div[2]/eipgeneralcart/div/div/div[2]/div/div[3]/button')       
post.click()     
time.sleep(2)                     
HSN = driver.find_element(By.XPATH, ' /html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[3]/eipautocomplete/mat-form-field/div/div[1]/div/input')
HSN.click()
HSN_options = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span')
HSN_options.click()
time.sleep(2)
tax_type = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[4]/div/eipautocomplete/mat-form-field/div/div[1]/div/input')
tax_type.click()
time.sleep(1)
tax_type_options = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/mat-option[2]/span')
tax_type_options.click()
expand_list = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[10]/div/i')
expand_list.click()
cost_package = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input')
cost_package.click()
time.sleep(1)
cost_package.send_keys("acs")
time.sleep(2)
press('enter')

time.sleep(3)
cost_package_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[1]/kendo-combobox/span/kendo-searchbar/input')
cost_package_option.click()
time.sleep(1)
indent_qty = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[4]/mat-form-field/div/div[1]/div/input')
indent_qty.click()
indent_qty.send_keys("1")
time.sleep(1)
next_next = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[3]/div/div/button[3]')
next_next.click()
time.sleep(2)
submit = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[3]/div/div/button[3]')
submit.click()




                  







time.sleep(500)
