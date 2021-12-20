# -*- coding: utf-8 -*-
"""
Giovanni Minor
Created on Sat Dec  4 10:13:30 2021

@author: Giomi
"""


class Hand:
    def __init__(self, deck):
        #Card display
        self.cards = [deck.removeCard(), deck.removeCard()]
        
    def __str__(self):
        return(" ".join([str(c) for c in self.cards]))
    def hit(self, deck):
        self.cards.append(deck.removeCard())
    def value(self):
        #total card value
        s = sum(card.getValue() for card in self.cards)
        #Ace 11 or 1 value
        if any(card.number == "a" for card in self.cards):
            if s+ 10 <=21:    
                return(s, s+10)
        return(s,)
        
    