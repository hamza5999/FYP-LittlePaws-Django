from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect
from store.models.storeuser import StoreUser
from django.views import View

class Signin(View):
    
    def get(self, request):
        return render(request, 'signin.html')
    
    def post(self, request):
        error_message = None
        lu_email = request.POST.get('lemail')
        lu_pass = request.POST.get('lpass')
        suser = StoreUser.get_user_by_email(lu_email)
        if suser:
            valid = check_password(lu_pass, suser.password)
            print("actual pass: ", lu_pass)
            print("entered pass: ", suser.password)
            if valid:
                request.session['session_name'] = suser.fullname
                request.session['session_email'] = suser.email
                request.session['session_customer_id'] = suser.id
                request.session['session_type'] = suser.type
                status = suser.type
                # print(status)
                if status == 'Seller':
                    return redirect('seller_home') #changed here
                elif status == 'Admin':
                    return redirect('adminpanel') 
                else:
                    return redirect('homepage')    
            else:
                error_message = "Invalid email or password."
                return render(request,'signin.html', {'error': error_message})
        else:
            error_message = "Invalid email or password."
            return render(request,'signin.html', {'error': error_message})
        
def logout(request):
    request.session.clear()
    return redirect('homepage')
def sellerlogout(request):
    request.session.clear()
    return redirect('homepage')