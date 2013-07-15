'''
Created on Jul 15, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

class Entity(Widget):
    mStateMachine = ObjectProperty(None)
    mUtilityBasedAI = ObjectProperty(None)
    
    mbIsExpired = False
    
    def Initialize(self):
        print ("And he said, be initialized! Entity.")
        if (self.mStateMachine != None):
            self.mStateMachine.Initialize()
        if (self.mUtilityBasedAI != None):
            self.mUtilityBasedAI.Initialize()
    
    def Update(self, dt):
        if (self.mStateMachine != None):
            self.mStateMachine.Update(dt)
        if (self.mUtilityBasedAI != None):
            self.mUtilityBasedAI.Update(dt)