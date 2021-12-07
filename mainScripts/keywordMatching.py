def keywordMatching(amazonTitle,wallmartTitles,wallmartPrices,wallmartIds):
    #whitelist of letters
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    amazonTitle = ''.join(filter(whitelist.__contains__, amazonTitle))

    titles = []
    commonalities = []

    for i in wallmartTitles:
        #amount of words in common
        commonWords = 0

        wallmartTitle = ''.join(filter(whitelist.__contains__, i))

        for x in wallmartTitle.split():
            for y in amazonTitle.split():
                if x == y:
                    commonWords += 1

        titles.append(wallmartTitle)
        commonalities.append(commonWords)

    matchingTitleIndex = commonalities.index(max(commonalities))

    wallmartMatchingProduct = {
        'title': wallmartTitles[matchingTitleIndex],
        'price': wallmartPrices[matchingTitleIndex],
        'id': wallmartIds[matchingTitleIndex]
    }

    return wallmartMatchingProduct
        