from django.shortcuts import render,redirect
from django.views import View
from store.models.catalog import Catalog
from store.models.orders import Order
from store.models.storeuser import StoreUser

class OrderView(View):
    def get(self, request):
        customer = request.session.get('session_email')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'order.html' ,{'orders':orders})
       