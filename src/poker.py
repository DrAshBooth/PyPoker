'''
Created on 31 Aug 2013

@author: Ash Booth
'''

class Card(object):
    def __init__(self, suit, rank, 
                 name,longName, dealt=False):
        self.suit = suit
        self.rank = suit
        self.name = name
        self.longName = longName
        self.dealt = dealt

class Player(object):
    def __init__(self):
        self.hand = None
        self.link = None
        self.firstLink = None
        
        self.numCards = None
        self.numSuit = None
        self.handStrength = None
        self.compCard = None
        
        self.thisBet = None
        self.bluffing = False
        self.folded = False
        self.busted = False
        
        self.allIn = False
        self.allInRound = None
        self.partialPot
        
        self.chips = None
        self.balance = None
        self.buyIns = None

        self.topUpGap = None

        self.constRand = None
        self.totalRaisesThisHand = None
        self.raisesThisHand = None
        self.preFlopRaise = None
        self.calledPreFlopRaise = None

#        struct windowStatsStruct flops;
#        struct windowStatsStruct showdowns;
#        struct windowStatsStruct raiseRate;

        self.strategyType = None
#        struct strategyStruct *strategy;
#        struct sparseNetStruct *sparseNet;

