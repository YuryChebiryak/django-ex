from project.navigationContext import navContext

__author__ = 'yurychebiryak'
from django.shortcuts import render_to_response
from django.template import RequestContext

from project.handlesubmit import handle


def draft(request):
    if request.method == 'POST':
        return handle(request)
    context = RequestContext(request, navContext)
    return render_to_response('submit.html', context)
