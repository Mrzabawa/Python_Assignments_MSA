#Aug 21, 2019
#Michael Zabawa
#Python Assignment 2 for NCSU

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
#driving function
def main():
    print("\n \nWould you like to play\nTic-Tack_Toe?")
    play = input("Type (Y)es or (N)o:  ")
    play = str.upper(play[0])
    while(play == 'Y'):
        twoPlayerGame()
        print("\nWold you like to play again?")
        play = input("Type (Y)es or (N)o:  ")
        play = str.upper(play[0])

################################################################################
main()















