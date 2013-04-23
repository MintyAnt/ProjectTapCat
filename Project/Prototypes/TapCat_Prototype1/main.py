'''
Created on Apr 23, 2013

@author: MintyAnt
'''
import kivy

from kivy.app import App
from kivy.uix.label import Label

class TapCatApp(App):
    
    def build(self):
        return Label(text='PROJECT: TAPCAT')

if __name__ in ('__main__', '__android__'):
    TapCatApp().run()