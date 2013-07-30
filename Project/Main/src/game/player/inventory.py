'''
Created on Jul 27, 2013

@author: MintyAnt
'''

from kivy.uix.togglebutton import ToggleButton

class Inventory():
    def GetSelectedItem(self):
        from core import engine
        from game.game import Game
        from core.userinterface.user_interface_manager import UserInterfaceManager
        from core.userinterface.uiwidgets.screens.game_hud_screen import GameHUDScreen

        engineInstance = engine.GetInstance()
        
        #Get the hud
        gameHUDScreen = engineInstance.mGame.mUserInterface.gameHUDScreen
        
        # Get the selected item
        itemSelectionGroup = gameHUDScreen.bottomBar.itemSelectionGroup
        
        for currentChild in itemSelectionGroup.children:
            if isinstance(currentChild, ToggleButton):
                if (currentChild.state == 'down'):
                    return currentChild
                
        return None