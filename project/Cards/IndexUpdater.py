__author__ = 'yurychebiryak'
from Drafts.DraftID import GetDrafts, readPicks, DraftState
import re
from Cards.CardArt import GetCard
def updateIndex():
    """
        Updates the cards index by going through all the drafts and requesting all the cards :)

    """
    files = GetDrafts()
    for file in files:
        print (" updating index using draft no %s " % file)
        id = int(re.match(r'(.*)/(\d+).txt', file).group(2))
        # state with 1, 1 is already in cache, states with picks > 8 are cards that were seen already
        for pack in range(1,4):
            for pick in range(1,9):
                if pack == 1 and pick == 1:
                    continue
                x, cards, y, z = readPicks(DraftState(id, pack, pick))
                for card in cards:
                    print ("\t card=%s" % card)
                    GetCard(card)


if __name__ == '__main__':
    updateIndex()