'''
Created on Jul 13, 2013

@author: MintyAnt
'''

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty

class AnimationGraphic(Widget):
    mID = StringProperty("")
    mSpriteStrip = StringProperty(None)
    mNumFrames = NumericProperty(0)
    mFrameDimensions = ListProperty([0, 0])
    mAnimateSpeed = NumericProperty(0)
    
    mCurrentTextureArea = None
    
    _CurrentFrame = 0
    _AnimatePulse = 0
    mSpriteStripImage = None
    
    def Initialize(self):
        self.mSpriteStripImage = Image(source=self.mSpriteStrip, pos=self.pos)
    
    def Start(self):
        self.UpdateFrame()
        self._AnimatePulse = self.mAnimateSpeed
    
    def Stop(self):
        pass
    
    def Update(self, dt):
        # Move to the next frame if our animation speed is up.
        self._AnimatePulse -= dt
        if (self._AnimatePulse <= 0):
            self._AnimatePulse = self.mAnimateSpeed
            
            # Animate to the next box.
            self._CurrentFrame = self._CurrentFrame + 1
            if (self._CurrentFrame >= self.mNumFrames):
                self._CurrentFrame = 0
            self.UpdateFrame()
            
    def UpdateFrame(self):
        newFrameX = self.mFrameDimensions[0] * self._CurrentFrame
        newFrameY = 0
        
        # Set the new area
        self.mCurrentTextureArea = self.mSpriteStripImage.texture.get_region(newFrameX, newFrameY, self.mFrameDimensions[0], self.mFrameDimensions[1])
        #self.mCurrentTextureArea = Image(texture=self.mCurrentTextureArea)
        #self.mCurrentTextureArea.reload()
        