import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
url =("https://eip4dev.lntecc.com/EIPSCMUI/SOPUI/Warehouse/MaterialIssue")

# set up speech recognition
r = sr.Recognizer()

# set up selenium driver
driver = webdriver.Chrome(executable_path="C:\\Users\\20325730\\Downloads\\ZZZ\\chromedriver_win32\\chromedriver.exe")

# function to open a URL
def open_url(url):
    driver.get(url)

# function to fill in login credentials and click login button
def fill_credentials(username, password):
    try:
        username_field = driver.find_element_by_id("username")
        password_field = driver.find_element_by_id("password")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
    except:
        print("Could not fill in login credentials or click login button.")

# loop for continuous voice recognition
while True:
    # listen for speech input
    with sr.Microphone() as source:
        print("Speak a URL...")
        audio = r.listen(source)

    # use speech recognition to convert speech to text
    try:
        url = r.recognize_google(audio)
        print(f"Opening {url}")
        open_url(url)

        # get login credentials
        while True:
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
                    fill_credentials(username, password)
                    break
                except sr.UnknownValueError:
                    print("Speech recognition could not understand audio.")
                except sr.RequestError as e:
                    print(f"Could not request results from Speech Recognition service; {e}")
                break
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Speech Recognition service; {e}")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Speech Recognition service; {e}")
