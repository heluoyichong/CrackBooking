from selenium import webdriver
from time import sleep # this should go at the top of the file
url = 'http://w2.leisurelink.lcsd.gov.hk/leisurelink/application/checkCode.do?flowId=2&lang=EN'

driver = webdriver.PhantomJS(executable_path="C:\Python27\misc\phantomjs-2.0.0-windows\phantomjs.exe")

driver.get(url)

sleep(100)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print html