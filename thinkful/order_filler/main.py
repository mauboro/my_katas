def fillable(stock, merch, n):
    return stock.get(merch) >= n if stock.get(merch) else False
