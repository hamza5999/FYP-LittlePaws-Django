from django.shortcuts import render, redirect
from django.views import View
from store.models.orders import Order

class SellerHome(View):
    
    def get(self, request):
        print ("You are : ", request.session.get('session_name'))
        print ("You email : ", request.session.get('session_email'))
        seller_email = request.session.get('session_email')
        allorders = None
        allorders = Order.get_all_my_orders_by_email(seller_email)
        totalbalance = 0
        for x in allorders:
            totalbalance = totalbalance + x.price 
        print(totalbalance)
        request.session['sellerbalance'] = totalbalance
        data = {}
        data['allorders'] = allorders
        print ("You orders : ", allorders)
        return render(request, 'seller_home.html', data)