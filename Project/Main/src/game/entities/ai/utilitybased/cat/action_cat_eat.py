'''
Created on Jul 14, 2013

@author: MintyAnt
'''

from ..action import Action

class ActionCatEat(Action):
    def IsDone(self, inCat):
        pass
    
    def GetUtility(self, inCat):
        return 0
    
    def Enter(self, inCat):
        pass
    
    def Update(self, inCat, dt):
        pass
    
    def Exit(self, inCat):
        pass