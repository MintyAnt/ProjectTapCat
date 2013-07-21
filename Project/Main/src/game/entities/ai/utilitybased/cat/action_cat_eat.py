'''
Created on Jul 14, 2013

@author: MintyAnt
'''

from ..action import Action
from kivy.vector import Vector
import math

class ActionCatEat(Action):
    mEatingTime = .5
    mFoodPerEnergy = 2
    
    _EatCounter = 0
    _EatingPulse = 0
    
    _bDone = False
    
    def IsDone(self, inCat):
        return self._bDone
    
    def GetUtility(self, inCat):
        from core import engine
        foodBowl = engine.GetInstance().mGame.mMap.mFoodBowl
        foodInBowl = foodBowl.IsThereFoodInBowl()
        if (not foodInBowl):
            return 0.0
        
        utility = (1.0 - (inCat.mHunger / inCat.mHungerMax))
        utility = math.pow(utility, 3)
        print ("eat ", utility)
        return utility
    
    def Enter(self, inCat):
        self._EatCounter = 0
        self._EatingPulse = self.mEatingTime
        
        from core import engine
        foodBowl = engine.GetInstance().mGame.mMap.mFoodBowl
        self._bDone = (not foodBowl.IsThereFoodInBowl())
    
    def Update(self, inCat, dt):
        from core import engine
        foodBowl = engine.GetInstance().mGame.mMap.mFoodBowl
        
        if (not self._bDone):
            if (inCat.pos == foodBowl.pos):
                self.EatFromBowl(inCat, foodBowl, dt)
            else:
                # Walk to food bowl.
                self.WalkToFoodBowl(inCat, Vector(foodBowl.pos))
    
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
                    inCat.mHunger += 1
        else:
            self._bDone = not bFoodAvailable
        
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