from django.views import View
from store.models.orders import Order
from django.shortcuts import render

class BuyerCompleteOrders(View):
    
    def get(self, request):
        print ("You are : ", request.session.get('session_name'))
        print ("You email : ", request.session.get('session_email'))
        buyer_email = request.session.get('session_email')
        completeorders = None
        completeorders = Order.get_complete_orders_of_customer(buyer_email)
        data = {}
        data['completeorders'] = completeorders
        print ("You orders : ", completeorders)
        return render(request, 'buyer_completeorders.html', data)