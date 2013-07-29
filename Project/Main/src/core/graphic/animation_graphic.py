'''
Created on Jul 13, 2013

@author: MintyAnt
'''

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty

class AnimationGraphic(Widget):
    mID = StringProperty("")
    mSpriteStripSource = StringProperty(None)
    mNumFrames = NumericProperty(0)
    mFrameDimensions = ListProperty([0, 0])
    mAnimateSpeed = NumericProperty(0)
    
    def Initialize(self):
        self.mSpriteStripSourceImage = Image(source=self.mSpriteStripSource, pos=self.pos)
        self.mCurrentTextureArea = None
        self._CurrentFrameIndex = 0
        self._AnimatePulse = 0
    
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
            self._CurrentFrameIndex = self._CurrentFrameIndex + 1
            if (self._CurrentFrameIndex >= self.mNumFrames):
                self._CurrentFrameIndex = 0
            self.UpdateFrame()
            
    def UpdateFrame(self):
        newFrameX = self.mFrameDimensions[0] * self._CurrentFrameIndex
        newFrameY = 0
        
        # Set the new area
        self.mCurrentTextureArea = self.mSpriteStripSourceImage.texture.get_region(newFrameX, newFrameY, self.mFrameDimensions[0], self.mFrameDimensions[1])
        #self.mCurrentTextureArea = Image(texture=self.mCurrentTextureArea)
        #self.mCurrentTextureArea.reload()
        