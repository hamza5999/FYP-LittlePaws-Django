from django.shortcuts import render,redirect
from django.views import View
from store.models.catalog import Catalog
from store.models.orders import Order
from store.models.storeuser import StoreUser

class Checkout(View):
    def post(self, request):
        totalpayment = 0
        address = request.POST.get('address')
        request.session['updatedaddress'] = address
        # customer = request.session.get('session_customer_id')
        customer = request.session.get('session_email')
        if customer:
            cart = request.session.get('session_cart')
            catalog = Catalog.get_catalog_by_id(list(cart.keys()))
            
       
            for product in catalog:
                order = Order(product = product,
                seller = product.seller,
                customer = customer,
                name = product.name,
                quantity = cart.get(str(product.id)),
                price = int(product.price) * cart.get(str(product.id)),
                address = address)
                totalpayment = totalpayment + order.price
                order.placeOrder()
            request.session['session_cart'] = {}
            request.session['payable'] = totalpayment
            print(request.session.get('payable'))
            return redirect('payment')
        else:
            print("session not set")
            return redirect('signin')

        