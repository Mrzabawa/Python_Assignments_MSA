#Aug 21, 2019
#Michael Zabawa
#Python Assignment 2 for NCSU
#classes for TicTacToe game
from random import * #for random moves

################################################################################
#                           Board Class                                        #
################################################################################
class Tic_Tac_Toe_Board:#defines the board Class for a tic_tac_toe game
    def __init__(self):
        self.board = ["   "] * 9
    
    def printBoard(self):#method to print board
        count = 0
        for i in range(0, 9, 3):
            count = count + 1
            print(self.board[i] + "|" + self.board[i+1] + "|" + self.board[i+2])
            if count < 3:
                print("-----------")
    
    def checkWinner(self):# Checks the borad to see if there is a winner
        #checks each case to see if there is a winner
        if ((self.board[0] == self.board[3] == self.board[6]) and not self.board[6] == "   ") or ((self.board[1] == self.board[4] == self.board[7]) and not self.board[7]== "   ") or ((self.board[2] == self.board[5] == self.board[8])and not self.board[2] == "   "):
            return True
        elif ((self.board[0] == self.board[1] == self.board[2])and not self.board[0] == "   ") or ((self.board[3] == self.board[4] == self.board[5])and not self.board[3] == "   ") or ((self.board[6] == self.board[7] == self.board[8])and not self.board[6] == "   "):
            return True
        elif ((self.board[0] == self.board[4] == self.board[8])and not self.board[0] == "   ") or ((self.board[2] == self.board[4] == self.board[6])and not self.board[2] == "   "):
            return True
        else:
            return False

################################################################################
#                           Player Classes                                     #
################################################################################
class Player:#defines a base player so there can be different types of players <- not sure I needed this abstract class but I made it
    def __init__(self):
        self.marker = "   "
    
    def makeMark(self, tic_tack_toe_board, position):
        if tic_tack_toe_board.board[position] == "   ":
            tic_tack_toe_board.board[position] = self.marker
            return True
        else:
            return False

#################################################################
class HumanPlayer(Player):#derived class of player that takes input from the consel
    def __init__(self, mark):
        self.marker = mark
    
    def move(self, tic_tack_toe_board):#obtains players move
        madeMove = False #assumes player has not moved yet
        position = -1 #sentenial position
        while not madeMove:#assumes that the player has not moved yet
            playerInput = input("Choose a spot or (E)xit: ")
            if  str.upper(playerInput[0]) == 'E':#if player wants to quit mid game
                exit()
            elif playerInput == 'A1':
                position = 0
            elif playerInput == 'A2':
                position = 3
            elif playerInput == 'A3':
                position = 6
            elif playerInput == 'B1':
                position = 1
            elif playerInput == 'B2':
                position = 4
            elif playerInput == 'B3':
                position = 7
            elif playerInput == 'C1':
                position = 2
            elif playerInput == 'C2':
                position = 5
            elif playerInput == 'C3':
                position = 8
            else:#did not enter a correct format
                print("Use format Capital letter(A, B, C) followed by a number(1, 2, 3). example A1")
            if position >= 0 and self.makeMark(tic_tack_toe_board, position):#checks if a successful move was chossen
                madeMove = True
                break
            else:
                print("Choose a different position")
        return position

#################################################################
class ComputerPlayer(Player):#dumb player that just chooses random position
    def __init__(self, mark):
        self.marker = mark
    
    def move(self, tic_tack_toe_board):
        position = randint(0,8)
        while not self.makeMark(tic_tack_toe_board, position):
            position = randint(0,8)
        return position

#################################################################
class SmartComputerPlayer(ComputerPlayer):#did not have time to complete this
    #intent was to create a smart player to play aginst 
    #either by deterministic approch using recursion or renforcement learning or some other model
    def __init__(self, mark):
        self.marker = mark
    #fit model from training data
    
    #make moves based on model
    def move(self, tic_tack_toe_board):
        position = -1
        while not self.makeMark(tic_tack_toe_board, position):
            position = -1
        return position

################################################################################
#                           Game Classes                                       #
################################################################################
class Game():#game class that ties it all together
    def __init__(self):
        self.tic_tac_toe_board = Tic_Tac_Toe_Board()#a game has a board
        self.winner = -1#has a winner
        self.moveList = [-1]*9#maintains moves
        self.move = 0#tracker to alternate players
    
    def updateMoveList(self, position):#method to maintain the moves in order. Used to gather data
        self.moveList[self.move] = position
    
    def printMoveList(self, toFile = False):#used to collect game data
        if toFile:
            out = open("gameData.csv", "a")
            for i in range(9):
                out.write(str(self.moveList[i]))
                out.write(",")
            out.write(str(self.winner))
            out.write("\n")
            out.close()
        else:
            print(self.moveList)
    
    def playGame(self):#abstract method for playing a tic-tac-toe game
        winnerFlag = False 
        while( ( self.move < 9 ) and not winnerFlag):#go until there is a winner or board is full which ever is first
            self.tic_tac_toe_board.printBoard()# display  move
            print("\n")
            if self.move % 2 == 0:
                choosenPosition = self.player1.move(self.tic_tac_toe_board)
                message = "Player X Wins The Game"
            else:
                choosenPosition = self.player2.move(self.tic_tac_toe_board)
                message = "Player O Wins The Game"
            self.updateMoveList(choosenPosition)
            self.move += 1 #next move
            if(self.tic_tac_toe_board.checkWinner()): #check for winner
                winnerFlag = True
                self.winner = self.move % 2
        if not (self.tic_tac_toe_board.checkWinner()):
            self.winner = -1
            message = "Tie Game"
        self.tic_tac_toe_board.printBoard()
        print(message)

#################################################################
class TwoPlayerGame(Game):#derived class for two human players
    def __init__(self):
        super().__init__()
        self.player1 = HumanPlayer(" X ")
        self.player2 = HumanPlayer(" O ")
#################################################################
class OnePlayerGame(Game):#derived class of human v computer. intended to have this be smart computer
    def __init__(self):
        super().__init__()
        self.player1 = HumanPlayer(" X ")
        self.player2 = ComputerPlayer(" O ")
#################################################################
class NoPlayerGame(Game):#Used to generate data for training a model to make it smart
    def __init__(self):
        super().__init__()
        self.player1 = ComputerPlayer(" X ")
        self.player2 = ComputerPlayer(" O ")
    
    def playGame(self):
        winnerFlag = False 
        while( ( self.move < 9 ) and not winnerFlag):#go until there is a winner or board is full which ever is first
            if self.move % 2 == 0:
                choosenPosition = self.player1.move(self.tic_tac_toe_board)
            else:
                choosenPosition = self.player2.move(self.tic_tac_toe_board)
            self.updateMoveList(choosenPosition)
            self.move += 1 #next move
            if(self.tic_tac_toe_board.checkWinner()): #check for winner
                winnerFlag = True
                self.winner = self.move % 2
        if not (self.tic_tac_toe_board.checkWinner()):
            self.winner = -1
