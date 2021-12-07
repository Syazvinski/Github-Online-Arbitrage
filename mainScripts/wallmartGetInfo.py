import requests
from bs4 import BeautifulSoup
import json
import sys
import refGen

def getTitlesPrices(url):
    #setting headers so we dont get refused
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    acceptLanguage = 'en-US,en;q=0.5'
    dnt = '1'
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    referer = refGen.getRef()#random refere

    #defining headers
    headers = {'user-agent':userAgent,'accept':accept,'referer':referer,'accept-language':acceptLanguage,'dnt':dnt}

    #initilizing requests
    r = requests.get(url, headers=headers)

    #getting the json
    soup = BeautifulSoup(r.text, 'lxml')
    s = str(soup.find('script', {'id': 'searchContent'}))

    #striping unnecesary javascript
    s = s.strip('<script id="searchContent" type="application/json"></script>')
    s = s.strip('"</script>"')

    #try loading json and catch exxeption if not loading
    try:
        j = json.loads(s)
    except:
        print (s)
        sys.exit()

    #going into json to find what we neeed
    x = j['searchContent']['preso']['items']

    #making 2 blank lists
    titles = []
    prices = []
    ids = []

    #going in an getting needed data and adding to list
    for i in x:
        try:
            price = i['primaryOffer']['offerPrice']
            title = i['title'].replace("<mark>","").replace("</mark>","")
            id = i['productId']
            titles.append(title)
            prices.append(price)
            ids.append(id)
        except:
            pass
        
        

    return titles, prices ,ids

if __name__ == "__main__":
    print(getTitlesPrices(r"https://walmart.com/search?query=Mr.%20Coffee%20Steam%20Espresso%20Cappuccino%20and%20Latte%20Maker,%20One%20Size,%20Black"))