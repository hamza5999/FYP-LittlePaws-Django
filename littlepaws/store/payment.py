from turtle import home,payment
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.views import View
# Create your views here.
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
class PaymentPageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    

