# Import
from dotenv import load_dotenv
from splinter import Browser
import time
import sys
import os

# Init error variable
err = True

# Load credentials from .env file
load_dotenv()
user = os.environ.get('FREEDNS_USER')
pw = os.environ.get('FREEDNS_PW')

# Initialize the browser
# - Use 'firefox' (default) or 'chrome'
# - Hide browser window with: headless=True
# - https://www.useragentstring.com/pages/Chrome/
# - https://www.useragentstring.com/pages/Firefox/
browser = Browser('chrome', headless=False, user_agent='Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.166 Safari/537.36')

# Visit site
browser.visit('https://freedns.afraid.org/profile/')

# Fill credentials and logon
form = browser.find_by_css('form#oPersistForm')
form.find_by_name('username').fill(user)
time.sleep(2)
form.find_by_name('password').fill(pw)
time.sleep(2)
form.find_by_name('submit').click()

# Check "Invalid UserID/Pass"
if browser.is_text_present('Invalid UserID/Pass', wait_time=10):
    print('Login: FAILED')
else:
    err = False
    print('Login: OK')

# Tell python to pause for 10s
time.sleep(10)

# Quit
browser.quit()

# Return exit code
if err:
    sys.exit(100)
else:
    sys.exit(0)
