def delete_nth(order, max_e):
    for i in order:
        if order.count(i) > max_e:
            while order.count(i) > max_e:
                order.reverse()
                order.remove(i)
                order.reverse()
    return order
        
def delete_nth_refactored(order,max_e):
    res = []
    for n in order:
        if res.count(n) < max_e: res.append(n)

    return res


 
