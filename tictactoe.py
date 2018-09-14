#First Small Project - Tic-Tac-Toe
board = [['X','O','X'],['O','O','X'],['X','O','X']] #playable squares, will be filled throuoght the game
#board is filled for the purpose of testing table printer

def printTable(matrix):
    print()
    bar = ('===================')
    row = 0

    for i in range(0,6):
        if i % 2 == 0:
            print (bar)
        else:
            for j in range(3):
                    print ('|',end ='  %s  ' % board[row][j])

            print('|') #prints the final element of the line and goes to the next one

            row += 1
    print(bar)
#def game2players():
#def game1player():


choice = int(input("***Welcome to Tic-Tac-Toe***\n\nType 1 if you want to play!"))
while (choice == 1):
    #game() planned system
    choice = int(input("***Thank you for playing***\n\nType 1 if you want to play again!"))

printTable(board)
