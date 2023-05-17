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


file = "good"
i="0"
flag = True


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
                elif character == 'ampersand' :
                    temp=temp.replace('ampersand','&')
    return temp




# predefined URL
url = "https://eip4uat1.lntecc.com/eiproot/login"
driver = webdriver.Chrome(executable_path="C:\\Users\\Manikandan\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(url)
driver.maximize_window()
time.sleep(4)
#temporary code starts 
advanced = driver.find_element(By.XPATH,'//*[@id="details-button"]')
advanced.click()
time.sleep(1)
proceed = driver.find_element(By.XPATH,'//*[@id="proceed-link"]')
proceed.click()
time.sleep(3)
#temporary code ends 

other_user = driver.find_element(By.XPATH,'/html/body/app-root/div/div[2]/app-login/div/form/div/div/div[1]/div/div[2]/div[1]/div/div[1]/ul/li[2]/a')
other_user.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.click()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
try:
    print("Recognizing")
    text = r.recognize_google(audio)
    
    print("you said:", text)
except sr.UnknownValueError:
    print("sorry , i could not understand")
except sr.RequestError as e:
    print("Error:" , str(e))

conversion = convert_special_char(text)
trimtext = conversion.split(" ")
username.send_keys("".join(trimtext))

#username.send_keys("mmurali")
password = driver.find_element(By.XPATH, '//*[@id="password-field"]')
password.click()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
try:
    print("Recognizing")
    text = r.recognize_google(audio)
    
    print("you said:", text)
except sr.UnknownValueError:
    print("sorry , i could not understand")
except sr.RequestError as e:
    print("Error:" , str(e))

conversion = convert_special_char(text)
trimtext = conversion.split(" ")
password.send_keys("".join(trimtext))

#password.send_keys("A110w#40E1p&uat")
time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="login-submit"]')
login.click()
#temporary code starts 
time.sleep(3)
session = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/eipmessagebox/div/div[3]/button')
session.click()
#temporary code ends
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
time.sleep(3) #pakka
issue_type_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/mat-option[5]/span')
issue_type_option.click()
priority = driver.find_element(By.XPATH, '//*[@id="ICpriority"]')
priority.click()
time.sleep(1)
priority_option = driver.find_element(By.XPATH, '//*[@id="mat-option-24"]/span/span')
priority_option.click()
time.sleep(500)


'''
# function to fill in login credentials and click login button
def fill_credentials(username, password):
    try:
        username_field = driver.find_element_by_id("Username")
        password_field = driver.find_element_by_id("Password")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
    except:
        print("Could not fill in login credentials or click login button.")

# loop for continuous voice recognition
while True:
    # get login credentials
    with sr.Microphone() as source:
        print("Speak your username...")
        audio = r.listen(source)
    try:
        username = r.recognize_google(audio)
        with sr.Microphone() as source:
            print("Speak your password...")
            audio = r.listen(source)
        try:
            password = r.recognize_google(audio)
            print(f"Logging in with username '{username}' and password '{password}'...")
            open_url()
            fill_credentials(username, password)
            break
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Speech Recognition service; {e}")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Speech Recognition service; {e}")
        '''
