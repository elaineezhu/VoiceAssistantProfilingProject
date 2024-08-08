from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def google_login(driver, username, password):
    driver.get("https://accounts.google.com/signin/v2/identifier")

    # Enter the username
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "identifier"))
    )
    email_input.send_keys(username)
    email_input.send_keys(Keys.RETURN)
    
    # Wait for 5 seconds after entering the username
    time.sleep(5)

    # Wait for the password field and enter the password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    # Wait for 5 seconds after entering the password
    time.sleep(5)

    driver.get("https://www.google.com")

def search_google(driver, query):
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for search results to load

if __name__ == "__main__":
    # Create a new instance of the Chrome driver using seleniumbase
    driver = Driver(uc=True)

    # Login credentials
    username = "bamtrisno24"
    password = "RouterGreen"

    # Perform Google login
    google_login(driver, username, password)

    # Read queries from questions.txt
    with open('/Users/elainezhu/Documents/GitHub/VoiceAssistantProfiling/questions.txt', 'r') as file:
        queries = file.readlines()

    # Perform searches
    for query in queries:
        search_google(driver, query.strip())

    # Close the browser
    driver.quit()
