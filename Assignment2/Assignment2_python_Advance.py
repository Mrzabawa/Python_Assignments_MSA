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

################################################################################
#Generate Game Data
for i in range(100):
    game = NoPlayerGame()
    game.playGame()
    game.printMoveList(True)
    
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
data = pd.read_csv("gameData.csv")
X = data.iloc[:, 0:9]
y = data.loc[:,'WINNER']
clf = MultinomialNB()
clf.fit(X, y)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print(clf.predict(X[2:3]))

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X, y)
clf.get_params()









