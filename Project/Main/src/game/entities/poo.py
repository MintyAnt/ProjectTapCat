'''
Created on Jun 26, 2013

@author: MintyAnt
'''

from kivy.clock import Clock
from kivy.lang import Builder
from .entity import Entity

Builder.load_file('game/entities/Poo.kv')

class PooWidget(Entity):
    _LifeTime = 5
    
    def __init__(self, **kwargs):
        super(PooWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
        
    def Update(self, dt):
        pass