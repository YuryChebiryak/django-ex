__author__ = 'yurychebiryak'
from django.http import HttpResponse
import Cards.IndexUpdater

def updateindex(request):
    IndexUpdater.updateIndex()
    return HttpResponse("Done!")
