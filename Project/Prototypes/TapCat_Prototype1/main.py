'''
Created on Apr 23, 2013

@author: MintyAnt
'''
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class TapCatApp(App):
    
    def build(self):
        return TapCatGame()

class TapCatGame(Widget):
    pass

class TheCatWidget(Widget):
    def on_touch_down(self, touch):
        downPosInLocalSpace = self.to_widget(touch.x, touch.y)
        print (downPosInLocalSpace)
        #if (self.collide_point(downPosInLocalSpace[0], downPosInLocalSpace[1])):
        if (self.collide_point(touch.x, touch.y)):
            print ("You touched me!")
            print (touch)
        
    def on_touch_move(self, touch):
        pass
    
    def on_touch_up(self, touch):
        pass

if __name__ in ('__main__', '__android__'):
    TapCatApp().run()