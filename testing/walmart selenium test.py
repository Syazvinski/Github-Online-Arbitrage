#Importing selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#time management
import time

#random number gen
import random

def getSearchResults():
    #for mac m1
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_driver_binary = "/usr/local/bin/chromedriver"

    #driver
    driver = webdriver.Chrome(chrome_driver_binary, options=options)

    #wallmart url
    url = r'https://www.walmart.com/'

    #going to google
    driver.get(url)

    #waiting for a random amount of time
    time.sleep(random.uniform(1.0, 5.0))

    #input title
    driver.find_element_by_xpath('//*[@id="global-search-input"]').send_keys('Mr. Coffee Steam Espresso Cappuccino and Latte Maker, One Size, Black')

    #waiting for a random amount of time
    time.sleep(random.uniform(1.0, 5.0))

    #click on seatch
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/section/section/div[2]/div/div[3]/div[2]/div/form/button[3]/span').click()

    #get all text from listings
    listingsText = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/section/div[1]/div/div/div[4]/div[2]/div[2]').text

    #split text into list
    listingsText = listingsText.splitlines()

    #current index
    index = 0
    #indexes of every product title
    product_title_index = []

    #We are looking for the word product title because we know immideatly after is the title
    for i in listingsText:
        if i == 'Product Title':
            product_title_index.append(index)
        index += 1

    product_titles = []

    #find all titles
    for i in product_title_index:
        product_titles.append(listingsText[i+1])


    #current index
    index = 0
    #index of every product price
    product_price_index = []

    #we have to do theese seperatley because some products dont have review so it would ofset everything and mess it up

    #We are looking for the word product title because we know immideatly after is the title
    for i in listingsText:
        if i == 'Current Price':
            product_price_index.append(index)
        index += 1

    product_prices = []

    #find all prices
    for i in product_price_index:
        product_prices.append(listingsText[i+1])

    driver.close()

    results = {
        'titles': product_titles,
        'prices': product_prices }

    return results


def keywordMatching(title_amazon, results):
    #Keyword Matching
    keywordMatches = []

    #letters/words allowed
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    #amazon title
    #filtering everything thats not whitelisted out
    title_amazon = ''.join(filter(whitelist.__contains__, title_amazon))

    for i in results['titles']:

        #defining var for matching words
        words_matching = 0

        #filtering everything thats not whitelisted out
        title_wallmart = ''.join(filter(whitelist.__contains__, i))
        
        for x in title_wallmart.split():
            for y in title_amazon.split():
                if x == y:
                    words_matching += 1

        keywordMatchesDict = {
            'title': title_wallmart,
            'matches': words_matching
        }

        keywordMatches.append(keywordMatchesDict)

    return keywordMatches

if __name__ == "__main__":
    results = getSearchResults()

    print(keywordMatching('Mr. Coffee Steam Espresso Cappuccino and Latte Maker, One Size, Black',results))

    