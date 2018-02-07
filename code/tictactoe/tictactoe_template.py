# use this function to copy things when needed
from copy import deepcopy

class Board(object):
    def __init__(self, player, conf, size = 3):
        # player is either "X" or "O" denoting the current player
        # conf is the current configuration of the board. For example, "XXOO--X--" stands for [['X', 'X', 'O'], ['O', None, None], ['X', None, None]]
        self.board = [[None for i in range(size)] for i in range(size)]
        self.size = size
        self.player = player
        #fill in here to implement that the current value of self.board is as indicated by conf
    def __str__(self):
        # this method is invoked when print(...) is called on the object
        # should return the configuration in the string form
        # For example, [['X', 'X', 'O'], ['O', None, None], ['X', None, None]] should return "XXOO--X--"
        return ...
    def play(self, position):
        # position is a pair (i, j) denoting the ith row and jth column
        # first check that the indicated position is empty
        assert ...
        # if so, make the current player make a move here
        # and then, flip the current player
    def isWon(self):
        # if X has already won in the current state of the board, return X
        # if O has already won in the current state of the board, return O
        # if neither has won, return None
        return ...
    def nextBoards(self):
        # if the current position is already won by somebody, return []
        # otherwise, return a list of boards, which are the possible game configurations that are reachable in one step from here
        # to do this, for every box that is not marked, make a new copy of the board (using deepcopy),
        # and use the play method to mark that position in the board (and flip the player), and append it to a list,
        # which you'd return at the end of the computation
        return ...
    def value(self):
        # return 'X' if 'X' can force a win at the current state of the game
        # return 'O' if 'O' can force a win at the current state of the game
        # return None if the current state of the game is a draw in optimal play
        return ...
