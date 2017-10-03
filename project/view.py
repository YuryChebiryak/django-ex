
__author__ = 'yurychebiryak'
from django.shortcuts import render_to_response
from django.template import RequestContext
from .Drafts.DraftState import DraftState, GetDraftUrl, GetNextPick, GetPrevPick, GetNextPack
from .Drafts.DraftID import readPicks
from project.navigationContext import uniteContexts
from project.navigationContext import navContext
from .Cards.CardArt import GetCard
#import Cards.CardArt

def show(request, id, pack='1', pick='1'):
    s = DraftState(int(id), int(pack), int(pick))
    print (" Generating view of draft with id %d, pack %d, pick %d " % \
           ( s.id, s.pack, s.pick) )
    cards = []
    event, time, picks, prevPicks, drafter = readPicks(s)
    for name in picks:
        card = GetCard(name)
        cards.append( card )
    s1 = DraftState(s.id, 1,1)
    localContext = {'p1p1' :  GetDraftUrl(s1),
         'nextlink' : GetDraftUrl(GetNextPick(s)),
         'prevlink' : GetDraftUrl(GetPrevPick(s)),
         'selflink' : GetDraftUrl(s1),
         'nextpack' : GetDraftUrl(GetNextPack(s)),
         'event' : event,
         'id': id,
         'pack': pack,
         'pick': pick,
         'cards':cards,
         'prevPicks' : prevPicks,
         'drafter' : drafter,
         'time' : time,
         }
    context = RequestContext(request, uniteContexts(navContext, localContext))
    return render_to_response('view.html', context)
