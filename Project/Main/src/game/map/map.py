'''
Created on Jun 18, 2013

@author: MintyAnt
'''

from ..entities.entity import Entity
from ..entities.cat import CatWidget
from ..entities.litterbox import LitterBoxWidget
from ..entities.food_bowl import FoodBowlWidget
from kivy.lang import Builder
from kivy.uix.widget import Widget

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout

from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from functools import partial

Builder.load_file('game/map/TapMap.kv')

class Map(RelativeLayout):
    
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.mMapEntities = []
    
    def add_widget(self, widget):
        super(Map, self).add_widget(widget)
        
    def Initialize(self):
        print ("initing map")
        for currentChild in self.children:
            if isinstance(currentChild, Entity):
                print ("adding widget to map ", currentChild)
                self.mMapEntities.append(currentChild)
            
        for currentEntity in self.mMapEntities:
            currentEntity.Initialize()
    
    def Update(self, dt):
        for currentEntity in self.mMapEntities:
            if (currentEntity.mbIsExpired):
                # Destroy
                self.mMapEntities.remove(currentEntity)
                self.remove_widget(currentEntity)
            else:
                currentEntity.Update(dt)