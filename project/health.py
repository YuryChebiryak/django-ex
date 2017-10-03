
__author__ = 'yurychebiryak'
from django.http import HttpResponse

def liveliness(request):
    return HttpResponse("OK")

def readiness(request):
    return HttpResponse("OK")
