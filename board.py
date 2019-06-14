from random import randint
import sys

sys.setrecursionlimit(1000)

SIZE = 13

PLAYER = -1
BOT = 1
NO_ONE = 0

class Board:
    board = [[NO_ONE] * SIZE for i in range(SIZE)]
    visited = [[NO_ONE] * SIZE for j in range(SIZE)]
    turn = 1

    def printboard(self):
        num = 0
        for row in self.board:
            print(str(num) + " " +  " "* num ,  end="")
            num+=1
            for cell in row:
                if cell == NO_ONE:
                    print(".", end=" ")
                if cell == BOT:
                    print("O", end=" ")
                if cell == PLAYER:
                    print("x", end=" ")

            print()

    def play(self, x,y):
        if self.board[y][x] != NO_ONE:
            print("Invalid Move")
            return False
        else:
            self.board[y][x] = self.turn
            self.turn = -self.turn
            return True

    def winner(self):
        self.visited = [[NO_ONE] * SIZE for j in range(SIZE)]
        for i in range(0, SIZE):
            if(self.board[i][SIZE-1] == BOT and self.visited[i][SIZE-1] == False):
                if(self.floodfill(SIZE-1, i, BOT)):
                    return (True, BOT)
        for i in range(0, SIZE):
            if(self.board[SIZE-1][i] == PLAYER and self.visited[SIZE-1][i] == False):
                if(self.floodfill(i,SIZE-1, PLAYER)):
                    return (True, PLAYER)
        all = True
        for y in range(SIZE):
            for x in range(SIZE):
                if self.board[y][x] == NO_ONE:
                    all = False
        if not all:
            return (False, NO_ONE)
        return (True, NO_ONE)

    # x,y
    # x-1, y
    # x+1, y
    # x, y+1
    # x-1, y+1
    # x+1, y-1
    # x, y-1
    def floodfill(self,x,y,player):
        if(x < 0 or y < 0 or y == SIZE or x == SIZE):
            return False
        if (self.board[y][x] != player):
            return False
        if(self.visited[y][x] == True):
            return False
        if(x == 0 and player == BOT):
            return True
        if(y == 0 and player == PLAYER):
            return True
        self.visited[y][x] = True

        moves = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (-1, 1),
            (1, -1),
            (0, -1),
        ]
        for x_off,y_off in moves:
            if(self.floodfill(x+x_off, y+y_off,player)):
                return True

board = Board()
board.printboard()
while not board.winner()[0]:
    x = randint(0,SIZE-1)
    y = randint(0, SIZE - 1)
    print(x,y)
    while not board.play(x,y):
        x = randint(0, SIZE - 1)
        y = randint(0, SIZE - 1)
        board.printboard()
    print(board.winner())
    x = int(input("X?"))
    y = int(input("Y?"))
    board.play(x,y)
    board.printboard()
print(board.winner())