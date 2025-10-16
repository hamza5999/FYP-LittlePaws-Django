from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from store.models.catalog import Catalog
from store.models.filter import Filter
from django.views import View
from django.core.files.storage import FileSystemStorage
import cv2
import  numpy
import os
import time
class Home(View):
    def post(self, request):
        if 'filter' in request.POST:
            products = None
            color = request.POST.get('color')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            print(gender)
            products = Catalog.get_all_catalog()
            if color!='' and color is not None and gender!='' and gender is not None and gender!='' and gender is not None and age!='' and age is not None:
                products=products.filter(color__icontains=color, gender__icontains=gender, size__icontains=age)
            elif color!='' and color is not None and gender!='' and gender is not None:
                products=products.filter(color__icontains=color, gender__icontains=gender)
            elif color!='' and color is not None and age!='' and age is not None:
                products=products.filter(size__icontains=age, color__icontains=color)
            elif gender!='' and gender is not None and age!='' and age is not None:
                products=products.filter(gender__icontains=gender, size__icontains=age)
            elif age!='' and age is not None:
                products=products.filter(size__icontains=age)
            elif gender!='' and gender is not None:
                products=products.filter(gender__icontains=gender)
            elif color!='' and color is not None:
                products=products.filter(color__icontains=color)
            data = {}
            data['products'] = products
            print("Color age gender are : " , color ,age, gender)
            cart = request.session.get('cart')
            if not cart:
                request.session['cart'] = {}
            filter = Filter.get_all_catagories()  
            data['catagory'] = filter
            print ("You are : ", request.session.get('session_name'))
            return render(request, 'home.html',data)
        elif 'search' in request.POST:
            imageofsearch = request.FILES['search_image']
            file = FileSystemStorage()
            filename = file.save(imageofsearch.name+"image_by_search_for_preprocessing.jpg",imageofsearch)
            final_name_of_pic = imageofsearch.name+"image_by_search_for_preprocessing.jpg"
            input_image = "media\\"+final_name_of_pic
            color = ""
            products = None
            products = Catalog.get_all_catalog()
            data = {}
            face = cv2.CascadeClassifier("cat_features.xml")  # for detecting face
            image = cv2.imread(input_image)  
            if image is None:
                print('Wrong path:')
            else:
                print("Image Readable")
            image = cv2.resize(image, (300, 200))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert into gray so color not effect accuracy
            # parameters(img,scale_factor[reduce image size],min_neighbour)
            faces = face.detectMultiScale(gray, 1.1, 1)  # for  faces
            x_axis = 0
            y_axis = 0
            cat = False
            for (x, y, w, h) in faces:
                cat = True
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 205), 3)
                x_axis = x + int(w/2)
                x_axis = x_axis - 10
                y_axis = y + int(h/2)
                y_axis = y_axis - 10
            if cat:
                hue = [0,0,0]
                print(list)
                print("Cat Detected")
                image = cv2.rectangle(image, (x_axis, y_axis), (x_axis + 20, y_axis + 20), (127, 0, 205), 1)
                hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                x_axis = x_axis + 10
                y_axis = y_axis
                xlimit = x_axis+20
                ylimit = y_axis+20
                for x in range(x_axis,xlimit):
                    for y in range(y_axis,ylimit):
                        pixel = hsv[x,y]
                        H = pixel[0]
                        S = pixel[1]
                        V = int(pixel[2]/255) * 100
                        if H<20:
                            hue[1] = hue[1] + 1
                        elif H>15 and V>60:
                            hue[2] = hue[2] + 1
                        elif S<2:
                            hue[0] = hue[0] + 1
                        else:
                            hue[2] = hue[2] + 1
                print(hue)
                if hue[0]>hue[1] and hue[0]>hue[2]:
                    color = "Black"
                elif hue[1]>hue[0] and hue[1]>hue[2]:
                    color = "Brown"
                else:
                    color = "White"
                print(color)
            else:
                print("Its not a Cat")
            os.remove(input_image)
            #Here is the part of integration
            products=products.filter(color__icontains=color)
            data['products'] = products
            cart = request.session.get('cart')
            if not cart:
                request.session['cart'] = {}
            filter = Filter.get_all_catagories()
            data['catagory'] = filter
            print ("You are : ", request.session.get('session_name'))
            return render(request, 'home.html',data)    
        else:
            # request.session.get('session_cart').clear()
            product = request.POST.get('product')
            # print(product)
            remove = request.POST.get('remove')
            cart = request.session.get('session_cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity-1
                    else:
                        cart[product] = quantity+1
                else:
                    cart[product] = 1                
            else:
                cart = {}
                cart[product] = 1 
            request.session['session_cart'] = cart
            print(request.session['session_cart'])
            return redirect('homepage')
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        filter = Filter.get_all_catagories()
        filterid = request.GET.get('breed')
        if filterid:
            products = Catalog.get_all_catalog_by_id(filterid)
        else:
            products = Catalog.get_all_catalog()
        paginator = Paginator(products,6)
        page_number=request.GET.get('page')
        productDataFinal=paginator.get_page(page_number)
        data = {}
        data['products'] = productDataFinal   #products
        data['catagory'] = filter
        print ("You are : ", request.session.get('session_name'))
        # print ("You are : ", request.session.get('session_email'))
        return render(request, 'home.html',data)
class Homepage(View):
    def get(self, request):
        return redirect('homepage') 