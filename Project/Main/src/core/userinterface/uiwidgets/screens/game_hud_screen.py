'''
Created on Jul 24, 2013

@author: MintyAnt
'''

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from ..status_bar_widget import StatusBarWidget
from game.items.item_food import ItemFood
from game.items.item_poop_scoop import ItemPoopScoop

Builder.load_file('core/userinterface/uiwidgets/screens/GameHUDScreen.kv')
#Builder.load_file('uiwidgets/screens/GameHUDScreen.kv')

class GameHUDScreen(Screen):
    mMap = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(GameHUDScreen, self).__init__(**kwargs)
        
        #from core import engine
        #mMap = engine.GetInstance().mGame.mMap