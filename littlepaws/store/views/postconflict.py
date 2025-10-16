from django.shortcuts import render, redirect
from django.views import View
from store.models.conflicts import Conflict

class PostConflict(View):
    
    def post(self, request):
        subject = request.POST.get('subject')
        raisedbyname = request.POST.get('raisedbyname')
        raisedbytype = request.POST.get('raisedbytype')
        raisedbyemail = request.POST.get('raisedbyemail')
        raisedagainstname = request.POST.get('raisedagainstname')
        raisedagainsttype = request.POST.get('raisedagainsttype')
        raisedagainstemail = request.POST.get('raisedagainstemail')
        description = request.POST.get('conflictdescription')
        conflict = Conflict(raisedby_name=raisedbyname, raisedby_type=raisedbytype, raisedby_email=raisedbyemail, raisedagainst_name=raisedagainstname, raisedagainst_type=raisedagainsttype, raisedagainst_email=raisedagainstemail, conflict_subject=subject, conflict_description=description)
        conflict.save()
        useractive = request.session.get('session_type')
        if useractive == "Buyer":
            return redirect('homepage')
        else:
            return redirect('seller_home')