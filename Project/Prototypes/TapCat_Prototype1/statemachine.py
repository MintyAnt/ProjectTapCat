'''
Created on May 12, 2013

@author: MintyAnt
'''

from kivy.vector import Vector
import main
import random

''' ############################################################# '''
class StateMachine():
    _Owner = None
    _CurrentState = None
    _PreviousState = None
    
    def __init__(self, inOwner):
        self._Owner = inOwner
        
    def Update(self, dt):
        if (not self._CurrentState == None):
            self._CurrentState.Execute(self._Owner)
            
    def SetState(self, inState):
        if (inState == None):
            return
        
        if (not self._CurrentState == None):
            self._CurrentState.Exit(self._Owner)
            
        self._PreviousState = self._CurrentState
        print ("Changing state from %r to %r" % (self._CurrentState, inState))
        self._CurrentState = inState
        
        self._CurrentState.Enter(self._Owner)
    
    def RevertToPreviousState(self):
        self.SetState(self._PreviousState)
        
''' ############################################################# '''
class State():
    def Enter(self, inEntity):
        pass
    def Execute(self, inEntity):
        pass
    def Exit(self, inEntity):
        pass
    
''' ############################################################# '''
class StateCatWander():
    _Target = Vector(0,0)
    
    def Enter(self, inCat):
        self._Target = Vector(random.randrange(0, 500), random.randrange(0, 500))
    
    def Execute(self, inCat):
        # Move to target
        myPos = Vector(inCat.pos[0], inCat.pos[1])
        
        vectorToTarget = self._Target - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > inCat._Speed):
            normalizedVectorToTarget *= inCat._Speed
        else:
            normalizedVectorToTarget *= distanceToTarget
            
        myPos += normalizedVectorToTarget
        inCat.pos = myPos
        
        if (myPos == self._Target):
            # find a new target
            self._Target = Vector(random.randrange(0, 500), random.randrange(0, 500))
            
        # While we wander, check the stats
        if (inCat.LitterBox >= 25):
            # time 2 poo
            inCat._StateMachine.SetState(StateCatPoopSearch())
    
    def Exit(self, inCat):
        pass
    
''' ############################################################# '''
class StateCatSearchFood():
    def Enter(self, inCat):
        pass
    
    def Execute(self, inCat):
        pass
    
    def Exit(self, inCat):
        pass
    
''' ############################################################# '''
class StateCatEatFood():
    def Enter(self, inCat):
        pass
    
    def Execute(self, inCat):
        pass
    
    def Exit(self, inCat):
        pass
    
''' ############################################################# '''
class StateCatPoopSearch():
    _LitterBoxLocation = None
    
    def Enter(self, inCat):
        # Is there a litterbox nearby?
        litterBox = main.GetGameInstnace().litterBox
        
        if (not litterBox == None):
            # Is the litterbox full?
            if (litterBox.IsFull()):
                # Poo wherever we are!
                inCat._StateMachine.SetState(StateCatPerformPoop())
            
            # Otherwise, let's go to the litterbox
            self._LitterBoxLocation = Vector(litterBox.x, litterBox.y)
            
    def Execute(self, inCat):
        # Walk to the box until we are close enough
        myPos = Vector(inCat.pos[0], inCat.pos[1])
        
        vectorToTarget = self._LitterBoxLocation - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > inCat._Speed):
            normalizedVectorToTarget *= inCat._Speed
        else:
            normalizedVectorToTarget *= distanceToTarget
            
        myPos += normalizedVectorToTarget
        inCat.pos = myPos
        
        if (myPos == self._LitterBoxLocation):
            # go poo
            inCat._StateMachine.SetState(StateCatPerformPoop())

    def Exit(self, inCat):
        pass
    
class StateCatPerformPoop():
    def Enter(self, inCat):
        litterBox = main.GetGameInstnace().litterBox
        print("%r and %r", (litterBox, litterBox.IsFull()))
        if (not litterBox == None 
            and not litterBox.IsFull()):
            # poo in litterbox
            litterBox.PerformPoo(inCat)
            print ('im here')
        else:
            # Poo Right Here
            pass
        
        # Reset poo
        inCat.LitterBox = 0
        
        # Go back to wander
        inCat._StateMachine.SetState(StateCatWander())
    
    def Execute(self, inCat):
        pass
    
    def Exit(self, inCat):
        pass
    
    