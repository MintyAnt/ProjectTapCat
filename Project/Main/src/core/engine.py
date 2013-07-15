'''
Created on Jun 16, 2013

@author: MintyAnt
'''

from game.game import Game
from kivy.clock import Clock

gEngineInstance = None

def GetInstance():
    global gEngineInstance
    if (gEngineInstance == None):
        gEngineInstance = Engine()
    return gEngineInstance

class Engine():
    mGame = None
    _bInitialized = False
    
    def __init__(self):
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
        self.mGame = Game()
    
    def GetRoot(self):
        return self.mGame
    
    def Initialize(self):
        self.mGame.Initialize()
        self._bInitialized = True
        
    def Update(self, dt):
        if (not self._bInitialized):
            self.Initialize()
        self.mGame.Update(dt)