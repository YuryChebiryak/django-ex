__author__ = 'yurychebiryak'
import os
import glob
from DraftState import DraftState
import re
from project.settings import base_url
from project.settings import data_dir

class Draft:
    def __init__(self, id):
        self.id = id
        self.filename = GetDraftFilenameByID(self.id)
        s = DraftState(self.id, 1, 1)
        self.eventNo, self.time, x, y, self.drafter = readPicks(s)
        self.url = base_url + 'view/%d/%d/%d' % (self.id, 1, 1)

def readPicks(s):
    """
    @return : list of avaiable cards, first one is the pick
    @param state: draft state
    """
    assert(isinstance(s, DraftState))
    cards = []
    prevPicks = []
    eventNo = 0
    time = ""
    filename = GetDraftFilenameByID(s.id)
    #filename = Draft(s.id).filename
    with open(filename, 'rb') as file:
        pick = "Pack %d pick %d:" % (s.pack, s.pick)
        event = r'^Event #: (\d*)'
        card = r'^(--> |    )(.*)$'
        pickedCard = r'^-->(.*)$'
        pickre = re.compile(pick)
        cardre = re.compile(card)
        eventre = re.compile(event)
        timere = re.compile(r'^Time:(.*)')
        pickedCardRe = re.compile(pickedCard)
        found = False
        lineno = -1
        for line in file:
            lineno += 1
            t = timere.match(line)
            if t:
                time = t.group(1).strip()
            e = eventre.match(line)
            if e:
                eventNo = int(e.group(1).rstrip())
            #print("%d %s" % (lineno, line))
            p = pickedCardRe.match(line)
            if p:
                prevPicks.append(p.group(1).strip())
            if not found:
                if pickre.match(line):
                    found = True
                    #print("was found in line no.", lineno)
            else:
                # found the necessary pick & pack, parsing the cards names
                m = cardre.match(line)
                if not m:
                    #print("exiting at this point")
                    break
                #print (" found a card in the corresp pack: %s" % line)
                if m.group(1) == '--> ': # first group is not empty: contains --> indicating the actual pick
                    cards.insert(0, m.group(2).rstrip())
                else:
                    cards.append(m.group(2).rstrip())
    return eventNo, time, cards, prevPicks[1:-1] if len(prevPicks) else [], prevPicks[0] if len(prevPicks) else "Error"


def GetDraftFilenameByID(id):
    """
    @param id: id of the draft
    @return: filename of that draft
    """
    name = os.path.join(data_dir, "storedDrafts/%d.txt" % id)
    return name

def GetDrafts():
    dir = os.path.join(data_dir, "storedDrafts/")
    print (" found files: ")
    files = filter(os.path.isfile, glob.glob(dir + "*.txt"))
    return files

def GetRecentDrafts(n):
    files = GetDrafts()
    for f in files:
        print (f)
    files.sort(key = lambda x: -os.path.getmtime(x))
    #print (files)
    drafts = []
    for f in files[:n]:
        id = int(re.match(r'^(.*)/(\d*).txt$', f).group(2))
        d = Draft(id)
        drafts.append(d)  # DraftState.GetDraftUrl(DraftState.DraftState(id, 1, 1)))
    return drafts
