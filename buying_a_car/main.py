def n_of_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    months = 0 
    savings = 0
    if start_price_old >= start_price_new:
        return [months, (start_price_old - start_price_new)]
    while (start_price_old + savings) <= start_price_new:
        months+=1
        if months % 2 == 0 and months != 0: 
            percent_loss_by_month+=0.5
        start_price_old *= (1 - percent_loss_by_month/100)
        start_price_new *= (1 - percent_loss_by_month/100)
        savings+=saving_per_month
    return [months, round((start_price_old + savings) - start_price_new)]
