from django.shortcuts import render,redirect
from django.views import View
from store.models.conflicts import Conflict
from store.models.orders import Order
from store.models.storeuser import StoreUser


class ConflictOnOrder(View):
    def get(self, request , order):
        order = Order.objects.get(id=order)
        # print(order.seller)
        # print(order.customer)
        useremail = request.session.get('session_email')
        # print(useremail)
        euser = StoreUser.get_user_by_email(useremail)
        raisedbyname=euser.fullname
        # print("Raised by name:", raisedbyname)
        raisedbytype=euser.type
        # print("type:", raisedbytype)
        raisedbyemail=euser.email
        # print("email:", raisedbyemail)
        if raisedbytype == "Buyer":
            raisedagainstemail=order.seller
            # print("Seller email:", raisedagainstemail)
            sellerinfo=StoreUser.get_user_by_email(raisedagainstemail)
            # print("Seller Info:", sellerinfo)
            raisedagainsttype=sellerinfo.type
            # print("Seller type:", raisedagainsttype)
            raisedagainstname=sellerinfo.fullname
            # print("Seller name:", raisedagainstname)
        else:
            raisedagainstemail=order.customer
            # print("Customer email:", raisedagainstemail)
            customerinfo=StoreUser.get_user_by_email(raisedagainstemail)
            # print("Customer Info:", customerinfo)
            raisedagainsttype=customerinfo.type
            # print("Customer type:", raisedagainsttype)
            raisedagainstname=customerinfo.fullname
            # print("Customer name:", raisedagainstname)
        data = {
            'raisedbyname': raisedbyname,
            'raisedbytype': raisedbytype,
            'raisedbyemail': raisedbyemail,
            'raisedagainstname': raisedagainstname,
            'raisedagainsttype': raisedagainsttype,
            'raisedagainstemail': raisedagainstemail
        }
        if raisedbytype == "Buyer":
            return render(request , 'writeconflict.html', data) 
        else:
            return render(request , 'writeconflictseller.html', data) 
    