#LOL I KNOW
def get_order(order):
    return f"{'Burger ' * order.count('burger')}{'Fries ' * order.count('fries')}{'Chicken ' * order.count('chicken')}{'Pizza ' * order.count('pizza')}{'Sandwich ' * order.count('sandwich')}{'Onionrings ' * order.count('onionrings')}{'Milkshake ' * order.count('milkshake')}{'Coke ' * order.count('coke')}"[:-1]

def get_order_properly_done(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    res = ""
    for i in menu:
        res += (i.title() + " ") * order.count(i)
    return res[:-2]

