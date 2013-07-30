'''
Created on Jun 26, 2013

@author: MintyAnt
'''

from kivy.clock import Clock
from kivy.lang import Builder
from .entity import Entity

Builder.load_file('game/entities/Poo.kv')

class PooWidget(Entity):
    
    def __init__(self, **kwargs):
        super(PooWidget, self).__init__(**kwargs)
        
    def Update(self, dt):
        super(PooWidget, self).Update(dt)
        
    def on_touch_up(self, touch):
        super(PooWidget, self).on_touch_up(touch)
        
        if self.collide_point(touch.x, touch.y):
            # Get current item
            from game.items.item_poop_scoop import ItemPoopScoop
            from core import engine
            engineInstance = engine.GetInstance()
            selectedItem = engineInstance.mGame.mPlayer.mInventory.GetSelectedItem()
            
            print ("Selected item: ", selectedItem)
            
            if isinstance(selectedItem, ItemPoopScoop):
                # Clean self up!
                self.mbIsExpired = True