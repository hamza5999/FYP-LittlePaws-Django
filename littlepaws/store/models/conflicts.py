from django.db import models
import datetime
class Conflict(models.Model):
    raisedby_name = models.CharField(max_length=50,default='')
    raisedby_type = models.CharField(max_length=10,default='')
    raisedagainst_name = models.CharField(max_length=50,default='')
    raisedby_email = models.CharField(max_length=50,default='')
    raisedagainst_email = models.CharField(max_length=50,default='')
    raisedagainst_type = models.CharField(max_length=10,default='')
    date = models.DateField(default=datetime.datetime.today)
    conflict_subject = models.CharField(max_length=40,default='')
    conflict_description = models.CharField(max_length=100,default='')
    status = models.BooleanField(default=False)
    
    @staticmethod
    def get_all_conflicts():
        return Conflict.objects.all()
    
    @staticmethod
    def get_pending_conflicts():
        return Conflict.objects.filter(status = False).order_by('-date')
    
    @staticmethod
    def get_complete_conflicts():
        return Conflict.objects.filter(status = True).order_by('-date')
    
    class Meta:
        db_table = "conflict"