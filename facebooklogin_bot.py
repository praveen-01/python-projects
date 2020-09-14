from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
username=input("Enter your username")
passw=input("enter your password")
cd ='E:\python\chromedriver.exe' #path to your chrome driver
browser = webdriver.Chrome(cd)
browser.get("http://www.facebook.com")
i = browser.find_element_by_xpath('//*[@id="email"]')
i.send_keys(username)
c = browser.find_element_by_xpath('//*[@id="pass"]')
c.send_keys(passw)
x = browser.find_element_by_xpath('//*[@id="u_0_b"]')
x.click()
