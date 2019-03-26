# A selenium script to automatically simulate an alpha on worldquantvrc.com , opening up the scope for automation of random-testing.
import selenium
from selenium import webdriver      
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time  
   
from selenium.webdriver.common.keys import Keys  

#taking email and password as inputs
email=input("enter email id :")
password=input("enter password :")

# Creating an instance webdriver 
browser = webdriver.Firefox()  
browser.get('https://websim.worldquantvrc.com/simulate')
flag=True
while(flag):
	try:
		email_addr = browser.find_element_by_xpath('//input[@id="email"]')
		email_addr.send_keys(email)
		pwd=browser.find_element_by_xpath('//input[@id="password"]')
		pwd.send_keys(password)
		flag=False
	except NoSuchElementException:
		time.sleep(2.0)	
time.sleep(2.0)		
sign_in=browser.find_element_by_xpath('//button[contains(@class,"button") and contains(@class,"button--lg")]')
sign_in.click()
flag=True
while(flag):
	try:
		skip_btn=browser.find_element_by_xpath('//a[contains(@class,"introjs-button") and contains(@class,"introjs-skipbutton")]')
		skip_btn.click()
		flag=False
	except NoSuchElementException or ElementNotInteractableException:
		time.sleep(2.0)	
flag=True
while(flag):
	try:
		act=browser.find_element_by_xpath('//div[@class="introjs-overlay"]')
		act.click()
		time.sleep(5.0)
##################################################################################
#model_selection here

##################################################################################
		browser.find_element_by_css_selector('.inputarea').send_keys("rank(sales/assets)")
		time.sleep(1)
		browser.find_element_by_xpath('//button[contains(@class,"intro-step-5")]').click()
		flag=False
	except NoSuchElementException:
		time.sleep(2.0)	
flag=True
time.sleep(10)
while(flag):
	try:
		summary=browser.find_element_by_xpath('//div[contains(@class,"summary__status-button")]').text
		flag=False
	except NoSuchElementException:
		time.sleep(2.0)