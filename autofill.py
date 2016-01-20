#PHASE ONE
#This is to mock real-person access to the website.
#Step 1: Open the webpage with browser - Firefox. (may be replaced with phantomjs in late revision)
#Step 2: Screencapture the page and store the .png file as "screenshot.png". (this should be considered when replacing the browser with phantomjs)
#Step 3: Cut the captcha from the "screenshot.png" and save as "crop.png".
#Step 4: Clean the noise of "crop.png" and save as "bath.png".
#Step 5: Using OCR Tesser to conduct the character recognition. (!!Pay Attention: We are using and calling the Tesseract engine directly from SHELL while not using exisiting python wrapper - Pytesser or whatsoever in this code because of inflexibility to adjust (only 6 characters or only digits&characters)induced by pre-installed outdated tesser enginine. Thus should have the latest Tesser installed.)
#____________Ref____________https://code.google.com/p/tesseract-ocr/____________
#Step 6: Fill in the form and submit automatically. (using selenium lib to call the webdriver. should consider to replace with phantomjs. NEED TO ADD RECURIVE ATTEMPTS IN CASE OF FAILURE)
#____________Ref____________http://stackoverflow.com/questions/26050075/filling-out-web-form-data-using-built-in-python-modules/____________
#Step 7: Reaching the username and password page. Then we've done with PHASE ONE

try:
    import Image
except ImportError:
    from PIL import Image

import SC_Reader

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

i = 2

url = 'http://w2.leisurelink.lcsd.gov.hk/leisurelink/application/checkCode.do?flowId=2&lang=EN'


#while i > 0:


driver = webdriver.Firefox()
driver.get(url)

driver.save_screenshot("screenshot.png")

def find_by_xpath(locator):
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, locator))
)
    return element

class FormPage(object):
    def fill_form(self, data):
        find_by_xpath('//input[@name = "imgCode"]').send_keys(data['catchar'])
        return self # makes it so you can call .submit() after calling this function

    def submit(self):
        find_by_xpath('//input[@value = "Continue"]').click()

data = {
'catchar': SC_Reader.code()
}

FormPage().fill_form(data).submit()
#i = i - 1

