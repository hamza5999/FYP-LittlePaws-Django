from django.shortcuts import render,redirect
from django.views import View
from store.models.orders import Order


class OrderStatusChange(View):
    def get(self, request , order):
        print(order)
        order = Order.objects.get(id=order)
        check = order.status
        if check == False:
            order.status = True
            order.save()
        if request.session.get('session_type') == "Seller":
            return redirect('seller_home')
        else:
            return redirect('orders')
        