


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

boardKey = []

for key in theBoard:
    boardKey.append(key)

def printBoard(board):
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

def game():

    turn = 'X'


    count = 0

    for i in theBoard:
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')

            
        move = input()


        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('That space is taken!')
            continue

        if count >= 5:
            if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break

            elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break
            elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break
            elif theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break
            elif theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break
            elif theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break
            elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break
            elif theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] != ' ':
                printBoard(theBoard)
                print("Game Over! " + turn + " won!")
                break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        if count == 9:
            printBoard(theBoard)
            print("Game Over! It's a tie!")

    restart = input('Would you like to play again? (y/n)')
    if restart.lower() == 'y':
            for key in theBoard:
                theBoard[key] = ' '
            game()

if __name__ == '__main__':
    game()