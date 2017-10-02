__author__ = 'yurychebiryak'
import urllib
import re
import os
import Card
import hashlib

from project.settings import data_dir

cardByName = Card.gatherer + "/Pages/Search/Default.aspx?name=[\""

#img = "(<img src=\"../../Handlers/Image.ashx?multiverseid=)(\\d+)(.*)(alt=\"\\w*\")(.*)(/>)"
imgSrc = Card.gatherer + "/Handlers/Image.ashx?multiverseid=%d&type=card"

def GetIndexFile(name):
    #we create many index files, so that it doesnt take too long to look thru them
    #   first 3 letters of card name serve as the index file name
    prefix = name[:3]
    m = hashlib.md5()
    m.update(prefix)
    filename = m.hexdigest()
    index = os.path.join(data_dir, "cardart/%s.txt" % filename)
    if not os.path.isfile(index):
        f = open(index, 'w+')
        f.close()
    return index


def GetCard(name):
    """
    @param name: card name
    @return: return the card
    """
    index = GetIndexFile(name)
    with open(index) as f:
        content = f.readlines()
        for line in content:
            c = Card.ReadCard(line)
            if not c:
                break
            if c.name == name:
                return c
        f.close()
    id = RetrieveCardID(name)
    if id == -1:
        c = Card.Card(name, id, cardByName+name +"\"]")
    else:
        c = Card.Card(name, id, GetCardImgById(id))
    with open(index, "a") as f:
        f.write("%s|%d|%s\r\n"  %(c.name, c.id, c.url))
    return c

def RetrieveCardID(name):
    """
    @rtype : card ID within the gatherer
    @param name: Card name
    """
    res = -1
    url = cardByName + name + "]" # % name
    print ("trying to open url %s" % url)
    f = urllib.urlopen(url)
    if not f:
        print "problem opening url %s" % url
        return res
    html = f.read()
    if not html:
        print "problem reading url %s" % url
        return res
    # now we need a card identifier for the card with exactly that name (there can be multiple matches)
        #print f.read()
    # parse the table, find the element with exact card name
    # return card id
    i = "(img src)(.*)(multiverseid=)(\\d+)(.*)(alt=\")" + name + "\""
    s = re.search(re.compile(i), html)
    if s:
        res = int(s.group(4))
    return res

def GetCardImgById(id):
    """
    @rtype: link to image
    @param id:
    """
    return imgSrc % id

#id = GetCardID("Balance")
#print ("requesting ", cardByName % id)
#imgexample = "<img src=\"../../Handlers/Image.ashx?multiverseid=202501&amp;type=card\" id=\"ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl00_listRepeater_ctl00_cardImage\" width=\"95\" height=\"132\" alt=\"Balance\" border=\"0\" />"
#cardimg = "<img src=\"../../Handlers/Image.ashx?multiverseid=202501&amp;type=card\" id=\"ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage\" alt=\"Balance\" style=\"border:none;\" />"
#print GetCardImgById(id)
