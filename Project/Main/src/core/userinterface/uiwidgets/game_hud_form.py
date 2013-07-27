'''
Created on Jul 24, 2013

@author: MintyAnt
'''

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

Builder.load_file('core/userinterface/uiwidgets/GameHUDForm.kv')
#Builder.load_file('uiwidgets/GameHUDForm.kv')

class GameHUDForm(Widget):
    mMap = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(GameHUDForm, self).__init__(**kwargs)
        
        #from core import engine
        #mMap = engine.GetInstance().mGame.mMap