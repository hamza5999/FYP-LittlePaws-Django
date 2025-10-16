from django.db import models
# Create your models here.
class StoreUser(models.Model):
    fullname = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    cnic = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    type = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    
    def emailExists(eParam):
        if StoreUser.objects.filter(email=eParam):
            return True
        return False
    
    def get_user_by_email(eParam):
        try:
            return StoreUser.objects.get(email=eParam)
        except:
            return False
    
    class Meta:
        db_table = "storeuser"