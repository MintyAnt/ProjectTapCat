'''
Created on Jul 14, 2013

@author: MintyAnt
'''


def BuildAction(inActionName):
    #Cat
    from .cat import action_cat_eat
    from .cat import action_cat_poop
    from .cat import action_cat_sleep
    from .cat import action_cat_wander
    
    if (inActionName == "cat_eat"):
        return action_cat_eat.ActionCatEat()
    elif (inActionName == "cat_poop"):
        return action_cat_poop.ActionCatPoop()
    elif (inActionName == "cat_sleep"):
        return action_cat_sleep.ActionCatSleep()
    elif (inActionName == "cat_wander"):
        return action_cat_wander.ActionCatWander()
    
    return None
    
class Action():
    def IsDone(self, inEntity):
        pass
    
    def GetUtility(self, inEntity):
        pass
    
    def Enter(self, inEntity):
        pass
    
    def Update(self, inEntity, dt):
        pass
    
    def Exit(self, inEntity):
        pass