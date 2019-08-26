#Aug 21, 2019
#Michael Zabawa
#Python Assignment 2 for NCSU

from TicTacToeClasses import *
################################################################################
#driving function
def main():
    print("\n \nWould you like to play\nTic-Tack_Toe?")
    play = input("Type (Y)es or (N)o:  ")
    play = str.upper(play[0])
    while(play == 'Y'):
        numPlayer = input("Type (O)ne or (T)wo players:  ")
        if str.upper(numPlayer[0]) == 'T':
            game = TwoPlayerGame()
            game.playGame()
        elif str.upper(numPlayer[0]) == 'O':
            game = OnePlayerGame()
            game.playGame()
        else:
            print("Incorrect Entry \nEnter T or O")
        print("\nWold you like to play?")
        play = input("Type (Y)es or (N)o:  ")
        play = str.upper(play[0])

################################################################################
main()

for i in range(100):
    game = NoPlayerGame()
    game.playGame()
    game.printMoveList(True)

game.tic_tac_toe_board.printBoard()

7,3,5,2,0,8,1,4,6













