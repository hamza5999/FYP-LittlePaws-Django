from django.views import View
from store.models.orders import Order
from django.shortcuts import render

class SellerPendingOrders(View):
    
    def get(self, request):
        print ("You are : ", request.session.get('session_name'))
        print ("You email : ", request.session.get('session_email'))
        seller_email = request.session.get('session_email')
        pendingorders = None
        pendingorders = Order.get_all_seller_pending_orders_by_email(seller_email)
        data = {}
        data['pendingorders'] = pendingorders
        print ("You orders : ", pendingorders)
        return render(request, 'seller_pendingorders.html', data)