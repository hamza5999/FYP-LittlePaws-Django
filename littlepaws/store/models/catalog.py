from django.db import models
from django.db.models.fields.files import ImageField
from .filter import Filter

class Catalog(models.Model):
    image = ImageField()
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    seller = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    ears = models.CharField(max_length=20)
    breed = models.ForeignKey(Filter, on_delete=models.CASCADE,default=1)
    totalratings = models.IntegerField(default=0)
    star1 = models.IntegerField(default=0)
    star2 = models.IntegerField(default=0)
    star3 = models.IntegerField(default=0)
    star4 = models.IntegerField(default=0)
    star5 = models.IntegerField(default=0)
    ratings = models.FloatField(default=0.0)
    
    @staticmethod
    def get_all_catalog():
        return Catalog.objects.all()
    
    @staticmethod
    # for getting cart cats
    def get_catalog_by_id(ids):
        return Catalog.objects.filter(id__in = ids)

    @staticmethod
    def get_all_catalogs_of_seller(semail):
        return Catalog.objects.filter(seller = semail)

    @staticmethod
    def get_all_catalog_by_id(breed_name):
        if breed_name:
            return Catalog.objects.filter(breed = breed_name)
        else:
            Catalog.get_all_catalog()
        

    class Meta:
        db_table = "catalog"
    