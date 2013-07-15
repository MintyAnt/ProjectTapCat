'''
Created on Jun 18, 2013

@author: MintyAnt
'''

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from ..entities.cat import CatWidget
from ..entities.litterbox import LitterBoxWidget
from kivy.clock import Clock
from functools import partial
from ..entities.entity import Entity

Builder.load_file('game/map/TapMap.kv')

class Map(Widget):
    mMapRootElement = None
    #mCat = ObjectProperty()
    #mLitterBox = ObjectProperty()
    mMapEntities = []
    
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
    
    def add_widget(self, widget):
        print ("Adding Widget", widget)
        if isinstance(widget, Entity):
            self.mMapEntities.append(widget)
        super(Map, self).add_widget(widget)
        
    def Initialize(self):
        print ("initing map")
        self.mMapRootElement = self
        for currentEntity in self.mMapEntities:
            currentEntity.Initialize()
    
    def Update(self, dt):
        for currentEntity in self.mMapEntities:
            if (currentEntity.mbIsExpired):
                # Destroy
                self.mMapEntities.remove(currentEntity)
                self.mMapRootElement.remove_widget(currentEntity)
            else:
                currentEntity.Update(dt)