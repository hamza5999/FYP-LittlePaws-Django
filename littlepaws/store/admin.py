from django.contrib import admin
from .models import StoreUser, Catalog,Filter,Order, Conflict

class UsersTable(admin.ModelAdmin):
    list_display = ['fullname', 'contact', 'address', 'cnic', 'type', 'email', 'password']
class CatalogTable(admin.ModelAdmin):
    list_display = ['name', 'color', 'gender', 'price', 'description', 'image', 'ears', 'size', 'seller', 'breed']
class FilterTable(admin.ModelAdmin):
    list_display = ['breed']
class OrderTable(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'price', 'date']    
class ConflictTable(admin.ModelAdmin):
    list_display = ['raisedby_name', 'raisedby_type', 'raisedby_email', 'raisedagainst_name', 'raisedagainst_type', 'raisedagainst_email', 'conflict_subject', 'conflict_description', 'status', 'date']    
# Register your models here.
admin.site.register(StoreUser, UsersTable)
admin.site.register(Catalog, CatalogTable)
admin.site.register(Filter, FilterTable)
admin.site.register(Order , OrderTable)
admin.site.register(Conflict , ConflictTable)