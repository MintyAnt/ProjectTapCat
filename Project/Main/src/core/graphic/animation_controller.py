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
    
    def __init__(self, **kwargs):
        super(AnimationController, self).__init__(**kwargs)
        self.mAnimations = {}
        self._CurrentAnimation = None
        
    def add_widget(self, widget):
        super(AnimationController, self).add_widget(widget)
        
    def InitializeAnimation(self, inAnimationWidget):
        animationID = inAnimationWidget.mID
        print (animationID)
        assert not animationID in self.mAnimations
        if (not animationID in self.mAnimations):
            print ("Initializing Animation %s" % animationID)
            inAnimationWidget.Initialize()
            self.mAnimations[animationID] = inAnimationWidget
    
    def PlayAnimationByName(self, inAnimationName):
        assert inAnimationName in self.mAnimations, "No animation named " + inAnimationName
        if (inAnimationName in self.mAnimations):
            if (self._CurrentAnimation != None):
                self._CurrentAnimation.Stop()
            
            self._CurrentAnimation = self.mAnimations[inAnimationName]
            print ("New Animation: ", self._CurrentAnimation)
            
            self._CurrentAnimation.Start()
            self._CurrentImage.texture = self._CurrentAnimation.mCurrentTextureArea
            print ("Current image: ", self._CurrentImage)

    def Initialize(self, inOwner):
        for currentChild in self.children:
            if isinstance(currentChild, AnimationGraphic):
                print ("Scheduling animaton add")
                self.InitializeAnimation(currentChild)
        
        self._CurrentImage = Image(pos=inOwner.pos)
        self.bind(pos=self._CurrentImage.setter('pos'))
        self.add_widget(self._CurrentImage)
        
        self.PlayAnimationByName(self.mStartingAnimation)

    def Update(self, dt):
        if (self._CurrentAnimation != None):
            self._CurrentAnimation.Update(dt)
            
            self._CurrentImage.texture = self._CurrentAnimation.mCurrentTextureArea
    