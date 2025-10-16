from django.views import View
from store.models.conflicts import Conflict
from django.shortcuts import render

class AdminbPendingConflicts(View):
    
    def get(self, request):
        pendingconflicts = Conflict.get_pending_conflicts()
        print(pendingconflicts)
        data = {}
        data['conflicts'] = pendingconflicts
        print ("pending conflicts : ", pendingconflicts)
        return render(request, 'adminb_pendingconflicts.html', data)