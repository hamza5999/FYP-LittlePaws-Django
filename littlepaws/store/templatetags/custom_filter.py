from django import template
register = template.Library()

@register.filter(name='currency')
def currency(num):
    return "Rs. " + str(num)

@register.filter(name='multiply')
def multiply(num, num1):
    return "Rs. " + str(num*num1)