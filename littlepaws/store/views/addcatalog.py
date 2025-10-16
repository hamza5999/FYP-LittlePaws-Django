from django.shortcuts import redirect, render
from django.views import View
from django.core.files.storage import FileSystemStorage
from store.models.catalog import Catalog
from store.models.catalog import Filter

class AddCatalog(View):
    
    def get(self, request):
        return render(request, 'addcatalog.html')
    
    def post(self, request):
        if request.method=='POST' and request.FILES['catimage']:
            cbreed = request.POST.get('catbreed')
            cbreed = Filter.get_catagory_by_name(cbreed)
            cname = request.POST.get('catname')
            ccolor = request.POST.get('catcolor')
            cgender = request.POST.get('catgender')
            csize = request.POST.get('catsize')
            cears = request.POST.get('catears')
            cimage = request.POST.get('catimage')
            
            image = request.FILES['catimage']
            file = FileSystemStorage()
            filename = file.save(image.name,image)
            cprice = request.POST.get('catprice')
            cdescription = request.POST.get('catdescription')
            cseller = request.POST.get('catseller')
            catalog = Catalog(name=cname, color=ccolor, gender=cgender, size=csize, ears=cears, image=filename, price=cprice, breed=cbreed, description=cdescription, seller=cseller)
            catalog.save()
        return redirect('sellercatalogs')