import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up the Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-browser-side-navigation')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')

# set up the webdriver
driver = webdriver.Chrome(chrome_options=chrome_options)

# navigate to the website and log in
driver.get('https://www.ahmmedshop.com/login')
# add code to enter login credentials here

# define a function to clean cookies and caches
def clear_cache():
    driver.execute_script('window.localStorage.clear();')
    driver.execute_script('window.sessionStorage.clear();')
    driver.get('chrome://settings/clearBrowserData')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//settings-ui'))).send_keys(Keys.ENTER)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//settings-ui'))).send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)

# define a function to refresh the page
def refresh_page():
    driver.refresh()

# define a function to get the cookies and post them to the API
def post_cookies():
    cookies = driver.get_cookies()
    requests.post('https://www.ahmmedshop.com/api/cookies', json=cookies)

# loop through the tasks every 15 minutes
while True:
    try:
        clear_cache()
        refresh_page()
        post_cookies()
        time.sleep(900) # wait for 15 minutes
    except:
        time.sleep(60) # if there is an error, wait for 1 minute and try again
