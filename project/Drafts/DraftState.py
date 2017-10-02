__author__ = 'yurychebiryak'

from project.settings import base_url

class DraftState:
    def __init__(self, id, pack, pick):
        self.id = id
        self.pack = pack
        self.pick = pick

def GetNextPick(state):
    assert(isinstance(state, DraftState))
    if state.pick != 15:
        return DraftState(state.id, state.pack, state.pick +1)
    if state.pack != 3:
        return DraftState(state.id, state.pack + 1, 1)
    return DraftState(state.id, 1, 1)

def GetPrevPick(s):
    assert(isinstance(s, DraftState))
    if s.pick != 1:
        return DraftState(s.id, s.pack, s.pick - 1)
    if s.pack != 1:
        return DraftState(s.id, s.pack - 1, s.pick)
    return DraftState(s.id, 3, 15)

def GetNextPack(s):
    assert(isinstance(s, DraftState))
    if s.pack != 3:
        return DraftState(s.id, s.pack + 1, 1)
    return DraftState(s.id, 1, 1)

def GetDraftUrl(s):
    assert(isinstance(s, DraftState))
    return base_url + 'view/%d/%d/%d' % (s.id, s.pack, s.pick)
