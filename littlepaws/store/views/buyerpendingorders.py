from django.views import View
from store.models.orders import Order
from django.shortcuts import render

class BuyerPendingOrders(View):
    
    def get(self, request):
        print ("You are : ", request.session.get('session_name'))
        print ("You email : ", request.session.get('session_email'))
        buyer_email = request.session.get('session_email')
        pendingorders = None
        pendingorders = Order.get_pending_orders_of_customer(buyer_email)
        data = {}
        data['pendingorders'] = pendingorders
        print ("You orders : ", pendingorders)
        return render(request, 'buyer_pendingorders.html', data)