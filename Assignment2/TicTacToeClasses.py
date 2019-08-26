from random import * #for random moves

################################################################################
#                           Board Class                                        #
################################################################################
class Tic_Tac_Toe_Board:
    def __init__(self):
        self.board = ["   "] * 9
    
    def printBoard(self):
        count = 0
        for i in range(0, 9, 3):
            count = count + 1
            print(self.board[i] + "|" + self.board[i+1] + "|" + self.board[i+2])
            if count < 3:
                print("-----------")
    
    def checkWinner(self):
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
class __Player__:
    def __init__(self):
        self.marker = "   "

################################################################################
class HumanPlayer(__Player__):
    def __init__(self, mark):
        self.marker = mark
    
    def makeMark(self, tic_tack_toe_board, position):
        if tic_tack_toe_board.board[position] == "   ":
            tic_tack_toe_board.board[position] = self.marker
            return(True)
        else:
            print("Choose a different position")
            return(False)
    
    def move(self, tic_tack_toe_board):
        madeMove = False
        position = -1
        while not madeMove:
            playerInput = input("Choose a spot or (E)xit: ")
            if  str.upper(playerInput[0]) == 'E':
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
            else:
                print("Use format Capital letter(A, B, C) followed by a number(1, 2, 3). example A1")
            if position >= 0 and self.makeMark(tic_tack_toe_board, position):
                madeMove = True
                break
        return position

################################################################################
class ComputerPlayer(__Player__):
    def __init__(self, mark):
        self.marker = mark
    
    def makeMark(self, tic_tack_toe_board, position):
        if tic_tack_toe_board.board[position] == "   ":
            tic_tack_toe_board.board[position] = self.marker
            return True
        else:
            return False
    
    def move(self, tic_tack_toe_board):
        position = randint(0,8)
        while not self.makeMark(tic_tack_toe_board, position):
            position = randint(0,8)
        return position

################################################################################
class SmartComputerPlayer(ComputerPlayer):
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
class Game():
    def __init__(self):
        self.tic_tac_toe_board = Tic_Tac_Toe_Board()
        self.winner = -1
        self.moveList = [-1]*9
        self.move = 0
    
    def updateMoveList(self, position):
        self.moveList[self.move] = position
    
    def printMoveList(self, toFile = False):
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
    
    def playGame(self):
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

class TwoPlayerGame(Game):
    def __init__(self):
        super().__init__()
        self.player1 = HumanPlayer(" X ")
        self.player2 = HumanPlayer(" O ")

class OnePlayerGame(Game):
    def __init__(self):
        super().__init__()
        self.player1 = HumanPlayer(" X ")
        self.player2 = ComputerPlayer(" O ")

class NoPlayerGame(Game):
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

################################################################################
#still working on this 
#still working  on this
################################################################################
# def makeGameData():
#     tic_tac_board = [-1] * 9
#     player = 0
#     boardMark = -1
#     winner = False
#     games = [""]
#     target = -1#assumes there is tie
#     while((player < 9) and not winner):
#         if player % 2 == 1:
#             boardMark = 0
#         else:
#             boardMark = 1
#         player = randomComputerMove(tic_tac_board, player)
#         games.append(tic_tac_board)
#         player = randomComputerMove(tic_tac_board, player)
#         games.append(tic_tac_board)
#         if player > 4:
#             winner = checkWinner(tic_tac_board)
#     if winner:
#         target = player % 2 # 0 or 1
#     else:
#         target  = -1
#     out = open("gameData.csv", "a")
#     for game in games:
#         out.write(game)
#         out.write(target)
#         out.write("\n")
#     out.close()
# 
# makeGameData()
# ################################################################################
# def computerMove(board, player):
#     position = explore(score, player, board)
#     makeMark(board, position, " O ")
#     return player + 1
# 
# def explore(player, board):
#     score = 0
#     #Check for  a winner
#     if checkWinner(board):
#         if player % 2 == 1:#gets Mark and sets score
#             score = 1
#         else:
#             score = -1
#     move = -1
#     score = -2
#     if player % 2 == 1:#gets Mark and sets score
#         boardMark = " O "
#     else:
#         boardMark = " X "
#     printBoard(TestBoard)
#     print(score)
#     #if not a winner dig deeper
#     for i in range(9):#Check eack position
#         if board[i] == "   ":#Check if the position is already taken
#             print(i)
#             newBoard = copy.deepcopy(board)#sets new board
#             makeMark(newBoard, i, boardMark)#mutates newBoard with new mark
#             movescore = -explore(player + 1, newBoard)#digs deeper
#             if movescore > score:
#                 score = movescore
#                 move = i
#     return score
# 
# 
# 
