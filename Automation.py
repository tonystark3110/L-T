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
r = sr.Recognizer()


def texttospeech(text, filename):
    filename = filename + '.mp3'
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return

def speechtotext(duration):
    global i, addr, passwrd
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        # texttospeech("speak", file + i)
        # i = i + str(1)
        playsound('speak.mp3')
        audio = r.listen(source, phrase_time_limit=duration)
    try:
        response = r.recognize_google(audio)
    except:
        response = 'N'
    return response


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
username.send_keys("mmurali")
password = driver.find_element(By.XPATH, '//*[@id="password-field"]')
password.click()
password.send_keys("E210a#04P1e&bfix")
login = driver.find_element(By.XPATH, '//*[@id="login-submit"]')
login.click()
time.sleep(3)
session = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/eipmessagebox/div/div[3]/button')
session.click()
time.sleep(9)
create_indent = driver.find_element(By.XPATH, '//*[@id="ibtINDADD"]')
create_indent.click()
time.sleep(2)
warehouse = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCWarehouse"]')
warehouse.click()
time.sleep(4)
warehouse_option = driver.find_element(By.XPATH, '//*[@id="mat-option-26"]/span/span')
warehouse_option.click()
time.sleep(4)  
stock_job = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCAccountingCentre"]')
stock_job.click()
time.sleep(1)
stock_job_option = driver.find_element(By.XPATH, '//*[@id="mat-option-48"]/span/span')
stock_job_option.click()
time.sleep(3)  
indent_type = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCIndentType"]')
indent_type.click()
time.sleep(3)
indent_type_option = driver.find_element(By.XPATH, '//*[@id="mat-option-94"]/span')
indent_type_option.click()
time.sleep(3)
issue_type = driver.find_element(By.XPATH, '//*[@id="ActxtboxINDCIssueType"]')
issue_type.click()
time.sleep(3)
issue_type_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/mat-option[5]/span')
issue_type_option.click()
priority = driver.find_element(By.XPATH, '//*[@id="ICpriority"]')
priority.click()
time.sleep(1)
priority_option = driver.find_element(By.XPATH, '//*[@id="mat-option-24"]/span/span')
priority_option.click()
time.sleep(500)
