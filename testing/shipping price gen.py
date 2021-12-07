#Importing selenium
from os import truncate
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#time management
import time

#random number gen
import random

#for some filtering
import re

#for mac m1
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"

#driver
driver = webdriver.Chrome(chrome_driver_binary, options=options)

#wallmart url
url = r'https://onlineshippingcalculator.com/'

#going to google
driver.get(url)

#waiting for a random amount of time
#time.sleep(random.uniform(1.0, 5.0))

productDetails = {

    'length': 12,
    'width': 6,
    'height': 4,
    'weight':3
    }

#City From
driver.find_element_by_xpath("/html/body/div[1]/div/div/section[2]/div/div[2]/form/div[1]/div/div[1]/input").send_keys('Atlanta, GA, USA')

#City To
driver.find_element_by_xpath("/html/body/div[1]/div/div/section[2]/div/div[2]/form/div[2]/div/div[1]/input").send_keys('New York, NY, USA')

#Length
driver.find_element_by_xpath('/html/body/div[1]/div/div/section[2]/div/div[2]/form/div[3]/div[1]/div/input').send_keys(productDetails['length'])

#width
driver.find_element_by_xpath('/html/body/div[1]/div/div/section[2]/div/div[2]/form/div[3]/div[2]/div/input').send_keys(productDetails['width'])

#height
driver.find_element_by_xpath('/html/body/div[1]/div/div/section[2]/div/div[2]/form/div[3]/div[3]/div/div/input').send_keys(productDetails['height'])

#weight
driver.find_element_by_xpath('/html/body/div[1]/div/div/section[2]/div/div[2]/form/div[4]/div[1]/div/input').send_keys(productDetails['weight'])

#theese are the auto suggestions
driver.find_element_by_xpath('/html/body/div/div/div/section[2]/div/div[2]/form/div[1]/div/div[2]/div[1]').click()
driver.find_element_by_xpath('/html/body/div/div/div/section[2]/div/div[2]/form/div[2]/div/div[2]/div[1]').click()

#need a little rest for site to think
time.sleep(2.5)

#search button
driver.find_element_by_xpath('/html/body/div[1]/div/div/section[2]/div/div[2]/form/div[4]/div[2]/button').click()

elementExists = False

while elementExists == False:
    try:
        if driver.find_element_by_xpath('/html/body/div[1]/div/div/section[3]/div/div/div/h3').text == 'Shipping costs':
            elementExists = True
    except:
        pass

time.sleep(.5)

tableText = driver.find_element_by_xpath('/html/body/div/div/div/section[3]/div/div/div/div/table/tbody').text

driver.close()

newlinesSplit = tableText.splitlines()

shippingCarriers = []
shippingMethods = []
shippingTimes = []
shippingPrices = []



for i in newlinesSplit:
    rowList = i.split()

    for i in rowList:
        for x in i:
            #we are chekcing to see if 1 or 2 or 3 or 4 is in the row, if it is thats our 
            if x == '1' or x == '2' or x == '3':
                #if it was a match then the shipping time is equal to i
                shipTime = x

                #the carrier is always the first index
                carrier = rowList[0]

                #remove all dollar signs
                rowListFiltered = [s.replace("$", "") for s in rowList]

                #extract all 3 prices 
                pricesFromList =  [s for s in rowListFiltered if re.match(r'\d+(?:\.\d+)+$', s)]

                shipPrice = pricesFromList[1]

                #find shipping method
                
                rowList.pop(0)

                shipMethod = ''
                
                for y in rowList:
                    try:
                        int(y)
                        break
                    except:
                        shipMethod = str(shipMethod)+str(y)

                shippingMethods.append(shipMethod)
                shippingCarriers.append(carrier)
                shippingTimes.append(shipTime)
                shippingPrices.append(float(shipPrice))
            else:
                break

minPriceIndex = shippingPrices.index(min(shippingPrices))

bestShippingMethod = {
    'carrier': shippingCarriers[minPriceIndex],
    'method': shippingMethods[minPriceIndex],
    'shipTime': shippingTimes[minPriceIndex],
    'price': shippingPrices[minPriceIndex]
}

print(bestShippingMethod)