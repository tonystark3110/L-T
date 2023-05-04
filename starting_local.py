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
time.sleep(8)
create_indent = driver.find_element(By.XPATH, '//*[@id="ibtINDADD"]')
create_indent.click()
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
