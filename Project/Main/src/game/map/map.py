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

Builder.load_file('game/map/TapMap.kv')

class Map(Widget):
    _MapRootElement = None
    mCat = ObjectProperty()
    mLitterBox = ObjectProperty()
    mMapEntities = []
    
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
    
    def Initialize(self):
        self._MapRootElement = self
    
    def Update(self, dt):
        for currentEntity in self.mMapEntities:
            if (currentEntity.mbIsExpired):
                # Destroy
                self.mMapEntities.remove(currentEntity)