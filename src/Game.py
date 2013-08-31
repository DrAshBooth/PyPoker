'''
Created on 31 Aug 2013

@author: Ash
'''

from globals import *
from poker import *

class Game(object):

    def __init__(self):
        self.deck = []
        self.numPlayers = 10
        self.handsToPlay = 30
        self.numStockPlayers = 0
        self.pName = None
        self.longestName = 0
        self.players = []
        
    def genertePlayers(self):
        pass
    
    def assignDeck(self):
        '''
        Has to be run once at the beginning of the program, to initialize the
        cards in the deck, and to assign the canonical table seat ordering.
        '''
        for i in range(RANKS['TWO'], RANKS['ACE']+1):
            for j in range(SUITS['HEARTS'], SUITS['SPADES']+1):
                self.deck.append(Card(i,j,
                                      [RANKS[i],SUITS[j],'\0'], 
                                      "{} of {}".format(RANKS[i],SUITS[j])))
    
    def getOptions(self):
        self.hardline()
        self.pName = raw_input("\nYour name, please? ")
        if len(self.pName) > self.longestName: 
            self.longestName = len(self.pName)
        
        self.handsToPlay = raw_input("\nHow many hands would you like to play, {}?".format(self.pName))
        
        self.numStockPlayers = raw_input("\nHow many stock players at the table?")
        
        if self.numStockPlayers > self.numPlayers-1:
            print "You can only have up to {} stock players.\n".format(self.numPlayers)
            self.numStockPlayers = self.numPlayers-1
            
        if self.numStockPlayers < 0:
            print ""
  
        if (self.numStockPlayers < 0):
            print "You can't have less than zero stock players.\n"
            self.numStockPlayers = 0

        
    def play(self):
        self.genertePlayers()
        self.assignDeck()
        self.getOptions()
        # assignPlayerStrategy next
        