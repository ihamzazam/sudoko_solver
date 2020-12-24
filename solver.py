board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(bo):
    for i in range(len(bo)): # iteration through the 2D list
        if i % 3 == 0 and i != 0: # prints lines after every 3 rows
            print("- - - - - - - - - - - - -")
        for j in range(len(bo[0])): # take the range of the first element as reference
            if j % 3 == 0 and j != 0: # prints borders after every 3 columns
                print(" | ", end="")
            if j == 8: # if its the last list then just print numbers w/o borders
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " " , end="")


print_board(board)