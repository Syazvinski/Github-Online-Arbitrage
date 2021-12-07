import requests
from requests import Session
from bs4 import BeautifulSoup
import time
import refGen
from fake_headers import Headers

def getASIN(url):

    #im setting some params for a random headers library
    header = Headers(
            browser="chrome",  # Generate only Chrome UA
            os="win",  # Generate ony Windows platform
            headers=True  # generate misc headers
        )

    #passing headers to amazon, so many because with one shit dont work. The useragent and referrer are the most import imo
    userAgent = header.generate()['User-Agent']#random user agent
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    referer = refGen.getRef()#random referer
    acceptLanguage = 'en-US,en;q=0.5'
    dnt = '1'

    # print('Using random referer: ' +referer)

    #defining headers
    headers = {'user-agent':userAgent,'accept':accept,'referer':referer,'accept-language':acceptLanguage,'dnt':dnt}

    #timing time because i want this to be an api
    t1 = time.time()

    headers.update(headers)

    #beautifull soup stuff (this takes the longest)
    source = requests.get(url,headers=headers)

    # f = open("yuh.html", "a")
    # f.write(source.text)
    # f.close()

    t2 = time.time()

    #getting data from page to parse
    soup = BeautifulSoup(source.text, 'lxml')

    #list of ids
    ids = []

    #find all hrefs (links)
    for link in soup.find_all('a'):

        #set url to href
        url = link.get('href')

        #if its of type string continue
        if type(url) == str:

            #see if string contains /dp/B0 because if it does its what we need
            if "/dp/B0" in url:
                #split every link into substring on every slash
                urlLst = url.split("/")
                #for every substring in main string lets see if there is B0 in the substring if there is log it and restart
                for i in urlLst:
                    if 'B0' in i:
                        if i not in ids and len(i) == 10:
                            ids.append(i)
                            break

    t3 = time.time()

    return ids

    # print("Request Time:"+str(t2-t1))
    # print("Filter Time:"+str(t3-t2))
    # print("Total Time:"+str(t3-t1))
