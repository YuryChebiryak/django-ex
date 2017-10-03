__author__ = 'yurychebiryak'
import datetime
from .Drafts import DraftID, DraftState
from django.http import HttpResponseRedirect
import os

def handle_uploaded_file(file):
    time = datetime.datetime.now()
    print (" handle uploaded file " )
    while True:
        id = time - datetime.datetime(1970,1,1)
        id = int (id.total_seconds() * 1000)
        if os.path.isfile(DraftID.GetDraftFilenameByID(id)):
            continue
        try:
            with open(DraftID.GetDraftFilenameByID(id), 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
                print(" wrote file into %s" % DraftID.GetDraftFilenameByID(id))
                return id
        except IOError:
            continue
    return id

def handle(request):
    print ("handle submit request")
    id = handle_uploaded_file(request.FILES['myfile'])
    s = DraftState.DraftState(id, 1, 1)
    return HttpResponseRedirect( DraftState.GetDraftUrl(s))
