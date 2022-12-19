# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import numpy as np
import random


class Oneplayergame():
    def __init__(self):
        self.winner = None
        self.currentplayer = random.choice(['X', 'O'])
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]


    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', '0', or None."""
        if self.checkDig(self.board) or self.checkRow(self.board) or self.checkHorizon(self.board) :
            print(f"The dig winner is {self.winner}")
            print(self.board)   
        return self.winner


    def other_player(self):
        """switch the global variable currentplayer """
        if self.currentplayer == "X":
            self.currentplayer = "O"
        elif self.currentplayer == "O":
            self.currentplayer = "X"
        else:
            print("player not X or O!")


    #take player input
    def playerInput(self,board):
        print(self.currentplayer, "Enter a number 0-8: ")
        position = int(input()) #Flask沒有辦法跑，從form這邊跑過來
        if position >= 0 and position <= 8:
            currentSpot = board[position // 3][position - (position // 3) * 3]
            if currentSpot != None:
                print("This spot is aleady taken")
            else: board[position // 3][position - (position // 3) * 3] = self.currentplayer
        else:
            print("only input 0-8")
    
    def random_input(self,board):
        self.board = board
        X = random.randint(low=1, high=10)
        O = random.randint(low=1, high=10)
        while self.board[X][O] != None:
            X = random.randint(low=1, high=10)
            O = random.randint(low=1, high=10)
        self.board[X][O] = self.currentplayer
        return self.board

    #check for win or tie

    def checkRow(self,board):
        global winner
        for i in range(3):
            if board[0][i] == None:
                return False
            player = board[0][i]
            if board[1][i] == player and board[2][i] == player:
                winner = player
                return True
        return False

        
    def checkHorizon(self,board): 
        global winner
        for i in range(3):
            if board[i][0] == None:
                return False
            player = board[i][0] 
            if board[i][1] == player and board[i][2] == player:
                winner = player
                return True
        return False 

    def checkDig(self,board):
        global winner
        if board[1][1] == None:
            return False
        if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
            winner = board[0][0]
            return True
        if board[0][2] == board[1][1] == board[2][0]:
            winner = board[0][2]
            return True
        return False
    
    #Check for win or tie again
    def run(self):
        winner = None
        while winner == None:
            self.printBoard()
            self.playerInput(self.board)
            winner = self.get_winner()
            self.other_player()

    #Printing the game board 
    def printBoard(self):
        print(str(self.board[0]) + "\n" + str(self.board[1]) + "\n" + str(self.board[2]))

