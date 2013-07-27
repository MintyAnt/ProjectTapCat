'''
Created on Jun 16, 2013

@author: MintyAnt


'''

from kivy.app import App
from core import engine
from kivy.clock import Clock

class TapCatApp(App):
    def build(self):
        print ("b4")
        engine.CreateInstance()
        tapEngine = engine.GetInstance()
        rootElement = tapEngine.GetRoot()
        
        Clock.schedule_once(tapEngine.Initialize)
        
        print ("aftr")
        return rootElement

if __name__ == '__main__':
    TapCatApp().run()
