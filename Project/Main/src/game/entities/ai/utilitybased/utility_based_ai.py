'''
Created on Jul 14, 2013

@author: MintyAnt
'''

class UtilityBasedAI():
    mCurrentAction = None
    _Actions = []
    _DefaultAction = None
    
    def __init__(self):
        pass
    
    def Initialize(self):
        pass
    
    def Update(self, dt):
        bIsCurrentActionDone = True
        if (self.mCurrentAction != None):
            bIsCurrentActionDone = self.mCurrentAction.IsDone()
        
        if (bIsCurrentActionDone):
            # Determine next action.
            self.CalculateAndSwitchToNextAction()
        
    def CalculateAndSwitchToNextAction(self):
        highestAction = self._DefaultAction
        highestActionUtility = self._DefaultAction.GetUtility()
        
        #Iterate through all actions. Calculate highest
        for currentAction in self._Actions:
            
            currentWeight = currentAction.GetUtility()
            if (currentWeight >= highestActionUtility):
                highestAction = currentAction
                highestActionUtility = currentAction.GetUtility()
        
        if (highestActionUtility != self.mCurrentAction):
            # Switch to this action.
            