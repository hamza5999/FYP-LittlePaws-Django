from django.db import models
class Filter(models.Model):
    breed=models.CharField(max_length=30)

   
    @staticmethod
    def get_catagory_by_name(name):
        return Filter.objects.get(breed=name)

    @staticmethod
    def get_all_catagories():
        return Filter.objects.all()


    def __str__(self):
        return self.breed


    class Meta:
        db_table = "filter"

