from navigationContext import navContext

__author__ = 'yurychebiryak'
from django.shortcuts import render_to_response
from django.template import RequestContext
from navigationContext import uniteContexts
from Drafts.DraftID import GetRecentDrafts

def show(request):
    print (" List of recent drafts")
    drafts = GetRecentDrafts(200)
    context = RequestContext(request,
                             uniteContexts(navContext, {'drafts' : drafts}) )
    return render_to_response('recent.html', context)
