'''
Created on Jun 16, 2013

@author: MintyAnt
'''

from game.game import Game

gEngineInstance = None

def GetInstance():
    global gEngineInstance
    if (gEngineInstance == None):
        gEngineInstance = Engine()
    return gEngineInstance

class Engine():
    mGame = None
    
    def __init__(self):
        pass
    
    def Initialize(self):
        self.mGame = Game()
        
        self.mGame.Initialize()
        tapRoot = self.mGame
        
        return tapRoot