import pandas as pd
import os

#changing current wokirng dir to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#import excel
lbs = pd.read_excel (r'priorityMailRatesLbs.xlsx', sheet_name='Sheet1')
oz = pd.read_excel (r'firstClassMailRatesOzs.xlsx', sheet_name='Sheet1')

def getShipRate(weightOzs):
    #if more than 16 oz
    if float(weightOzs) > 16:

        #pounds
        weight = round(weightOzs/16)

        #return result
        return lbs.loc[weight-1]['Zone 5']

    #if less than 16 ounces
    elif float(weightOzs) < 16:
        
        #ounces
        weight = round(weightOzs)

        #return result
        return oz.loc[weight-1]['Zone 5']
    #im lost
    else:
        print("help me im lost")

if __name__ == "__main__":
    print(getShipRate(400))