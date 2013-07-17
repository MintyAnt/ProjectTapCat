'''
Created on Jul 16, 2013

@author: MintyAnt
'''

from .entity import Entity
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder

Builder.load_file('game/entities/FoodBowl.kv')

class FoodBowlWidget(Entity):
    mFoodValue = NumericProperty(0)
    
    def GetFood(self):
        return self.mFoodValue
    
    def ModifyFood(self, inFoodModification):
        self.mFoodValue += inFoodModification
    
    def IsThereFoodInBowl(self):
        return self.mFoodValue > 0