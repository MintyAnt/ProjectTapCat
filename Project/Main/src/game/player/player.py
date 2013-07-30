'''
Created on Jul 27, 2013

@author: MintyAnt
'''

from .inventory import Inventory

class Player():
    def __init__(self):
        self.mInventory = Inventory()