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
        from .ai.statemachine.statemachine import StateMachine
        from .ai.utilitybased.utility_based_ai import UtilityBasedAI
        from core.graphic.animation_controller import AnimationController
        
        print ("And he said, be initialized! Entity.")
        
        for currentChild in self.children:

            if isinstance(currentChild, StateMachine) \
                or isinstance(currentChild, UtilityBasedAI) \
                or isinstance(currentChild, AnimationController):
                currentChild.Initialize(self)
    
    def Update(self, dt):
        if (self.mStateMachine != None):
            self.mStateMachine.Update(dt)
        if (self.mUtilityBasedAI != None):
            self.mUtilityBasedAI.Update(dt)