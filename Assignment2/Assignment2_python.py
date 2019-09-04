#Aug 21, 2019
#Michael Zabawa
#Python Assignment 2 for NCSU

from TicTacToeClasses import *
################################################################################
#If you dont want the while loop and "user" inerface
#uncomment below and comment out the rest and it will just be one instance of the game
#sorry if I made it too complacted

#game = TwoPlayerGame()#Game for two human players
#game.playGame()

################################################################################
#driving function
def main():
    print("\n \nWould you like to play\nTic-Tack_Toe?")
    play = input("Type (Y)es or (N)o:  ")
    play = str.upper(play[0])
    while(play == 'Y'):
        numPlayer = input("Type (O)ne or (T)wo players:  ")
        if str.upper(numPlayer[0]) == 'T':
            game = TwoPlayerGame()#Game for two human players
            game.playGame()
        elif str.upper(numPlayer[0]) == 'O':
            game = OnePlayerGame()#game for human v Computer
            game.playGame()
        else:
            print("Incorrect Entry \nEnter T or O")
        print("\nWold you like to play?")
        play = input("Type (Y)es or (N)o:  ")
        play = str.upper(play[0])

################################################################################
main()#call main function

################################################################################










