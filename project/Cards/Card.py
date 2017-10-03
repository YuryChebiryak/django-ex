__author__ = 'yurychebiryak'
gatherer = "http://gatherer.wizards.com"


class Card:
    def __init__(self, name, id, url):
        self.name = name
        self.id = id
        self.url = url
    def GetGathererUrl(self):
        cardById = gatherer + "/Pages/Card/Details.aspx?multiverseid=%d"
        return cardById % self.id


def ReadCard(s):
    assert(isinstance(s, str))
    groups = s.split('|')
    if len(groups) == 3:
        return Card(groups[0], int(groups[1]), groups[2])
    return None
