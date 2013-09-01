'''
Created on 1 Sep 2013

@author: Ash Booth

'''

from globals import *

###############################################################################
######################## Basic Strategies from Jason ##########################
###############################################################################

# A listing of pre-set strategies for use as opponents in the
# evolution of poker players.  Commenced Sunday 18 June 2000, 14:39:43

N_A = 0

me = [0.05, 0.35,
      ['HIGH_CARD', 'PAIR', 'PAIR', 'PAIR'], 
      ['TWO', 'TWO', 'FIVE', 'ACE'],
      ['PAIR', 'PAIR', 'TWO_PAIR', 'TWO_PAIR'],
      ['TWO', 'JACK', 'THREE', 'THREE'],
      [2, 5, 10, 10], 
      [25, 25, 25, 35],
      [False, False, True, True],
      [N_A, True, False, False], 
      [N_A, True, True, N_A],
      [N_A, True, True, N_A], 
      0.0, 0, -1]

sirem = [0.2, 0.0, 
         ['HIGH_CARD', 'PAIR', 'PAIR', 'PAIR'],
         ['TWO', 'TWO', 'TEN', 'TEN'],
         ['PAIR', 'PAIR', 'TWO_PAIR', 'TWO_PAIR'],
         ['TEN', 'TEN', 'THREE', 'TEN'],
         [2, 5, 5, 5], 
         [20, 10, 25, 25],
         [False, False, False, True],
         [N_A, False, False, True], 
         [N_A, True, True, N_A],
         [N_A, True, True, N_A], 
         0.0, 0, -2]

bold = [0.15, 0.0, 
        ['HIGH_CARD', 'HIGH_CARD', 'PAIR', 'PAIR'],
        ['TWO', 'JACK', 'SEVEN', 'SEVEN'],
        ['PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND', 'THREE_OF_A_KIND'],
        ['FIVE', 'THREE', 'TWO', 'TWO'],
        [5, 10, 15, 15], 
        [40, 40, 60, 60],
        [False, True, True, True],
        [N_A, True, False, False], 
        [N_A, False, False, N_A],
        [N_A, False, True, N_A], 
        0.0, 0, -3]

boldLiar = [0.3, 0.5, 
            ['HIGH_CARD', 'HIGH_CARD', 'PAIR', 'PAIR'],
            ['TWO', 'JACK', 'SEVEN', 'SEVEN'],
            ['PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND', 'THREE_OF_A_KIND'],
            ['FIVE', 'THREE', 'TWO', 'TWO'],
            [5, 10, 15, 15], 
            [40, 40, 60, 60],
            [False, True, True, True],
            [N_A, False, False, False], 
            [N_A, True, True, N_A],
            [N_A, True, True, N_A], 
            0.0, 0, -4]

honesty = [0.0, 0.0, 
           ['HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD'],
           ['TWO', 'ACE', 'ACE', 'ACE'],
           ['HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD'],
           ['TWO', 'TWO', 'TWO', 'TWO'],
           [5, 5, 10, 20], 
           [5, 5, 10, 20],
           [False, False, False, False],
           [N_A, False, False, False], 
           [N_A, True, True, N_A],
           [N_A, True, True, N_A], 
           0.0, 0, -5 ]

braverHonesty = [0.0, 0.0, 
                 ['HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD'],
                 ['TWO', 'TEN', 'TEN', 'TEN'],
                 ['HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD'],
                 ['TWO', 'TWO', 'TWO', 'TWO'],
                 [5, 5, 10, 20], 
                 [5, 5, 10, 20],
                 [False, False, False, False],
                 [N_A, True, True, True], 
                 [N_A, False, False, N_A],
                 [N_A, False, False, N_A], 
                 0.0, 0, -6]

evolved1 = [0.2, 0.8,
            ['HIGH_CARD', 'HIGH_CARD', 'PAIR', 'PAIR'],
            ['SIX', 'JACK', 'JACK', 'JACK'],
            ['HIGH_CARD', 'PAIR', 'TWO_PAIR', 'HIGH_CARD'],
            ['EIGHT', 'JACK', 'JACK', 'QUEEN'],
            [10, 20, 20, 20],
            [55, 40, 30, 35],
            [False, False, True, False],
            [N_A, False, False, False], 
            [N_A, True, True, N_A],
            [N_A, True, False, N_A],
            0.0, 0, -7]

evolved2 = [0.3, 0.4,
            ['HIGH_CARD', 'HIGH_CARD', 'HIGH_CARD', 'TWO_PAIR'],
            ['ACE', 'ACE', 'ACE', 'JACK'],
            ['FLUSH', 'TWO_PAIR', 'THREE_OF_A_KIND', 'HIGH_CARD'],
            ['JACK', 'EIGHT', 'QUEEN', 'TWO'],
            [25, 25, 10, 30],
            [100, 100, 100, 300],
            [False, False, False, False],
            [N_A, False, False, False], 
            [N_A, True, True, N_A],
            [N_A, False, True, N_A],
            0.0, 0, -8]

piecemealStr = [0.05, 0.88,
                ['HIGH_CARD', 'PAIR', 'PAIR', 'PAIR'],
                ['TWO', 'TWO', 'FIVE', 'ACE'],
                ['PAIR', 'PAIR', 'TWO_PAIR', 'TWO_PAIR'],
                ['TEN', 'TEN', 'THREE', 'TEN'],
                [10, 20, 20, 20],
                [55, 40, 30, 35],
                [False, True, True, True],
                [N_A, False, False, False], 
                [N_A, True, True, N_A],
                [N_A, True, True, N_A], 
                0.0, 0, -9]


referencePlayer = [0.0, 0.98,
                   ['HIGH_CARD', 'PAIR', 'PAIR', 'PAIR'],
                   ['JACK', 'FIVE', 'FIVE', 'FIVE'],
                   ['PAIR', 'HIGH_CARD', 'HIGH_CARD', 'PAIR'],
                   ['FIVE', 'TWO', 'TWO', 'QUEEN'],
                   [15, 45, 50, 15],
                   [50, 50, 50, 50],
                   [True, False, True, True],
                   [N_A, False, False, False], 
                   [N_A, True, False, N_A],
                   [N_A, True, False, N_A],
                   0.0, 0, -10]