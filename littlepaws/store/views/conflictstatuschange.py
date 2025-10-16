from django.shortcuts import render,redirect
from django.views import View
from store.models.conflicts import Conflict


class ConflictStatusChange(View):
    def get(self, request , conflict):
        print(conflict)
        conflict = Conflict.objects.get(id=conflict)
        check = conflict.status
        if check == False:
            conflict.status = True
            conflict.save()
            return redirect('adminpanel')
        else:
            return redirect('adminpanel')
        