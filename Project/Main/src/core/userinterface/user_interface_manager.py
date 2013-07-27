'''
Created on Jul 20, 2013

@author: MintyAnt
'''

from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from uiwidgets.main_menu_form import MainMenuForm
from uiwidgets.game_hud_form import GameHUDForm

Builder.load_file('core/userinterface/UserInterfaceManager.kv')
#Builder.load_file('UserInterfaceManager.kv')

class UserInterfaceManager(Widget):
    mMap = ObjectProperty()

from kivy.app import App

class TapCatApp(App):
    def build(self):
        return UserInterfaceManager()

if __name__ == '__main__':
    TapCatApp().run()