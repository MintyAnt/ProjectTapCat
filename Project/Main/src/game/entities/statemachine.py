'''
Created on May 12, 2013

@author: MintyAnt
'''

from kivy.vector import Vector
import random

''' ############################################################# '''
class StateMachine():
    _Owner = None
    mCurrentState = None
    mPreviousState = None
    
    def __init__(self, inOwner):
        self._Owner = inOwner
        
    def Update(self, dt):
        if (not self.mCurrentState == None):
            self.mCurrentState.Execute(self._Owner, dt)
            
    def SetState(self, inState):
        if (inState == None):
            return
        
        if (not self.mCurrentState == None):
            self.mCurrentState.Exit(self._Owner)
            
        self.mPreviousState = self.mCurrentState
        print ("Changing state from %r to %r" % (self.mCurrentState, inState))
        self.mCurrentState = inState
        
        self.mCurrentState.Enter(self._Owner)
    
    def RevertToPreviousState(self):
        self.SetState(self.mPreviousState)
        
''' ############################################################# '''
class State():
    def Enter(self, inEntity):
        pass
    def Execute(self, inEntity, inDeltaTime):
        pass
    def Exit(self, inEntity):
        pass
    
''' ############################################################# '''
class StateCatWander():
    _Target = Vector(0,0)
    
    def Enter(self, inCat):
        self._Target = Vector(random.randrange(0, 500), random.randrange(0, 500))
    
    def Execute(self, inCat, dt):
        # Move to target
        myPos = Vector(inCat.pos[0], inCat.pos[1])
        
        vectorToTarget = self._Target - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > inCat.Speed):
            normalizedVectorToTarget *= inCat.Speed
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
            inCat.mStateMachine.SetState(StateCatPoopSearch())
        elif (inCat.Energy <= 10):
            # Sleep
            inCat.mStateMachine.SetState(StateCatTired())
    
    def Exit(self, inCat):
        pass
    
''' ############################################################# '''
class StateCatSearchFood():
    def Enter(self, inCat):
        pass
    
    def Execute(self, inCat, dt):
        pass
    
    def Exit(self, inCat):
        pass
    
''' ############################################################# '''
class StateCatEatFood():
    def Enter(self, inCat):
        pass
    
    def Execute(self, inCat, dt):
        pass
    
    def Exit(self, inCat):
        pass
    
''' ############################################################# '''
class StateCatPoopSearch():
    _LitterBoxLocation = Vector(0, 0)
    
    def Enter(self, inCat):
        # Is there a litterbox nearby?
        from core import engine
        litterBox = engine.GetInstance().mGame.mMap.mLitterBox
        
        if (not litterBox == None):
            # Is the litterbox full?
            if (litterBox.IsFull()):
                # Poo wherever we are!
                inCat.mStateMachine.SetState(StateCatPerformPoop())
            
            # Otherwise, let's go to the litterbox
            self._LitterBoxLocation = Vector(litterBox.x, litterBox.y)
            
    def Execute(self, inCat, dt):
        # Walk to the box until we are close enough
        myPos = Vector(inCat.pos[0], inCat.pos[1])
        
        vectorToTarget = self._LitterBoxLocation - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > inCat.Speed):
            normalizedVectorToTarget *= inCat.Speed
        else:
            normalizedVectorToTarget *= distanceToTarget
            
        myPos += normalizedVectorToTarget
        inCat.pos = myPos
        
        if (myPos == self._LitterBoxLocation):
            # go poo
            inCat.mStateMachine.SetState(StateCatPerformPoop())

    def Exit(self, inCat):
        pass
    
class StateCatPerformPoop():
    def Enter(self, inCat):
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
            pass
        
        # Reset poo
        inCat.LitterBox = 0
        
        # Go back to wander
        inCat.mStateMachine.SetState(StateCatWander())
    
    def Execute(self, inCat, dt):
        pass
    
    def Exit(self, inCat):
        pass
    
    
''' ############################################################# '''
class StateCatTired():
    _EnergyMax = 40
    _SleepPulse = 0
    _SleepPulseTime = 100
    
    def Enter(self, inCat):
        # Am I tired?
        from core import engine
        energy = inCat.Energy
        if (energy >= 0):
            # I'm not tired, go back to the other state.
            inCat.mStateMachine.RevertToPreviousState()
            self._SleepPulse = self._SleepPulseTime
        
    
    def Execute(self, inCat, dt):
        self._SleepPulse -= dt
        if (self._SleepPulse <= 0):
            self._SleepPulse = self._SleepPulseTime
            
            inCat.Energy += 1
            if (inCat.Energy >= self._EnergyMax):
                inCat.mStateMachine.SetState(StateCatWander())            
    
    def Exit(self, inCat):
        pass