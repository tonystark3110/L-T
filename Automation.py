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

text_3 = "80172"
text_4 = "general"


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
time.sleep(4)

my_dict_1 = {
    "80104": '/html/body/div[2]/div[3]/div/div/mat-option[1]/span/span',
    "80137": '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span',
    "80138": '/html/body/div[2]/div[3]/div/div/mat-option[3]/span/span',
    "80139": '/html/body/div[2]/div[3]/div/div/mat-option[4]/span/span',
    "80140": '/html/body/div[2]/div[3]/div/div/mat-option[5]/span/span',
    "80147": '/html/body/div[2]/div[3]/div/div/mat-option[6]/span/span',
    "80148": '/html/body/div[2]/div[3]/div/div/mat-option[7]/span/span',
    "80149": '/html/body/div[2]/div[3]/div/div/mat-option[8]/span/span',
    "80150": '/html/body/div[2]/div[3]/div/div/mat-option[9]/span/span',
    "80151": '/html/body/div[2]/div[3]/div/div/mat-option[10]/span/span',
    "80152": '/html/body/div[2]/div[3]/div/div/mat-option[11]/span/span',
    "80153": '/html/body/div[2]/div[3]/div/div/mat-option[12]/span/span',
    "80154": '/html/body/div[2]/div[3]/div/div/mat-option[13]/span/span',
    "80155": '/html/body/div[2]/div[3]/div/div/mat-option[14]/span/span',
    "80156": '/html/body/div[2]/div[3]/div/div/mat-option[15]/span/span',
    "80157": '/html/body/div[2]/div[3]/div/div/mat-option[16]/span/span',
    "80158": '/html/body/div[2]/div[3]/div/div/mat-option[17]/span/span',
    "80159": '/html/body/div[2]/div[3]/div/div/mat-option[18]/span/span',
    "80160": '/html/body/div[2]/div[3]/div/div/mat-option[19]/span/span',
    "80162": '/html/body/div[2]/div[3]/div/div/mat-option[20]/span/span',
    "80163": '/html/body/div[2]/div[3]/div/div/mat-option[21]/span/span',
    "80164": '/html/body/div[2]/div[3]/div/div/mat-option[22]/span/span',
    "80165": '/html/body/div[2]/div[3]/div/div/mat-option[23]/span/span',
    "80166": '/html/body/div[2]/div[3]/div/div/mat-option[24]/span',
    "80167": '/html/body/div[2]/div[3]/div/div/mat-option[25]/span',
    "80168": '/html/body/div[2]/div[3]/div/div/mat-option[26]/span/span',
    "80169": '/html/body/div[2]/div[3]/div/div/mat-option[27]/span/span',
    "80170": '/html/body/div[2]/div[3]/div/div/mat-option[28]/span/span',
    "80171": '/html/body/div[2]/div[3]/div/div/mat-option[29]/span/span',
    "80172": '/html/body/div[2]/div[3]/div/div/mat-option[30]/span/span',
    "80173": '/html/body/div[2]/div[3]/div/div/mat-option[31]/span/span',
    "80174": '/html/body/div[2]/div[3]/div/div/mat-option[32]/span',
    "80177": '/html/body/div[2]/div[3]/div/div/mat-option[33]/span/span',
    "80178": '/html/body/div[2]/div[3]/div/div/mat-option[34]/span/span',
    "80179": '/html/body/div[2]/div[3]/div/div/mat-option[35]/span/span',
    "80180": '/html/body/div[2]/div[3]/div/div/mat-option[36]/span/span',
    "80182": '/html/body/div[2]/div[3]/div/div/mat-option[37]/span/span',
    "80184": '/html/body/div[2]/div[3]/div/div/mat-option[38]/span/span',
    "80185": '/html/body/div[2]/div[3]/div/div/mat-option[39]/span',
    "80186": '/html/body/div[2]/div[3]/div/div/mat-option[40]/span/span',
    "80187": '/html/body/div[2]/div[3]/div/div/mat-option[41]/span/span',
    "80188": '/html/body/div[2]/div[3]/div/div/mat-option[42]/span',
    "80189": '/html/body/div[2]/div[3]/div/div/mat-option[43]/span/span',
    "80190": '/html/body/div[2]/div[3]/div/div/mat-option[44]/span/span',
    "80191": '/html/body/div[2]/div[3]/div/div/mat-option[45]/span',
    "80192": '/html/body/div[2]/div[3]/div/div/mat-option[46]/span',
    "80193": '/html/body/div[2]/div[3]/div/div/mat-option[47]/span/span',
    "80194": '/html/body/div[2]/div[3]/div/div/mat-option[48]/span/span',
    "80195": '/html/body/div[2]/div[3]/div/div/mat-option[49]/span/span',
    "80196": '/html/body/div[2]/div[3]/div/div/mat-option[50]/span'
}


if text_3 in my_dict_1:
    value_1 = my_dict_1[text_3]
    print("Value:", value_1)
else:
    print("Key not found in the dictionary.")


stock_job_option = driver.find_element(By.XPATH, value_1)
stock_job_option.click()
time.sleep(3)  
indent_type = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[1]/eipautocomplete/mat-form-field/div/div[1]/div/input')
indent_type.click()
my_dict_2 = {

   "general" : '/html/body/div[2]/div[3]/div/div/mat-option[1]/span',
    "plant and machinery" : '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span'
}

if text_4 in my_dict_2:
    value_2 = my_dict_2[text_4]
    print("Value:", value_2)
else:
    print("Key not found in the dictionary.")

time.sleep(2)

indent_type_option = driver.find_element(By.XPATH, value_2)
indent_type_option.click()
time.sleep(2)
priority = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-indent-create/div[2]/div/div/mat-horizontal-stepper/div[2]/div[1]/app-indent-create-header/div/mat-accordion/mat-expansion-panel[2]/div/div/div/div[3]/eipautocomplete/mat-form-field/div/div[1]/div/input')
priority.click()                          
time.sleep(1)
priority_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/mat-option[2]/span/span')
priority_option.click()                         
time.sleep(500)
