'''
Created on Jun 16, 2013

@author: MintyAnt
'''

from kivy.app import App
from core import engine

class TapCatApp(App):
    def build(self):
        tapEngine = engine.GetInstance()
        rootElement = tapEngine.GetRoot()
        return rootElement

if __name__ == '__main__':
    TapCatApp().run()