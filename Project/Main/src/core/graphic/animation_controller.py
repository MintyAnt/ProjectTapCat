'''
Created on Jul 12, 2013

@author: MintyAnt
'''

from functools import partial
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder

class AnimationController(Widget):
    mAnimations = {}
    _CurrentAnimation = None
    
    
    def add_widget(self, widget):
        if isinstance(widget, Animation) and widget.system_id not in self.systems:
            Clock.schedule_once(partial(self.InitializeAnimation, widget))
        super(AnimationController, self).add_widget(widget)
        
    def InitializeAnimation(self, inAnimationWidget):
        pass
    
    def PlayAnimationByName(self, inAnimationName):
        pass
    
    def Initialize(self):
        pass
    
    def Update(self, dt):
        self._CurrentAnimation.Update(dt)
        
    