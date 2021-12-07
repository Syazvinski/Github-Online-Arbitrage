#Importing selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#time management
import time

#for mac m1
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"

#driver
driver = webdriver.Chrome(chrome_driver_binary, options=options)

url = 'https://www.amazon.com/Mr-Coffee-Cappuccino-Stainless-Measuring/dp/B08NFMKHSK'

driver.get(url)

title = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[9]/div[4]/div[4]/div[1]/div/h1/span[1]').text

price = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[9]/div[4]/div[4]/div[9]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]').text


#we need to scroll to find theese
driver.execute_script("window.scrollTo(0,4500);")

time.sleep(5)

driver.get(url)

time.sleep(5)

size = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[9]/div[31]/div/div/div/div/div/div[1]/div/div/table/tbody/tr[1]/td').text
weight = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[9]/div[30]/div/div/div/div/div/div[1]/div/div/table/tbody/tr[2]/td').text

weight_num_only = int("".join(filter(str.isdigit, weight)))

if len(str(weight_num_only)) % 3 == 0:
    weight = float(weight_num_only[0],'.', weight_num_only[1],weight_num_only[2])

print(weight)

driver.close()