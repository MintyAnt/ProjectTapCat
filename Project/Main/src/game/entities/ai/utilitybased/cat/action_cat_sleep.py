'''
Created on Jul 14, 2013

@author: MintyAnt
'''

import math
from ..action import Action

class ActionCatSleep(Action):
    
    def __init__(self):
        self._bIsDone = False
        self._SleepPulse = 0
        self._SleepPulseTime = 1
        
        
    def IsDone(self, inCat):
        doneValue = inCat.mEnergy > (inCat.mEnergyMax / 2.0)
        return doneValue
    
    def GetUtility(self, inCat):
        returnValue = 1.0 - ( (inCat.mEnergy / inCat.mEnergyMax))
        if (inCat.mUtilityBasedAI.mCurrentAction != self):
            returnValue = math.pow(returnValue, 2)
            
        print ("Sleep ", returnValue)
        return returnValue
    
    def Enter(self, inCat):
        self._bIsDone = False
        
        # Am I tired?
        from core import engine
        energy = inCat.mEnergy
        if (energy >= inCat.mEnergyMax):
            # I'm not tired, go back to the other state.
            self._bIsDone = True
            self._SleepPulse = self._SleepPulseTime
    
    def Update(self, inCat, dt):
        self._SleepPulse -= dt
        if (self._SleepPulse <= 0):
            self._SleepPulse = self._SleepPulseTime
            
            inCat.mEnergy += 1
            if (inCat.mEnergy >= inCat.mEnergyMax):
                self._bIsDone = False
    
    def Exit(self, inCat):
        self._bIsDone = True
        
    def __repr__(self):
        return "action_cat_sleep"