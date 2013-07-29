'''
Created on Jun 16, 2013

@author: MintyAnt
'''

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from .map.map import Map
from core.userinterface.user_interface_manager import UserInterfaceManager

Builder.load_file('game/TapCatGame.kv')

class Game(FloatLayout):
    mMap = ObjectProperty()
    mUserInterface = ObjectProperty()
        
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
    
    def Initialize(self):
        self.mMap = Map(size_hint= (1, .8), pos_hint = {'top' : 1})
        self.mUserInterface = UserInterfaceManager(size = self.size)
        
        self.add_widget(self.mMap)
        self.add_widget(self.mUserInterface)
        
        self.mMap.Initialize()
        self.mUserInterface.Initialize()
        
    def Update(self, dt):
        self.mMap.Update(dt)
        self.mUserInterface.Update(dt)