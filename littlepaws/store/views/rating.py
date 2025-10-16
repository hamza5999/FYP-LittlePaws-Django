from itertools import product
from django.shortcuts import render,redirect
from django.views import View
from store.models.orders import Order
from store.models.catalog import Catalog


class Ratings(View):
    def get(self, request, order, rate):
        #print(order)
        #print(rate)
        ordervalue = Order.objects.get(id=order)
        cata = ordervalue.product
        ordervalue.feedback = True
        ordervalue.save()
        #print("My object is : ",cata)
        cata = cata.id
        #print("My object value is : ",cata)
        product = Catalog.objects.get(id=cata)
        product.totalratings = product.totalratings + 1
        print("Total ratings are ",product.totalratings)
        #print("My Total rating values  is : ",totalratings)
        if rate==1:
            product.ratings = ((product.star5*5)+(product.star4*4)+(product.star3*3)+(product.star2*2)+((product.star1+1)*1))/(product.totalratings)
            product.star1 = product.star1 + 1
            product.save()
        elif rate==2:
            product.ratings = ((product.star5*5)+(product.star4*4)+(product.star3*3)+((product.star2+1)*2)+(product.star1*1))/(product.totalratings)
            product.star2 = product.star2 + 1
            product.save()
        elif rate==3:
            product.ratings = ((product.star5*5)+(product.star4*4)+((product.star3+1)*3)+(product.star2*2)+(product.star1*1))/(product.totalratings)
            product.star3 = product.star3 + 1
            product.save()
        elif rate==4:
            product.ratings = ((product.star5*5)+((product.star4+1)*4)+(product.star3*3)+(product.star2*2)+(product.star1*1))/(product.totalratings)
            product.star4 = product.star4 + 1
            product.save()
        elif rate==5:
            product.ratings = (((product.star5+1)*5)+(product.star4*4)+(product.star3*3)+(product.star2*2)+(product.star1*1))/(product.totalratings)
            product.star5 = product.star5 + 1
            product.save()
        return redirect('orders')
       
        