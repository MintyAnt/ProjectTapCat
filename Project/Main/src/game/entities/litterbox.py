'''
Created on Jun 18, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.lang import Builder

Builder.load_file('game/entities/LitterBox.kv')

class LitterBoxWidget(Widget):
    mbIsExpired = False
    #DisplayLitter = StringProperty("0/0")
    _LitterCount = NumericProperty(0)
    _MaxLitter = NumericProperty(50)
    
    def __init__(self, **kwargs):
        super(LitterBoxWidget, self).__init__(**kwargs)
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
        