from django.shortcuts import render
from django.views import View

from store.models.conflicts import Conflict

class AdminPanel(View):
    
    def get(self, request):
        print ("You are : ", request.session.get('session_name'))
        print ("You email : ", request.session.get('session_email'))
        print ("This is admin panel.")
        conflicts= Conflict.get_all_conflicts()
        print(conflicts)
        return render(request, 'admin_panel.html',{'conflicts':conflicts})