'''
Created on Jul 20, 2013

@author: MintyAnt
'''

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from ..menu_profile_widget import MenuProfileWidget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import Screen

Builder.load_file('core/userinterface/uiwidgets/screens/MainMenuScreen.kv')
#Builder.load_file('uiwidgets/screens/MainMenuScreen.kv')

class MainMenuScreen(Screen):
    pass