'''
Created on Jun 16, 2013

@author: MintyAnt


'''

from kivy.app import App
from core import engine
from kivy.clock import Clock

class TapCatApp(App):
    def build(self):
        print ("Core startup beginning.")
        
        #from kivy.config import Config
        #Config.set('graphics', 'width', '163')
        #Config.set('graphics', 'height', '272')

        engine.CreateInstance()
        tapEngine = engine.GetInstance()
        rootElement = tapEngine.GetRoot()
        
        Clock.schedule_once(tapEngine.Initialize)
        
        print ("Core startup complete, root element is being returned.")
        return rootElement

if __name__ == '__main__':
    TapCatApp().run()
