import amazonGetInfo
import wallmartGetInfo
import shippingPriceInfo
import keywordMatching
import fees

# https://www.amazon.com/Chesapeake-Bay-Candle-Scented-Stillness/dp/B07GH7ZDWG

while True:

    def findProfitability(url):
        
        #get product info from amazon
        amazonProduct = amazonGetInfo.getInfo(url)
        wallmartUrl = amazonGetInfo.wlmrtUrlGen(amazonProduct['title'])

        #wallmart get info
        titles, prices, ids = wallmartGetInfo.getTitlesPrices(wallmartUrl)

        #get shipping price
        shipPrice = shippingPriceInfo.getShipRate(amazonProduct['weight'])

        #get matching wallmart item
        wallmartProduct = keywordMatching.keywordMatching(amazonProduct["title"],titles,prices,ids)

        #get amazon fees and wallmart tax
        wallmartTax, amazonFees = fees.feeCalculator(wallmartProduct['price'],amazonProduct['price'])

        #subtracting all expenses from amazon price
        profit = amazonProduct['price']-wallmartProduct['price']-amazonFees-wallmartTax-shipPrice

        print("Profit",profit)
        print("https://www.walmart.com/ip/"+wallmartProduct['id'])
        

    findProfitability(input("Amazon Url: "))