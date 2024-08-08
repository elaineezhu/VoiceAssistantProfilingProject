from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def amazon_login(driver, username, password):
    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    # Enter the email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_email"))
    )
    email_input.send_keys(username)
    email_input.send_keys(Keys.RETURN)

    # Wait for the password field and enter the password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_password"))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # Wait for login to complete
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nav-logo"))
    )

def search_and_add_to_cart(driver, item):
    # Search for the item
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for search results to load and add the first item to cart
    first_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] h2 a"))
    )
    first_item.click()
    
    # Wait for the product page to load and click on the "Add to Cart" button
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-button"))
    )
    add_to_cart_button.click()
    
    # Wait a bit to ensure the item is added to the cart
    time.sleep(2)

if __name__ == "__main__":
    driver = Driver(uc=True)

    # Login credentials
    username = "kaliblackster@gmail.com"
    password = "DigestBailiffs"

    # Perform Amazon login
    amazon_login(driver, username, password)

    # Read items from items.txt
    with open('/Users/elainezhu/Documents/GitHub/VoiceAssistantProfiling/items.txt', 'r') as file:
        items = file.readlines()

    # Search for each item and add to cart
    for item in items:
        search_and_add_to_cart(driver, item.strip())

    # Close the browser
    driver.quit()
