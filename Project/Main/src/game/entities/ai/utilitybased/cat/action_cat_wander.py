'''
Created on Jul 14, 2013

@author: MintyAnt
'''

import random
from kivy.vector import Vector
from ..action import Action

class ActionCatWander(Action):
    
    def __init__(self):
        self._Target = Vector(0,0)
        
    def IsDone(self, inCat):
        return True
    
    def GetUtility(self, inCat):
        returnUtility = .2
        print ("Wander", returnUtility)
        return returnUtility
    
    def Enter(self, inCat):
        self._Target = Vector(random.randrange(0, 500), random.randrange(0, 500))
    
    def Update(self, inCat, dt):
        # Move to target
        myPos = Vector(inCat.pos[0], inCat.pos[1])
        
        vectorToTarget = self._Target - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > inCat.mSpeed):
            normalizedVectorToTarget *= inCat.mSpeed
        else:
            normalizedVectorToTarget *= distanceToTarget
            
        myPos += normalizedVectorToTarget
        inCat.pos = myPos
        
        if (myPos == self._Target):
            # find a new target
            from core import engine
            map = engine.GetInstance().mGame.mMap
            xRandom = random.uniform(map.x, map.right - inCat.width)
            yRandom = random.uniform(map.y, map.top - inCat.height)
            self._Target = Vector(xRandom, yRandom)
    
    def Exit(self, inCat):
        pass
        
    def __repr__(self):
        return "action_cat_wander"