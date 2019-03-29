# A selenium script to automatically simulate an alpha on worldquantvrc.com , opening up the scope for automation of random-testing.
import selenium
from selenium import webdriver      
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time  
   
from selenium.webdriver.common.keys import Keys

import xlwt 
from xlwt import Workbook   

#taking email and password as inputs
email=input("enter email id :")
password=input("enter password :")

# Creating an instance webdriver 
browser = webdriver.Firefox()  

#initialise the excel workbook and sheet
#wb = Workbook()
#sheet1 = wb.add_sheet('Sheet 1')

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
#simulation		
		browser.find_element_by_css_selector('.inputarea').send_keys("rank(sales/assets)")
		time.sleep(1)
		browser.find_element_by_xpath('//button[contains(@class,"intro-step-5")]').click()
		flag=False
	except NoSuchElementException:
		time.sleep(2.0)	
##################################################################################
#generate self and prod correlation
flag=True
time.sleep(10)
while(flag):
	try:
		self_prod_correlation_buttons=browser.find_elements_by_xpath('//div[contains(@class,"content-status-time-refresh")]')
		self_prod_correlation_buttons[0].click()
		self_prod_correlation_buttons[1].click()
		flag=False
	except NoSuchElementException:
		time.sleep(2.0)
##################################################################################
#finding and storing the results in an excel sheet

flag=True
while(flag):
	try:
		status=browser.find_element_by_xpath('//div[contains(@class,"summary__status-button")]').text
		print(status)
		title_grabbers=browser.find_elements_by_xpath('//div[contains(@class,"summary-metrics-info--title")]')
		value_grabbers=browser.find_elements_by_xpath('//div[contains(@class,"summary-metrics-info--data")]')
		for i in range(0,5):
			print(title_grabbers[i].text+" - "+value_grabbers[i].text)
		flag=False
	except NoSuchElementException:
		time.sleep(2.0)

flag=True
while(flag):
	try:
		self_prod_correlations=browser.find_elements_by_xpath('//div[contains(@class,"correlation__content-status-higher-value")]')
		if(self_prod_correlations[0].text=="-" or self_prod_correlations[1].text=="-"):
			continue
		print("self correlation - "+self_prod_correlations[0].text)
		print("prod correlation - "+self_prod_correlations[1].text)
		flag=False
	except NoSuchElementException:
		time.sleep(2.0)		
