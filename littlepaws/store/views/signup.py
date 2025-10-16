from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from store.models.storeuser import StoreUser
from django.views import View

class Signup(View):
    
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        error_message = None
        u_fname = request.POST.get('fullname')
        u_phone = request.POST.get('phone')
        u_address = request.POST.get('address')
        u_cnic = request.POST.get('cnic')
        u_a_type = request.POST.get('accounttype')
        u_email = request.POST.get('emailaddress')
        u_pass = request.POST.get('pass')
        storeuser = StoreUser(fullname=u_fname, contact=u_phone, address=u_address, cnic=u_cnic, type=u_a_type, email=u_email, password=u_pass)
        value = {
            'fullname': u_fname,
            'phone': u_phone,
            'cnic': u_cnic,
            'email': u_email,
            'address': u_address
        }
        # validation
        if StoreUser.emailExists(u_email):
            error_message = "Email address already exists."
        # saving
        if not error_message:
            storeuser.password = make_password(storeuser.password)
            storeuser.save()
            return render(request,'signin.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request,'signup.html', data)