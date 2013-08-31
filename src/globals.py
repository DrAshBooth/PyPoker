'''
Created on 31 Aug 2013

@author: Ash Booth
'''

class TwoWayDict(dict):
    def __len__(self):
        return dict.__len__(self) / 2

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

def newLine(): 
    print "\n"
def hardLine(): 
    print "=================================================================\n"
    

############################################################################
############################ Global Variables ##############################
############################################################################
        
RANKS = TwoWayDict()
RANKS['TWO'] = 2
RANKS['THREE'] = 3
RANKS['FOUR'] = 4
RANKS['FIVE'] = 5
RANKS['SIX'] = 6
RANKS['SEVEN'] = 7
RANKS['EIGHT'] = 8
RANKS['NINE'] = 9
RANKS['TEN'] = 10
RANKS['JACK'] = 11
RANKS['QUEEN'] = 12
RANKS['KING'] = 13
RANKS['ACE'] = 14

SUITS = TwoWayDict()
SUITS['HEARTS'] = 1
SUITS['DIAMONDS'] = 2
SUITS['CLUBS'] = 3
SUITS['SPADES'] = 4



#struct playerStruct player[NUM_PLAYERS];
#struct playerStruct community;
#
#struct cardStruct card[DECK_SIZE];
#struct cardStruct *order[DECK_SIZE];
#int deckPointer = 0;
#int potsWonByHuman = 0;
#int playersStillAtTable = NUM_PLAYERS;
#
#long int rakeTotal = 0;
#
#int button = NUM_PLAYERS-1;
#int currentPlayer;
#int potSize = 0;
#int betSize = 0;
#int numFolders = 0;
#int numChancesToBet = 0;
#int smallBlindMarker, bigBlindMarker;
#
#int focalHand;
#struct pfHandStruct pfHand[169];
#
#struct windowStatsStruct playersPerFlop;
#struct windowStatsStruct showdownRate;
#struct windowStatsStruct avgPotSize;
#
#
#char sName[] = { 'h', 'c', 'd', 's' };
#char vName[] = { '?', '?', '2', '3', '4', '5', '6', '7', '8', 
#         '9', 'T', 'J', 'Q', 'K', 'A' };
#
#char *sNameL[] = { "hearts", "clubs", "diamonds", "spades" };
#char *vNameL[] = { "?", "?", "Two", "Three", "Four", "Five",
#            "Six", "Seven", "Eight", "Nine", "Ten", 
#            "Jack", "Queen", "King", "Ace" };
#
#char *pName[] = { "Anne", "Bob", "Carol", "Dave",   
#          "Emma", "Frank", "Gina", "Harry",
#                  "Irina", "John", "Karen", "Liam" };
#
#int longestName = 6;
#
#char *stgName[] = { "Pre-flop", "Flop", "Turn", "River" };
#
#char *strName[] = { "High card", "a Pair", "Two pair", "Three of a kind",
#            "a Straight", "a Flush", "a Full house", 
#            "Four of a kind", "a Straight flush" };
#
#char *outputName[] = { "Fold", "Call", "Raise" };
#
#
#char *preInputName[] = { "P_PAIR_F", "P_SUITED_F", "P_CONNECTED_F", 
#             "P_1GAP_F", "P_2GAP_F", "P_3GAP_PLUS_F", 
#             "P_BOTHBIG_F", "P_ACE_F", "P_KING_F", "P_PAIR",
#             "P_AS", "P_KS", "P_QS", "P_JS", "P_TS", "P_9S", 
#             "P_8S", "P_7S", "P_6S", "P_5S", "P_4S", "P_3S",
#             "P_A", "P_K", "P_Q", "P_J", "P_T", "P_9", "P_8", 
#             "P_7", "P_6", "P_5", "P_4", "P_3",
#             "P_NUM_AT_TABLE", "P_8PLUS_TABLE_F", 
#             "P_5THRU7_TABLE_F", 
#             "P_3THRU4_TABLE_F", "P_HEADS_UP_TABLE_F",
#             "P_NUM_IN_HAND", "P_HEADS_UP_F", "P_NUM_TO_ACT", 
#             "P_POSITION", "P_SB_F", "P_BB_F", 
#             "P_BET2U_BBL_UNITS", "P_BET2U_STACK_PCT", 
#             "P_POT_SIZE_2BBL_UNITS", "P_POT_ODDS", 
#             "P_RAND_CONST", "P_RAND_FLUX",
#             "P_OPP_FLOPS", "P_OPP_SHOWDOWNS", "P_OPP_RAISE_RATE",
#             "P_OPP_P_RAISE_F", "P_OPP_P_CALLED_RAISE_F",
#             "P_OPP_RAISES_THIS_ROUND", "P_OPP_RAISES_TOTAL",
#             "P_OPP_POSITION", "P_OPP_SB_F", "P_OPP_BB_F",
#             "P_OPP_BEFORE_F", "P_OPP_AFTER_F",
#             "P_OPP_STACK_2BBL_UNITS", "P_OPP_STACK_STACK_PCT",
#             "P_PLAYERS_PER_FLOP", "P_SHOWDOWN_RATE", 
#             "P_AVG_POT_2BBL_UNITS", "P_BIAS" };
#
#char *postInputName[] = { "F_FLOP_F", "F_TURN_F", "F_RIVER_F", 
#              "F_HAND_STRENGTH", "F_HC_F", "F_HC", 
#              "F_HC_NUM_OVERCARDS", "F_HC_HOLE_CARD_STRENGTH",
#              "F_PAIR_F", "F_PAIR", "F_PAIR_TOP_F",
#              "F_PAIR_2ND_F", "F_PAIR_WORSE_F",
#              "F_PAIR_POCKET_F", "F_PAIR_BOARD_F",
#              "F_PAIR_KICKER", "F_PAIR_OVERCARD_KICKER_F",
#              "F_2PR_F", "F_2PR", "F_2PR_KICKER",
#              "F_2PR_HI_TOP_F", "F_2PR_HI_2ND_F",
#              "F_2PR_HI_WORSE_F", "F_2PR_HI_POCKET_F", 
#              "F_2PR_LO_TOP_F", "F_2PR_LO_2ND_F", 
#              "F_2PR_LO_WORSE_F", "F_2PR_LO_POCKET_F",
#              "F_TRIPS_F", "F_TRIPS", "F_TRIPS_KICKER",
#              "F_TRIPS_SET_F", "F_TRIPS_BOARD_F", 
#              "F_TRIPS_TOP_F", "F_TRIPS_2ND_F", 
#              "F_TRIPS_WORSE_F",
#              "F_STRAIGHT_F", "F_STRAIGHT", 
#              "F_STRAIGHT_BOARD_F", "F_STRAIGHT_1HOLE_F",
#              "F_STRAIGHT_2HOLE_F", "F_STRAIGHT_NUM_BETTER_POSS", 
#              "F_FLUSH_F", "F_FLUSH",  "F_FLUSH_BOARD_F", 
#              "F_FLUSH_1HOLE_F", "F_FLUSH_2HOLE_F",
#              "F_FLUSH_NUM_BETTER_POSS", 
#              "F_BOAT_F", "F_BOAT", 
#              "F_BOAT_BOARD", "F_BOAT_1HOLE_F",
#              "F_BOAT_2HOLE_F", "F_BOAT_BETTER_POSS_F",
#              "F_QUADS_F", "F_QUADS", "F_QUADS_BOARD_F",
#              "F_SFLUSH_F", "F_SFLUSH",
#              "F_SFLUSH_BOARD_F",
#              "F_PAIRED_BOARD_F", "F_2PAIRED_BOARD_F",
#              "F_TRIP_BOARD_F", "F_2FLUSH_BOARD_F",
#              "F_3FLUSH_BOARD_F", "F_4FLUSH_BOARD_F",
#              "F_2CARD_POSS_STRAIGHT_F",
#              "F_1CARD_POSS_STRAIGHT_F",
#              "F_BACKDOOR_FLUSH_F", "F_BACKDOOR_STRAIGHT_F",
#              "F_FLUSH_DRAW_F", "F_OPENENDED_DRAW_F", 
#              "F_GUTSHOT_DRAW_F", 
#              "F_NUM_AT_TABLE", "F_8PLUS_TABLE_F", 
#              "F_5THRU7_TABLE_F", "F_3THRU4_TABLE_F",
#              "F_HEADS_UP_TABLE_F", "F_NUM_IN_HAND", 
#              "F_HEADS_UP_F", "F_NUM_TO_ACT", 
#              "F_POSITION", "F_SB_F", "F_BB_F", 
#              "F_BET2U_BBL_UNITS", "F_BET2U_BETS", 
#              "F_BET2U_STACK_PCT", "F_POT_SIZE_2BBL_UNITS", 
#              "F_POT_ODDS", "F_RAND_CONST", "F_RAND_FLUX",
#              "F_OPP_FLOPS", "F_OPP_SHOWDOWNS", 
#              "F_OPP_RAISE_RATE", "F_OPP_P_RAISE_F", 
#              "F_OPP_P_CALLED_RAISE_F", "F_OPP_RAISES_THIS_ROUND",
#              "F_OPP_RAISES_TOTAL",
#              "F_OPP_POSITION", "F_OPP_SB_F", "F_OPP_BB_F",
#              "F_OPP_BEFORE_F", "F_OPP_AFTER_F",
#              "F_OPP_STACK_2BBL_UNITS", "F_OPP_STACK_STACK_PCT",
#              "F_PLAYERS_PER_FLOP", "F_SHOWDOWN_RATE", 
#              "F_AVG_POT_2BBL_UNITS", "F_BIAS" };
#
#char *pfHandName[] = { "AA ", "KK ", "QQ ", "JJ ", "TT ", "99 ", "88 ",
#               "77 ", "66 ", "55 ", "44 ", "33 ", "22 ",
#               "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", 
#               "A6s", "A5s", "A4s", "A3s", "A2s",
#               "KQs", "KJs", "KTs", "K9s", "K8s", "K7s", 
#               "K6s", "K5s", "K4s", "K3s", "K2s",
#               "QJs", "QTs", "Q9s", "Q8s", "Q7s", 
#               "Q6s", "Q5s", "Q4s", "Q3s", "Q2s",
#               "JTs", "J9s", "J8s", "J7s", "J6s", 
#               "J5s", "J4s", "J3s", "J2s",
#               "T9s", "T8s", "T7s", "T6s", 
#               "T5s", "T4s", "T3s", "T2s",
#               "98s", "97s", "96s", 
#               "95s", "94s", "93s", "92s",
#               "87s", "86s", "85s", "84s", "83s", "82s",
#               "76s", "75s", "74s", "73s", "72s",
#               "65s", "64s", "63s", "62s",
#               "54s", "53s", "52s",
#               "43s", "42s",
#               "32s",
#               "AKo", "AQo", "AJo", "ATo", "A9o", "A8o", "A7o", 
#               "A6o", "A5o", "A4o", "A3o", "A2o",
#               "KQo", "KJo", "KTo", "K9o", "K8o", "K7o", 
#               "K6o", "K5o", "K4o", "K3o", "K2o",
#               "QJo", "QTo", "Q9o", "Q8o", "Q7o", 
#               "Q6o", "Q5o", "Q4o", "Q3o", "Q2o",
#               "JTo", "J9o", "J8o", "J7o", "J6o", 
#               "J5o", "J4o", "J3o", "J2o",
#               "T9o", "T8o", "T7o", "T6o", 
#               "T5o", "T4o", "T3o", "T2o",
#               "98o", "97o", "96o", 
#               "95o", "94o", "93o", "92o",
#               "87o", "86o", "85o", "84o", "83o", "82o",
#               "76o", "75o", "74o", "73o", "72o",
#               "65o", "64o", "63o", "62o",
#               "54o", "53o", "52o",
#               "43o", "42o",
#               "32o" };
#
#
#               
#
#                       
#
#int tableOrder[NUM_PLAYERS];
#int potContribution[NUM_PLAYERS];
#int matrix[NUM_PLAYERS][NUM_PLAYERS];
#int xmlShowDownOutput;