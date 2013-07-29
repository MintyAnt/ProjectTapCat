'''
Created on Jul 15, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

class Entity(Widget):
    
    def __init__(self, **kwargs):
        super(Entity, self).__init__(**kwargs)
        
        # A list of entities that contian common methods that we use, such as Update or Initialize
        self.mCustomEntities = []
        self.mbIsExpired = False
    
    def Initialize(self):    
        from .ai.statemachine.statemachine import StateMachine
        from .ai.utilitybased.utility_based_ai import UtilityBasedAI
        from core.graphic.animation_controller import AnimationController
        
        print ("inniting, list is ", self.mCustomEntities)
        for currentChild in self.children:
            if isinstance(currentChild, StateMachine) \
                or isinstance(currentChild, UtilityBasedAI) \
                or isinstance(currentChild, AnimationController):
                currentChild.Initialize(self)
                self.mCustomEntities.append(currentChild)
                print ("Appending child ", currentChild, " to ", self)
    
    def Update(self, dt):
        for currentCustomEntity in self.mCustomEntities:
            currentCustomEntity.Update(dt)