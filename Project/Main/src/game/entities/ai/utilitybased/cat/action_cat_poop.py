'''
Created on Jul 14, 2013

@author: MintyAnt
'''

from ..action import Action
from game.entities.poo import PooWidget
from kivy.vector import Vector

class ActionCatPoop(Action):
    _LitterBoxLocation = Vector(0, 0)
    _bComplete = False
    
    def IsDone(self, inCat):
        pass
    
    def GetUtility(self, inCat):
        pass
    
    def Enter(self, inCat):
        self._bComplete = False
        
        # Is there a litterbox nearby?
        from core import engine
        litterBox = engine.GetInstance().mGame.mMap.mLitterBox
        
        if (not litterBox == None):
            # Is the litterbox full?
            if (litterBox.IsFull()):
                # Poo wherever we are!
                self.ExecutePoop(inCat)
                return
            
            # Otherwise, let's go to the litterbox
            self._LitterBoxLocation = Vector(litterBox.x, litterBox.y)
            return
        
        # Poo wherever we are!
        self.ExecutePoop(inCat)
            
    def Update(self, inCat, dt):
        # Walk to the box until we are close enough
        myPos = Vector(inCat.pos[0], inCat.pos[1])
        
        vectorToTarget = self._LitterBoxLocation - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > inCat.mSpeed):
            normalizedVectorToTarget *= inCat.mSpeed
        else:
            normalizedVectorToTarget *= distanceToTarget
            
        myPos += normalizedVectorToTarget
        inCat.pos = myPos
        
        if (myPos == self._LitterBoxLocation):
            # go poo
            self.ExecutePoop(inCat)

    def Exit(self, inCat):
        pass
    
    def ExecutePoop(self, inCat):
        from core import engine
        litterBox = engine.GetInstance().mGame.mMap.mLitterBox
        print("%r and %r", (litterBox, litterBox.IsFull()))
        if (not litterBox == None 
            and not litterBox.IsFull()):
            # poo in litterbox
            litterBox.PerformPoo(inCat)
            print ('im here')
        else:
            # Poo Right Here
            from core import engine
            map = engine.GetInstance().mGame.mMap
            newPoo = PooWidget()
            newPoo.pos = inCat.pos
            map.mMapEntities.append(newPoo) 
            map.mMapRootElement.add_widget(newPoo)
        
        # Reset poo
        inCat.mLitterBox = 0
        
        # We are finished
        self._bComplete = True