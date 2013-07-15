'''
Created on Jul 12, 2013

@author: MintyAnt
'''

from functools import partial
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder
from .animation_graphic import AnimationGraphic

class AnimationController(Widget):
    mStartingAnimation = StringProperty("")
    _CurrentImage = ObjectProperty(None)
    
    mAnimations = {}
    
    _CurrentAnimation = None
    _bInitialized = False
    
    def __init__(self, **kwargs):
        super(AnimationController, self).__init__(**kwargs)
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
        
    def add_widget(self, widget):
        if isinstance(widget, AnimationGraphic):
            Clock.schedule_once(partial(self.InitializeAnimation, widget))
        print ("Widget: ", widget)
        super(AnimationController, self).add_widget(widget)
        
    def InitializeAnimation(self, inAnimationWidget, dt):
        animationID = inAnimationWidget.mID
        print (animationID)
        assert not animationID in self.mAnimations
        if (not animationID in self.mAnimations):
            #inAnimationWidget.pos = self.pos
            inAnimationWidget.Initialize()
            self.mAnimations[animationID] = inAnimationWidget
    
    def PlayAnimationByName(self, inAnimationName):
        assert inAnimationName in self.mAnimations
        if (inAnimationName in self.mAnimations):
            if (self._CurrentAnimation != None):
                self._CurrentAnimation.Stop()
            
            self._CurrentAnimation = self.mAnimations[inAnimationName]
            print ("New Animation: ", self._CurrentAnimation)
            
            self._CurrentAnimation.Start()
            self._CurrentImage.texture = self._CurrentAnimation.mCurrentTextureArea
            print ("Current image: ", self._CurrentImage)
            
    def Initialize(self):
        self._CurrentImage = Image(pos=self.parent.pos)
        self.bind(pos=self._CurrentImage.setter('pos'))
        self.add_widget(self._CurrentImage)
        
        self.PlayAnimationByName(self.mStartingAnimation)
        self._bInitialized = True
    
    def Update(self, dt):
        if (not self._bInitialized):
            self.Initialize()
        
        if (self._CurrentAnimation != None):
            self._CurrentAnimation.Update(dt)
            
            self._CurrentImage.texture = self._CurrentAnimation.mCurrentTextureArea
    