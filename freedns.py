# Import
from dotenv import load_dotenv
from splinter import Browser
import time
import os
import random
import helpers

# Init email body variable
body = ''

# Load credentials from .env file
load_dotenv()
user = os.environ.get('FREEDNS_USER')
pw = os.environ.get('FREEDNS_PW')

# Login to freedns
try:
    # Initialize the browser
    # - Use 'firefox' (default) or 'chrome'
    # - Hide browser window with: headless=True
    # - https://www.useragentstring.com/pages/Chrome/
    # - https://www.useragentstring.com/pages/Firefox/
    # - https://www.whatsmyua.info/
    browser = None
    browser = Browser('firefox', headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0')

    # Visit site
    browser.visit('https://freedns.afraid.org/profile/')

    # Fill credentials and logon
    form = browser.find_by_css('form#oPersistForm')
    form.find_by_name('username').fill(user)
    time.sleep(random.randint(2, 5))
    form.find_by_name('password').fill(pw)
    time.sleep(random.randint(2, 5))
    form.find_by_name('submit').click()

    # Check "Invalid UserID/Pass"
    if browser.is_text_present('Invalid UserID/Pass', wait_time=10):
        helpers.log('freedns login FAILED')
        body += 'freedns login FAILED\n'
    else:
        helpers.log('freedns login OK')
        body += 'freedns login OK\n'

    # Tell python to pause for 10s
    time.sleep(10)
except Exception as e:
    msg = f"freedns {e}"
    helpers.log(msg)
    body += msg + '\n'
finally:
    if browser is not None:
        browser.quit()

# Send email
helpers.log(helpers.email(os.environ.get('EMAIL_TO'), os.environ.get('EMAIL_FROM'), 
    os.environ.get('EMAIL_PORT'), os.environ.get('EMAIL_SMTP'), 
    'Autologin freedns.afraid.org', body, 
    os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PW')))
