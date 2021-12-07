import os
import random

def getRef():
    #changing current wokirng dir to current dir
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    my_file = open("randomWords.txt", "r")
    content = my_file.read()

    words = []
    for i in content.split():
        words.append(i)


    baseGoogleUrl = 'https://www.google.com/search?q='

    rndw1 = random.choice(words)
    rndw2 = random.choice(words)

    finalUrl = baseGoogleUrl + "+" + rndw1 + "+" + rndw2 + "+amazon" + "&sourceid=chrome&ie=UTF-8"  

    return finalUrl

