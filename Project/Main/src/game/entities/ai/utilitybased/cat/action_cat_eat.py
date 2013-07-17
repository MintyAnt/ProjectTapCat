'''
Created on Jul 14, 2013

@author: MintyAnt
'''

from ..action import Action
from kivy.vector import Vector

class ActionCatEat(Action):
    mEatingTime = .5
    mFoodPerEnergy = 5
    
    _EatCounter = 0
    _EatingPulse = 0
    
    _bDone = False
    
    def IsDone(self, inCat):
        return self._bDone
    
    def GetUtility(self, inCat):
        return 0
    
    def Enter(self, inCat):
        self._EatCounter = 0
        self._EatingPulse = self.mEatingTime
        
        from core import engine
        foodBowl = engine.GetInstance().mGame.mMap.mFoodBowl
        self._bDone = foodBowl.IsThereFoodInBowl()
    
    def Update(self, inCat, dt):
        from core import engine
        foodBowl = engine.GetInstance().mGame.mMap.mFoodBowl
        
        if (not self._bDone):
            if (inCat.pos != foodBowl.pos):
                self.EatFromBowl(inCat, foodBowl, dt)
            else:
                # Walk to food bowl.
                self.WalkToFoodBowl(inCat, foodBowl.pos)
    
    def Exit(self, inCat):
        self._bDone = False
        
    def EatFromBowl(self, inCat, inFoodBowl, dt):
        bFoodAvailable = inFoodBowl.IsThereFoodInBowl()
        if (bFoodAvailable):
            # Devour food from the bowl.
            self._EatingPulse -= dt
            if (self._EatingPulse <= 0):
                self._EatingPulse = self.mEatingTime
                
                # Take a food
                self._EatCounter += 1
                inFoodBowl.ModifyFood(-1)
                if (self._EatCounter >= self.mFoodPerEnergy):
                    self._EatCounter = 0
                    inCat.mEnergy += 1
        else:
            self._bDone = bFoodAvailable
        
    def WalkToFoodBowl(self, inCat, inFoodBowlLocation):
        myPos = Vector(inCat.pos[0], inCat.pos[1])
        
        vectorToTarget = inFoodBowlLocation - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > inCat.mSpeed):
            normalizedVectorToTarget *= inCat.mSpeed
        else:
            normalizedVectorToTarget *= distanceToTarget
            
        myPos += normalizedVectorToTarget
        inCat.pos = myPos
        
    def __repr__(self):
        return "action_cat_eat"