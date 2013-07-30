'''
Created on Jul 16, 2013

@author: MintyAnt
'''

from .entity import Entity
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder

Builder.load_file('game/entities/FoodBowl.kv')

class FoodBowlWidget(Entity):
    mFoodValue = NumericProperty(10)
    
    def __init__(self, **kwargs):
        super(FoodBowlWidget, self).__init__(**kwargs)
        
    def GetFood(self):
        return self.mFoodValue
    
    def ModifyFood(self, inFoodModification):
        self.mFoodValue += inFoodModification
    
    def IsThereFoodInBowl(self):
        return (self.mFoodValue > 0)
    
    def Update(self, dt):
        super(FoodBowlWidget, self).Update(dt)
        
    def on_touch_up(self, touch):
        super(FoodBowlWidget, self).on_touch_up(touch)
        
        if self.collide_point(touch.x, touch.y):
            # Get current item
            from game.items.item_food import ItemFood
            from core import engine
            engineInstance = engine.GetInstance()
            selectedItem = engineInstance.mGame.mPlayer.mInventory.GetSelectedItem()
            
            if isinstance(selectedItem, ItemFood):
                # Clean self up!
                self.mFoodValue += 10