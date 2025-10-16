from django.shortcuts import render, redirect
from django.views import View
from store.models.storeuser import StoreUser

class SellerEditProfile(View):
    
    def get(self, request):
        uemail = request.session['session_email']
        print(uemail)
        euser = StoreUser.get_user_by_email(uemail)
        context = {'euser':euser}
        # print("It is", str(euser.fullname))
        return render(request, 'sellereditprofile.html', context)
    
    def post(self, request):
        uemail = request.session['session_email']
        euser = StoreUser.get_user_by_email(uemail)
        uename = request.POST.get('uname')
        uecnic = request.POST.get('ucnic')
        uecontact = request.POST.get('ucontact')
        euser.fullname=uename
        euser.contact=uecontact
        euser.cnic=uecnic
        euser.save()
        return redirect('seller_home')