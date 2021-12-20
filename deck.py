# -*- coding: utf-8 -*-
"""
Giovanni Minor
Created on Mon Nov 22 16:35:06 2021

@author: Giomi
"""
import random 
from card import Card
class Deck:
    def __init__(self):
        self.cards = []
        #cards
        numbers = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
        #card typw
        suits = ['s', 'c', 'h', 'd']
        for number in numbers:
            for suit in suits:
                self.cards.append(Card(number, suit))
    def shuffle(self):
        #shuffling cards
        random.shuffle(self.cards)
    def __str__(self):
        return(" ".join([str(c) for c in self.cards]))
    def removeCard(self):
        #taking a card
        i = random.randrange(0, len(self.cards))
        return(self.cards.pop(i))
        
        