from django.shortcuts import redirect, render
from django.views import View
from store.models.catalog import Catalog

class SellerCatalogs(View):
    
    def get(self, request):
        print ("You are : ", request.session.get('session_name'))
        print ("You email : ", request.session.get('session_email'))
        seller_email = request.session.get('session_email')
        allcatalogs = None
        allcatalogs = Catalog.get_all_catalogs_of_seller(seller_email)
        data = {}
        data['allcatalogs'] = allcatalogs
        print ("You orders : ", allcatalogs)
        return render(request, 'sellercatalogs.html', data)
    
    def post(self, request):
        pass

def deleteCatalog(request, catalogid):
    catalog = Catalog.objects.get(id=catalogid)
    catalog.delete()
    return redirect('sellercatalogs')