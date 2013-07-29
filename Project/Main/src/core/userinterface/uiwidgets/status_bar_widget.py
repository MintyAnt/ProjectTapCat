'''
Created on Jul 28, 2013

@author: MintyAnt
'''

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.progressbar import ProgressBar
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty

Builder.load_file('core/userinterface/uiwidgets/StatusBarWidget.kv')

class StatusBarWidget(ProgressBar):
    statusName = StringProperty("Undefined")