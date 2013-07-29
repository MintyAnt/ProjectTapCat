'''
Created on Jun 16, 2013

@author: MintyAnt
'''

from game.game import Game
from kivy.clock import Clock

gEngineInstance = None

def CreateInstance():
    global gEngineInstance
    gEngineInstance = Engine()
    
def GetInstance():
    global gEngineInstance
    assert gEngineInstance != None, "Engine should be created with CreateInstance, otherwise loading will screw up"
    if (gEngineInstance == None):
        gEngineInstance = Engine()
    return gEngineInstance

class Engine():
    def __init__(self):
        self.mGame = None
    
    def GetRoot(self):
        self.mGame = Game()
        return self.mGame
    
    def Initialize(self, dt):
        self.mGame.Initialize()
        Clock.schedule_interval(self.Update, 1.0 / 60.0)
        
    def Update(self, dt):
        self.mGame.Update(dt)