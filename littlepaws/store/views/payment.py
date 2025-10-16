#from turtle import payment
from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.generic.base import TemplateView
from django.conf import settings
from requests import request
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
class PaymentPageView(TemplateView):
    template_name = 'payment.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
