'''
Created on Jul 13, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty

class AnimationGraphic(Widget):
    mSpriteStrip = ObjectProperty(None)
    mNumFrames = NumericProperty(0)
    _CurrentFrame = 0
    mFrameDimensions = ListProperty([0, 0])
    mCurrentTextureArea = None
    
    def Initialize(self):
        pass
    
    def Update(self, dt):
        pass