"""
Giovanni Minor
Created on Mon Nov 22 16:46:54 2021

@author: Giomi
"""

from deck import Deck 
from hand import Hand
#starting chips
chips = 200

while True:
    print("You have this many chips", chips)
    bet = int(input("How much would you like to bet?"))
    while bet > chips or bet <= 0:
        print("Error: You are spending more than you own or betting less than 1")
        bet = int(input("How much would you like to bet?"))
    
    chips -= bet
    
    myDeck = Deck()
    #print(myDeck)
    #bet = int(input("How much do you want to bet "))
    #user's hand
    myHand = Hand(myDeck)
    print(myHand)
    print(myHand.value())
    while True:
        try:
            call = int(input("type 1 to hit or 0 to stay "))
            break
        except:
            print("Error: Expected a number but got letters")
        
    while call == 1:
        myHand.hit(myDeck)
        print(myHand)
        print(myHand.value())
        if min(myHand.value()) < 21:
            while True:
                try:
                    call = int(input("type 1 to hit or 0 to stay "))
                    break
                except:
                    print("Error: Expected a number but got letters")
        else:
            break
    if any(v == 21 for v in myHand.value()):
        print("blackjack")
    elif min(myHand.value()) < 21:
        print(min(myHand.value()))
    else:
        print("bust")
    #dealer's hand
    dealerHand = Hand(myDeck)
    while max(dealerHand.value()) < 16:
        dealerHand.hit(myDeck)

    print("here is the Dealers hand", dealerHand )
    print(dealerHand.value())

    if max(myHand.value()) > 21 or max(myHand.value()) <= max(dealerHand.value()):
        print("Dealer has won the round")
    else:
        print("You won this round")
        chips += 2 * bet
        
    r = input("Do you want to pay again type 1 or exist type 2 ")
    if r == "2":
        break
	
