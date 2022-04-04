def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def mark (board, position, element):
    board[position] = element


elementUser = 'X'
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' '
           , 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' '
           , 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


for i  in range (1,10):
    print('select the position')
    positionUser = input()
    mark(theBoard, positionUser, elementUser)
    printBoard(theBoard)
    if elementUser == 'X':
        elementUser = 'O'
    else:
        elementUser = 'X'


