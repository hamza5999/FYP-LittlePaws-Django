from django.views import View
from store.models.conflicts import Conflict
from django.shortcuts import render

class AdminbCompleteConflicts(View):
    
    def get(self, request):
        completeconflicts = Conflict.get_complete_conflicts()
        print(completeconflicts)
        data = {}
        data['conflicts'] = completeconflicts
        print ("complete conflicts : ", completeconflicts)
        return render(request, 'adminb_completeconflicts.html', data)