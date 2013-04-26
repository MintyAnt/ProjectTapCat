'''
Created on Apr 26, 2013

@author: MintyAnt
'''

class Engine(object):
    '''
    classdocs
    '''
    mUserInterface = None
    mGameStack = []
    mCurrentGame = None
    
    # Specific for kivy. Root of all drawable things.
    _RootWidget = None


    def __init__(self, inRootWidget):
        '''
        Constructor
        '''
        