import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
r = sr.Recognizer()




# predefined URL
url = "http://localhost:4200/indent-request/indentReq"
driver = webdriver.Chrome(executable_path="C:\\Users\\20325730\\Desktop\\ZZZ\\chromedriver_win32\\chromedriver.exe")
driver.get(url)
driver.maximize_window()
#time.sleep(1000)

other_user = driver.find_element(By.XPATH,'/html/body/app-root/div/div[2]/app-login/div/form/div/div/div[1]/div/div[2]/div[1]/div/div[1]/ul/li[2]/a')
#search = driver.find_element(By.XPATH, '//*[@id="ibtINDADD"')
other_user.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.click()
username.send_keys("LandT")
password = driver.find_element(By.XPATH, '//*[@id="password-field"]')
password.click()
password.send_keys("ZZZZ")
login = driver.find_element(By.XPATH, '//*[@id="login-submit"]')
time.sleep(1000)

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
