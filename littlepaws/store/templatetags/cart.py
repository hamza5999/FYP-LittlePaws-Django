from django import template
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return False
 
@register.filter(name='price_total')
def price_total(product , cart):
    price = int(product.price)
    print("Price of each is :", price)
    return price * cart_quantity(product, cart)

@register.filter(name='cart_price_total')
def cart_price_total(products, cart):
    sum = 0
    for p in products:
        # print('values are : ',price_total(p, cart))
        sum += price_total(p, cart)
        
    return sum