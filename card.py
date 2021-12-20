# -*- coding: utf-8 -*-
"""
Giovanni Minor
Created on Mon Nov 22 16:01:32 2021

@author: Giomi
"""

class Card:
    def __init__(self, number,suit):
        self.number = number
        self.suit = suit
    def getValue(self):
        #value of king, jack, and queen
        if self.number in "kjq":
            return(10)
        else:
            #Ace starting value
            if self.number == "a":
                return(1)
            return(int(self.number))
    def __str__(self):
        return(self.number+self.suit)
    