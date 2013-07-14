'''
Created on Jul 12, 2013

@author: MintyAnt
'''

from functools import partial
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder
from .animation_graphic import Animation

class AnimationController(Widget):
    mAnimations = {}
    _CurrentAnimation = None
    _CurrentImage = None
    
    def add_widget(self, widget):
        if isinstance(widget, Animation) and widget.system_id not in self.systems:
            Clock.schedule_once(partial(self.InitializeAnimation, widget))
        super(AnimationController, self).add_widget(widget)
        
    def InitializeAnimation(self, inAnimationWidget):
        animationID = inAnimationWidget.mID
        assert not animationID in self.mAnimations
        if (not animationID in self.mAnimations):
            self.mAnimations[animationID] = inAnimationWidget
    
    def PlayAnimationByName(self, inAnimationName):
        assert inAnimationName in self.mAnimations
        if (inAnimationName in self.mAnimations):
            self._CurrentAnimation.Stop()
            
            self._CurrentAnimation = self.mAnimations[inAnimationName]
            
            self._CurrentAnimation.Start()
            self._CurrentImage = self._CurrentAnimation.mCurrentTextureArea
    
    def Initialize(self):
        pass
    
    def Update(self, dt):
        self._CurrentAnimation.Update(dt)
        
    