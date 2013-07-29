'''
Created on Jun 18, 2013

@author: MintyAnt
'''

from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.lang import Builder
from . import poo
import random
from .entity import Entity

Builder.load_file('game/entities/LitterBox.kv')

class LitterBoxWidget(Entity):
    _LitterCount = NumericProperty(40)
    _MaxLitter = NumericProperty(50)
    
    def __init__(self, **kwargs):
        super(LitterBoxWidget, self).__init__(**kwargs)
        
        self._LitterboxPoo = []
    
    def PerformPoo(self, inCat):
        # Add poo to us
        catLitterValue = 10#inCat.LitterBox
        print ("litter value", catLitterValue)
        self._LitterCount += catLitterValue
        print ("litter count", self._LitterCount)
        #self.UpdateText()
        
        from core import engine
        map = engine.GetInstance().mGame.mMap
        newPoo = poo.PooWidget()
        
        rightMostX = self.right - newPoo.width
        rightMostY = self.top - newPoo.height
        
        print ("args are (", self.x, ", ", rightMostX, ") (", self.y, ", ", rightMostY)
        newPoo.pos = random.uniform(self.x, rightMostX), random.uniform(self.y, rightMostY)
        
        map.mMapEntities.append(newPoo) 
        map.add_widget(newPoo)
        
        self._LitterboxPoo.append(newPoo)
        
        # Update the graphix
    def IsFull(self):
        return (self._LitterCount >= self._MaxLitter)
    
    def EmptyBox(self):
        for currentPoo in self._LitterboxPoo:
            currentPoo.mbExpired = True
        
        self._LitterboxPoo = []
        
    def UpdateText(self):
        self.DisplayLitter = ("%d/%d" % (self._LitterCount, self._MaxLitter))
        