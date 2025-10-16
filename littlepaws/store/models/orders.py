from django.db import models
from .storeuser import StoreUser
from .catalog import Catalog
import datetime
class Order(models.Model):
    product = models.ForeignKey(Catalog , on_delete=models.CASCADE)
    
    # customer = models.ForeignKey(StoreUser , on_delete=models.CASCADE)
    customer = models.CharField(max_length=30,default='')
    seller = models.CharField(max_length=30,default='')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    name = models.CharField(max_length=30,default='')
    date = models.DateField(default=datetime.datetime.today)
    address = models.CharField(max_length=30,default='')
    status = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)
    payment = models.BooleanField(default=True)



    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_email):
        return Order.objects.filter(customer = customer_email).order_by('-date')
    
    @staticmethod
    def get_pending_orders_of_customer(customer_email):
        return Order.objects.filter(customer = customer_email).filter(status = False).order_by('-date')
    
    @staticmethod
    def get_complete_orders_of_customer(customer_email):
        return Order.objects.filter(customer = customer_email).filter(status = True).order_by('-date')
    
    @staticmethod
    def get_all_my_orders_by_email(semail):
        return Order.objects.filter(seller = semail).order_by('-date')
    
    @staticmethod
    def get_all_seller_pending_orders_by_email(semail):
        return Order.objects.filter(seller = semail).filter(status = False).order_by('-date')
    
    @staticmethod
    def get_all_seller_complete_orders_by_email(semail):
        return Order.objects.filter(seller = semail).filter(status = True).order_by('-date')
    
    class Meta:
        db_table = "order"