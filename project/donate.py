from navigationContext import navContext

__author__ = 'yurychebiryak'
from django.shortcuts import render_to_response
from django.template import RequestContext


def show(request):
    context = RequestContext(request, navContext)
    return render_to_response('donate.html', context)