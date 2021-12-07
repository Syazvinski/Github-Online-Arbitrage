def feeCalculator(wallmartPrice,sellingPrice):

    #adding tax to wallmart price
    wallmartTax = wallmartPrice*.08924

    amazonFees = sellingPrice*.15

    return wallmartTax, amazonFees