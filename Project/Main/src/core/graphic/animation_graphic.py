'''
Created on Jul 13, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty

class AnimationGraphic(Widget):
    mID = StringProperty("")
    mSpriteStrip = ObjectProperty(None)
    mNumFrames = NumericProperty(0)
    mFrameDimensions = ListProperty([0, 0])
    mAnimateSpeed = NumericProperty(0)
    
    mCurrentTextureArea = None
    
    _CurrentFrame = 0
    _AnimatePulse = 0
    
    def Initialize(self):
        pass
    
    def Start(self):
        self._AnimatePulse = self.mAnimateSpeed
    
    def Stop(self):
        pass
    
    def Update(self, dt):
        # Move to the next frame if our animation speed is up.
        self._AnimatePulse -= dt
        if (self._AnimatePulse <= 0):
            self._AnimatePulse = self.mAnimateSpeed
            
            # Animate to the next box.
            self._CurrentFrame++
            if (self._CurrentFrame >= self.mNumFrames):
                self._CurrentFrame = 0
                
            newFrameX = mFrameDimensions[0] * self._CurrentFrame
            newFrameY = 0
            # Set the new area
            mCurrentTextureArea = mSpriteStrip.texture.get_region(newFrameX, newFrameY, mFrameDimensions[0], mFrameDimensions[1])
            mCurrentTextureArea = Image(mCurrentTextureArea)
            
            