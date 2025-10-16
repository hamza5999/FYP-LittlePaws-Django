from django.views import View
from store.models.orders import Order
from django.shortcuts import render

class SellerCompleteOrders(View):
    
    def get(self, request):
        print ("You are : ", request.session.get('session_name'))
        print ("You email : ", request.session.get('session_email'))
        seller_email = request.session.get('session_email')
        completeorders = None
        completeorders = Order.get_all_seller_complete_orders_by_email(seller_email)
        data = {}
        data['completeorders'] = completeorders
        print ("You orders : ", completeorders)
        return render(request, 'seller_completeorders.html', data)