from copy import deepcopy

class Board(object):
    def invert(player):
        if player == "X":
            return "O"
        elif player == "O":
            return "X"
    def __init__(self, player, size = 3):
        self.board = [[None for i in range(size)] for i in range(size)]
        self.size = size
        self.player = player
    def parse(self, string):
        for i in range(self.size):
            for j in range(self.size):
                cur = string[i*self.size + j]
                self.board[i][j] = cur if cur == "X" or cur == "O" else None
    def play(self, position):
        assert self.board[position[0]][position[1]] == None
        self.board[position[0]][position[1]] = self.player
        self.player = Board.invert(self.player)
    def isWon(self):
        #TODO: Make this size dependent
        board = self.board
        for player in ("X", "O"):
            if board[0][0] == board[0][1] == board[0][2] == player\
                or board[1][0] == board[1][1] == board[1][2] == player\
                or board[2][0] == board[2][1] == board[2][2] == player:
                    return player
            elif board[0][0] == board[1][0] == board[2][0] == player\
                or board[0][1] == board[1][1] == board[2][1] == player\
                or board[0][2] == board[1][2] == board[2][2] == player:
                    return player
            elif board[0][0] == board[1][1] == board[2][2] == player\
                or board[2][0] == board[1][1] == board[0][2] == player:
                    return player
        return None
    def nextBoards(self):
        if self.isWon() != None:
            return []
        answer = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    newBoard = deepcopy(self)
                    newBoard.play((i, j))
                    answer.append(newBoard)
        return answer
    def value(self):
        if self.isWon() != None:
            return self.isWon()
        nextBoards = self.nextBoards()
        if nextBoards == []:
            return None
        nextBoardValues = map(Board.value, nextBoards)
        answer = Board.invert(self.player)
        for value in nextBoardValues:
            if value == self.player:
                answer = self.player
                break
            elif value == None:
                answer = None
        return answer
        # return "X" if the game is a winning position for X
        # return "O" if the game is a winning position for O
        # return None if the game is a draw
