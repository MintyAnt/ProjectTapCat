'''
Created on Jun 18, 2013

@author: MintyAnt
'''

import random
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.vector import Vector
from . import statemachine

Builder.load_file('game/entities/Cat.kv')


class CatWidget(Widget):
    mbIsExpired = False
    mStateMachine = None
    
    # Exposed Values #
    # Cat Values
    Speed = NumericProperty(1.0)
    
    # Cat Gui Stuff
    cat_label = StringProperty("")
    cat_talk_label = StringProperty("")
    
    # Cat Levels
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
    
    _Heading = Vector(0,0)
    
    _MarkedMoveDirection = None
    _CatPetMeter = 10
    _CatPetCounter = 0
    
    def __init__(self, **kwargs):
        super(CatWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
        
        self.mStateMachine = statemachine.StateMachine(self)
        self.mStateMachine.SetState(statemachine.StateCatWander())
        self._CatPettingCounter = 0
    
    def Update(self, dt):
        # States
        self.mStateMachine.Update(dt)
        
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