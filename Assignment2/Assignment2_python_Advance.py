#Aug 21, 2019
#Michael Zabawa
#Python Assignment 2 for NCSU

from random import *
import copy
import csv

def printBoard(board):
    count = 0
    for i in range(0, 9, 3):
        count = count + 1
        print(board[i]+"|"+board[i+1]+"|"+board[i+2])
        if count < 3:
            print("-----------")

def makeMark(board, position, mark):
    if board[position] == "   ":
        board[position] = mark
        return(True)
    else:
        print("Choose a different position")
        return(False)
        
def computerMakeMark(board, position, mark):
    if board[position] == "   ":
        board[position] = mark
        return(True)

def checkWinner(board):
    if ((board[0] == board[3] == board[6]) and not board[6] == "   ") or ((board[1] == board[4] == board[7]) and not board[7]== "   ") or ((board[2] == board[5] == board[8])and not board[2] == "   "):
        return True
    elif ((board[0] == board[1] == board[2])and not board[0] == "   ") or ((board[3] == board[4] == board[5])and not board[3] == "   ") or ((board[6] == board[7] == board[8])and not board[6] == "   "):
        return True
    elif ((board[0] == board[4] == board[8])and not board[0] == "   ") or ((board[2] == board[4] == board[6])and not board[2] == "   "):
        return True
    else:
        return False

################################################################################
def humanMove(board, boardMark, player):
    playerInput = input("Choose a spot or (E)xit: ")
    if  str.upper(playerInput[0]) == 'E':
        exit()
    elif playerInput == 'A1':
        if makeMark(board, 0, boardMark):
            player = player + 1
    elif playerInput == 'A2':
        if makeMark(board, 3, boardMark):
            player = player + 1
    elif playerInput == 'A3':
        if makeMark(board, 6, boardMark):
            player = player + 1
    elif playerInput == 'B1':
        if makeMark(board, 1, boardMark):
            player = player + 1
    elif playerInput == 'B2':
        if makeMark(board, 4, boardMark):
            player = player + 1
    elif playerInput == 'B3':
        if makeMark(board, 7, boardMark):
            player = player + 1
    elif playerInput == 'C1':
        if makeMark(board, 2, boardMark):
            player = player + 1
    elif playerInput == 'C2':
        if makeMark(board, 5, boardMark):
            player = player + 1
    elif playerInput == 'C3':
        if makeMark(board, 8, boardMark):
            player = player + 1
    else:
        print("Use format Capital letter(A, B, C) followed by a number(1, 2, 3). example A1")
    return player

################################################################################
def randomComputerMove(board, player):
    position = randint(0,8)
    boardMark = "   "
    if player % 2 == 1:#gets Mark and sets score
        boardMark = " O "
    else:
        boardMark = " X "
    while not computerMakeMark(board, position, boardMark):
        position = randint(0,9)
    return player + 1

################################################################################
def makeGameData():
    tic_tac_board = [-1] * 9
    player = 0
    boardMark = -1
    winner = False
    games = [""]
    target = -1#assumes there is tie
    while((player < 9) and not winner):
        if player % 2 == 1:
            boardMark = 0
        else:
            boardMark = 1
        player = randomComputerMove(tic_tac_board, player)
        games.append(tic_tac_board)
        player = randomComputerMove(tic_tac_board, player)
        games.append(tic_tac_board)
        if player > 4:
            winner = checkWinner(tic_tac_board)
    if winner:
        target = player % 2 # 0 or 1
    else:
        target  = -1
    out = open("gameData.csv", "a")
    for game in games:
        out.write(game)
        out.write(target)
        out.write("\n")
    out.close()

makeGameData()
################################################################################
def computerMove(board, player):
    position = explore(score, player, board)
    makeMark(board, position, " O ")
    return player + 1

def explore(player, board):
    score = 0
    #Check for  a winner
    if checkWinner(board):
        if player % 2 == 1:#gets Mark and sets score
            score = 1
        else:
            score = -1
    move = -1
    score = -2
    if player % 2 == 1:#gets Mark and sets score
        boardMark = " O "
    else:
        boardMark = " X "
    printBoard(TestBoard)
    print(score)
    #if not a winner dig deeper
    for i in range(9):#Check eack position
        if board[i] == "   ":#Check if the position is already taken
            print(i)
            newBoard = copy.deepcopy(board)#sets new board
            makeMark(newBoard, i, boardMark)#mutates newBoard with new mark
            movescore = -explore(player + 1, newBoard)#digs deeper
            if movescore > score:
                score = movescore
                move = i
    return score

################################################################################
#testing for above functions 
TestBoard = ["   "]*9
score=[0]*9
printBoard(TestBoard)
test = explore(0, TestBoard)

################################################################################
#dont touch
def twoPlayerGame():
    tic_tac_board = ["   "] * 9
    player = 0
    playerInput = ''
    boardMark = ""
    winner = False
    while((player < 9) and not winner):
        print("\n")
        printBoard(tic_tac_board)
        if player % 2 == 1:
            boardMark = " O "
        else:
            boardMark = " X "
        player = humanMove(tic_tac_board, boardMark, player)
        if player > 4:
            winner = checkWinner(tic_tac_board)
    printBoard(tic_tac_board)
    if winner:
        print("Player", boardMark, "Wins The Game\n")
    else:
        print("Cats Game\n")

################################################################################

def onePlayerGame():
    tic_tac_board = ["   "] * 9
    player = 0
    playerInput = ''
    boardMark = ""
    winner = False
    while((player < 9) and not winner):
        print("\n")
        printBoard(tic_tac_board)
        if player % 2 == 1:
            boardMark = " O "
        else:
            boardMark = " X "
        player = humanMove(tic_tac_board, boardMark, player)
        player = computerMove(tic_tac_board, player)
        if player > 4:
            winner = checkWinner(tic_tac_board)
    printBoard(tic_tac_board)
    if winner:
        print("Player", boardMark, "Wins The Game\n")
    else:
        print("Cats Game\n")

################################################################################
#driving function
def main():
    print("\n \nWould you like to play\nTic-Tack_Toe?")
    play = input("Type (Y)es or (N)o:  ")
    play = str.upper(play[0])
    while(play == 'Y'):
        numPlayer = input("Type (O)ne or (T)wo players: ")
        if str.upper(numPlayer[0]) == 'T':
            twoPlayerGame()
        else:
            computerPlayer()
        print("\nWold you like to play again?")
        play = input("Type (Y)es or (N)o:  ")
        play = str.upper(play[0])

################################################################################
main()















