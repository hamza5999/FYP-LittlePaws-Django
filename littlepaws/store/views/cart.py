from django.shortcuts import render
from django.views import View
from store.models.catalog import Catalog
from store.models.storeuser import StoreUser

class Cart(View):
    
    def get(self, request):
        ids = list(request.session.get('session_cart').keys())
        uemail = request.session.get('session_email')
        euser = StoreUser.get_user_by_email(uemail)
        print(uemail)
        print(ids)
        catalogs = Catalog.get_catalog_by_id(ids)
        print("catalogs are: ", catalogs)
        return render(request, 'cart.html', {'catalogs': catalogs, 'euser':euser})