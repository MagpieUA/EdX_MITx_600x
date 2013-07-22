# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
        
    def setBefore(self, before):
        
        self.before = before
        
    def setAfter(self, after):
        self.after = after
        
    def getBefore(self):
        return self.before
    
    def getAfter(self):
        return self.after
    
    def myName(self):
        return self.name


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if atMe.myName() <= newFrob.myName():
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif atMe.getAfter().myName() > newFrob.myName():
            newFrob.setBefore(atMe)
            newFrob.setAfter(atMe.getAfter())
            atMe.getAfter().setBefore(newFrob)
            atMe.setAfter(newFrob)
        else:
            insert(atMe.getAfter(),newFrob)
    else:
        if atMe.getBefore() == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif atMe.getBefore().myName() <= newFrob.myName():
            newFrob.setAfter(atMe)
            newFrob.setBefore(atMe.getBefore())
            atMe.getBefore().setAfter(newFrob)
            atMe.setBefore(newFrob)
        else:
            insert(atMe.getBefore(),newFrob)

def printList(frob):
    curFrob = frob
    result = ""
    while not curFrob.getBefore() == None:
        curFrob = curFrob.getBefore()
    while not curFrob.getAfter() == None:
        result += curFrob.myName()
        result += " --> "
        curFrob = curFrob.getAfter()
    result += curFrob.myName()
    print result

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() == None:
        result = start
    else:
        result = findFront(start.getBefore())
    return result
            
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
fred1 = Frob('fred')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
insert(ruth, fred1)

printList(ruth)

print findFront(martha).myName()
print findFront(eric).myName()
print findFront(ruth).myName()
print findFront(andrew).myName()

