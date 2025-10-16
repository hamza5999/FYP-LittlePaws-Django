from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.views import View
# Create your views here.
from django.views.generic.base import TemplateView
from django.conf import settings
from store.models.orders import Order
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
class Charge(View):
    
    def post(self, request):
        amo = request.session.get('payable')
        charge = stripe.Charge.create(
                amount = amo,
                currency='usd',
                description='A django charge',
                source=request.POST['stripeToken']            
            )   
        return redirect('orders')
        #def charge(request):
        #if request.method == 'POST':
            
    def get(self, request):
        return redirect('homepage')
    
    