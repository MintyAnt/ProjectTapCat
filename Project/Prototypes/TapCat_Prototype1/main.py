'''
Created on Apr 23, 2013

@author: MintyAnt
'''
import statemachine
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector

gShittyGameSingleton = None

class TapCatApp(App):
    def build(self):
        return GetGameInstnace()

def GetGameInstnace():
    global gShittyGameSingleton
    if (gShittyGameSingleton == None):
        gShittyGameSingleton = TapCatGame()
    return gShittyGameSingleton
    
class TapCatGame(Widget):
    cat = ObjectProperty(None)
    litterBox = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        
        super(TapCatGame, self).__init__(**kwargs)

'''
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
CAT
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
class TheCatWidget(Widget):
    _StateMachine = None
    
    cat_label = StringProperty("")
    cat_talk_label = StringProperty("")
    
    Hapiness = NumericProperty(25)
    Energy = NumericProperty(40)
    Hygine = NumericProperty(30)
    LitterBox = NumericProperty(24)
    
    _HapinessPulse = 0
    _EnergyPulse = 0
    _HyginePulse = 0
    _LitterboxPulse = 0
    
    _LabelPulse = 0
    _CatTalkPulse = 0
    _RandomTalkPulse = random.randint(1, 10)
    
    _Speed = 2.5
    _Heading = Vector(0,0)
    
    _MarkedMoveDirection = None
    _CatPetMeter = 10
    _CatPetCounter = 0
    
    def __init__(self, **kwargs):
        super(TheCatWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
        
        self._StateMachine = statemachine.StateMachine(self)
        self._StateMachine.SetState(statemachine.StateCatWander())
        self._CatPettingCounter = 0
    
    def Update(self, dt):
        # States
        self._StateMachine.Update(dt)
        
        # Pulse crap
        self._LabelPulse -= dt
        self._CatTalkPulse -= dt
        self._RandomTalkPulse -= dt
        self._HapinessPulse -= dt
        self._EnergyPulse -= dt
        self._HyginePulse -= dt
        self._LitterboxPulse -= dt
        
        if (self._LitterboxPulse <= 0):
            self.LitterBox += 2
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
            self._HapinessPulse = 5.25
        
    def on_touch_down(self, touch):
        if (self.collide_point(touch.x, touch.y)):
            print ("touched!")
            
            self._CatPettingCounter += 1
            if (self._CatPettingCounter >= 7):
                # Perform pet
                self._CatPettingCounter = 0
                self.cat_label = "Hapiness+"
                self._LabelPulse = .5
                self.Hapiness += 1
            
    def on_touch_move(self, touch):
        if (self._MarkedMoveDirection == None):
            self._MarkedMoveDirection = Vector(touch.px - touch.x, touch.py - touch.y)
            return
        
        # Whats the current move direction
        currentMoveDir = Vector(touch.px - touch.x, touch.py - touch.y)
        
        # Rotation between this vector and our marked
        angleBetween = currentMoveDir.angle(self._MarkedMoveDirection)
        if (angleBetween >= 90 or angleBetween <= -90):
            # Do things
            self._MarkedMoveDirection = currentMoveDir
            
            self._CatPettingCounter += 1
            
            if (self._CatPettingCounter >= 7):
                # Perform pet
                self._CatPettingCounter = 0
                self.cat_label = "Hapiness+"
                self._LabelPulse = .5
                self.Hapiness += 1
    
    def on_touch_up(self, touch):
        self._MarkedMoveDirection = None

class TheLitterBoxWidget(Widget):
    #DisplayLitter = StringProperty("0/0")
    _LitterCount = NumericProperty(0)
    _MaxLitter = NumericProperty(50)
    
    def __init__(self, **kwargs):
        super(TheLitterBoxWidget, self).__init__(**kwargs)
        #self.UpdateText()
        
    def PerformPoo(self, inCat):
        # Add poo to us
        catLitterValue = 10#inCat.LitterBox
        print ("litter value", catLitterValue)
        self._LitterCount += catLitterValue
        print ("litter count", self._LitterCount)
        #self.UpdateText()
        
        # Update the graphix
    def IsFull(self):
        return (self._LitterCount >= self._MaxLitter)
        
    def UpdateText(self):
        self.DisplayLitter = ("%d/%d" % (self._LitterCount, self._MaxLitter))
        
'''
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
MAIN
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
if __name__ in ('__main__', '__android__'):
    TapCatApp().run()