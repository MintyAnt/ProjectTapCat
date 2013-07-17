'''
Created on Jul 14, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from . import action

class UtilityBasedAI(Widget):
    mDefaultAction = StringProperty("")
    mActions = ListProperty([])
    
    mCurrentAction = None
    _Actions = []
    _DefaultAction = None
    _Owner = None
    
    def __init__(self, **kwargs):
        super(UtilityBasedAI, self).__init__(**kwargs)
    
    def Initialize(self):
        print ("Initializing Utility")
        
        print ("Default Action: ", self.mDefaultAction)
        self._DefaultAction = action.BuildAction(self.mDefaultAction)
        assert self._DefaultAction != None
        self.mCurrentAction = self._DefaultAction
        
        for actionName in self.mActions:
            newAction = action.BuildAction(actionName)
            if (newAction != None):
                assert (not newAction in self._Actions)
                self._Actions.append(newAction)
                
        # Hope this works!
        self._Owner = self.parent
    
    def Update(self, dt):
        bIsCurrentActionDone = True
        if (self.mCurrentAction != None):
            self.mCurrentAction.Update(self._Owner, dt)
            bIsCurrentActionDone = self.mCurrentAction.IsDone(self._Owner)
        
        if (bIsCurrentActionDone):
            # Determine next action.
            self.CalculateAndTrySwitchToNextAction()
        
    def CalculateAndTrySwitchToNextAction(self):
        highestAction = self._DefaultAction
        highestActionUtility = self._DefaultAction.GetUtility(self._Owner)
        
        #Iterate through all actions. Calculate highest
        for currentAction in self._Actions:
            
            currentWeight = currentAction.GetUtility(self._Owner)
            if (currentWeight >= highestActionUtility):
                highestAction = currentAction
                highestActionUtility = currentWeight
        
        if (highestAction != self.mCurrentAction):
            print ("Switching from " , self.mCurrentAction , " to " , highestActionUtility)
            # Switch to this action.
            self.mCurrentAction.Exit(self._Owner)
            self.mCurrentAction = highestAction
            self.mCurrentAction.Enter(self._Owner)
            