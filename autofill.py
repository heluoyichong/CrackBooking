#from urllib2 import *

try:
    import Image
except ImportError:
    from PIL import Image
from SC_Reader import *

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
'catchar': code()
}

FormPage().fill_form(data).submit()
#i = i - 1

