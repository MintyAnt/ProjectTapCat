'''
Created on Jul 20, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from uiwidgets.screens.main_menu_screen import MainMenuScreen
from uiwidgets.screens.game_hud_screen import GameHUDScreen
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('core/userinterface/UserInterfaceManager.kv')
#Builder.load_file('UserInterfaceManager.kv')

class UserInterfaceManager(ScreenManager):
    mMap = ObjectProperty()
    
    def Initialize(self):
        pass

    def Update(self, dt):
        pass

from kivy.app import App

class TapCatApp(App):
    def build(self):
        return UserInterfaceManager()

if __name__ == '__main__':
    TapCatApp().run()