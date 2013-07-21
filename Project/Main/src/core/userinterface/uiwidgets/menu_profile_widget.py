'''
Created on Jul 20, 2013

@author: MintyAnt
'''

from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder
from kivy.animation import Animation

#Builder.load_file('core/userinterface/uiwidgets/MenuProfileWidget.kv')
Builder.load_file('uiwidgets/MenuProfileWidget.kv')


class MenuProfileWidget(StackLayout):
    
    def __init__(self, **kwargs):
        super(MenuProfileWidget, self).__init__(**kwargs)
    
    def on_activation(self, inStartLocation):
        self.pos = inStartLocation
        anim_start = Animation(pos = inStartLocation, duration = 0.001)
        anim_end = Animation(pos = (inStartLocation[0] + self.parent.width / 2.0, inStartLocation[1]), duration = 0.3)
        anim_open = anim_start + anim_end
        anim_open.start(self)
    
    def on_deactivation(self, inEndLocation):
        anim_end = Animation(pos = inEndLocation, duration = 0.3)
        anim_end.start(self)
        