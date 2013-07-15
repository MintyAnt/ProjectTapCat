'''
Created on Jun 16, 2013

@author: MintyAnt
'''

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from .map.map import Map


Builder.load_file('game/TapCatGame.kv')

class Game(Widget):
    # Private #
    # The root element that the entire game stems from. Just for clarity, as self can be used.
    # I would expect the game to have as children the UI and the Map
    _GameRootElement = None
    mMap = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
    
    def Initialize(self):
        self._GameRootElement = self
        self.mMap.Initialize()
        
    def Update(self, dt):
        self.mMap.Update(dt)