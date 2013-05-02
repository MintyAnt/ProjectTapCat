'''
Created on Apr 23, 2013

@author: MintyAnt
'''
import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector

class TapCatApp(App):
    def build(self):
        return TapCatGame()

class TapCatGame(Widget):
    cat = ObjectProperty(None)

'''
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
CAT
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
class TheCatWidget(Widget):
    cat_label = StringProperty("")
    cat_talk_label = StringProperty("")
    
    Hapiness = NumericProperty(100)
    Energy = NumericProperty(40)
    Hygine = NumericProperty(30)
    LitterBox = NumericProperty(30)
    
    _HapinessPulse = 0
    _EnergyPulse = 0
    _HyginePulse = 0
    _LitterboxPulse = 0
    
    _LabelPulse = 0
    _CatTalkPulse = 0
    _RandomTalkPulse = random.randint(1, 10)
    
    _Speed = 2.5
    _Heading = Vector(0,0)
    _Target = Vector(0,0)
    
    def __init__(self, **kwargs):
        super(TheCatWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
        self._Target = Vector(random.randrange(0, 500), random.randrange(0, 500))
    
    def Update(self, dt):
        # Moving
        self.UpdateMovement(dt)
        
        # Pulse crap
        self._LabelPulse -= dt
        self._CatTalkPulse -= dt
        self._RandomTalkPulse -= dt
        self._HapinessPulse -= dt
        self._EnergyPulse -= dt
        self._HyginePulse -= dt
        self._LitterboxPulse -= dt
        
        if (self._LitterboxPulse <= 0):
            self.LitterBox -= 2
            self._LitterboxPulse = 12
            
        if (self._EnergyPulse <= 0):
            self.Energy -= 1
            self._EnergyPulse = 9
            
        if (self._HyginePulse <= 0):
            self.Hygine -= 1
            self._HyginePulse = 6
        
        if (self._LabelPulse <= 0):
            self.cat_label = ""
            
        if (self._RandomTalkPulse <= 0 and self._CatTalkPulse <= 0):
            self.cat_talk_label = "meow"
            self._CatTalkPulse = 1
            self._RandomTalkPulse = random.randint(1, 10)
            
        if (self._CatTalkPulse <= 0):
            self.cat_talk_label = ""
        
        if (self._HapinessPulse <= 0):
            self.Hapiness -= 1
            self._HapinessPulse = 60
            
    def UpdateMovement(self, dt):
        # Move to target
        myPos = Vector(self.pos[0], self.pos[1])
        
        vectorToTarget = self._Target - myPos
        distanceToTarget = vectorToTarget.length()
        normalizedVectorToTarget = vectorToTarget.normalize()
        if (distanceToTarget > self._Speed):
            normalizedVectorToTarget *= self._Speed
        else:
            normalizedVectorToTarget *= distanceToTarget
            
        myPos += normalizedVectorToTarget
        self.pos = myPos
        
        if (myPos == self._Target):
            # find a new target
            self._Target = Vector(random.randrange(0, 500), random.randrange(0, 500))
        
    def on_touch_down(self, touch):
        if (self.collide_point(touch.x, touch.y)):
            print ("touched!")
            self.cat_label = "Hapiness+"
            self._LabelPulse = 1
            self.Hapiness += 1
            
    def on_touch_move(self, touch):
        pass
    
    def on_touch_up(self, touch):
        pass

'''
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
MAIN
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
if __name__ in ('__main__', '__android__'):
    TapCatApp().run()