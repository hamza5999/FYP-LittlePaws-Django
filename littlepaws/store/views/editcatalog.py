from django.shortcuts import render, redirect
from django.views import View
from store.models.catalog import Catalog
from store.models.filter import Filter

class EditCatalog(View):
    
    def get(self, request, catalogid):
        catalog = None
        catalog = Catalog.objects.get(id=catalogid)
        context = {'catalog':catalog}
        print("It is", str(catalog))
        return render(request, 'editcatalog.html', context)
    
    def post(self, request, catalogid):
        ucbreed = request.POST.get('ucatbreed')
        ucbreed = Filter.get_catagory_by_name(ucbreed)
        ucname = request.POST.get('ucatname')
        uccolor = request.POST.get('ucatcolor')
        ucgender = request.POST.get('ucatgender')
        ucsize = request.POST.get('ucatsize')
        ucears = request.POST.get('ucatears')
        ucprice = request.POST.get('ucatprice')
        ucdescription = request.POST.get('ucatdescription')
        catalog = Catalog.objects.get(id=catalogid)
        catalog.name=ucname
        catalog.color=uccolor
        catalog.gender=ucgender
        catalog.size=ucsize
        catalog.ears=ucears
        catalog.price=ucprice
        catalog.breed=ucbreed
        catalog.description=ucdescription
        catalog.save()
        return redirect('sellercatalogs')