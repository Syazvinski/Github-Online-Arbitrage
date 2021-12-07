#importing my lib
import resultASIN
import threading
import numpy as np

#opening list of UPC's and reading into list
my_file = open("upc.txt", "r")
upcList = my_file.readlines()

upcList = [s.replace("\n", "") for s in upcList]


#tracking percentages
amntDone = 0
amntToDo = len(upcList)


def getASINS(upcListSplit):
    global amntToDo
    global amntDone

    #open text file
    text_file = open("asinUPC.txt", "a")

    for i in upcListSplit:
        url = 'https://www.amazon.com/s?k='+str(i)

        #asin getting retirns list
        asinList = resultASIN.getASIN(url)

        if len(asinList) == 1:
            #write to text file
            text_file.write(str(asinList[0])+' '+str(i)+"\n")

            amntDone += 1
        elif len(asinList) > 1:
            for x in asinList:
                text_file.write(str(x)+' '+str(i)+"\n")
            amntDone += 1  
        elif len(asinList) == 0:
            pass
            amntDone += 1
        else:
            print("Fatal Error")
            amntDone += 1

        #printing percentage left
        print("{:.2%}".format(amntDone/amntToDo))

    text_file.close()


#num of lists to split into
n = 6

#list splilts
splits = np.array_split(upcList, n)

for array in splits:
    threading.Thread(target=getASINS, args=(list(array),)).start()