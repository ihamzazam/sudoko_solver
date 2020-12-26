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
             print("- - - - - - - - - - - -")
        for j in range(len(bo[0])): # take the range of the first element as reference
            if j % 3 == 0 and j != 0: # prints borders after every 3 columns
                print(" | ", end="")
            if j == 8: # if its the last list then just print numbers w/o borders
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " " , end="")

                
def find_empty(board):
    for i in range(len(board)): #loop through rows
        for j in range(len(board[0])): #loop through column
            if board[i][j] == 0: #checking if the position is zero
                return(i, j) #return the empty (row,col)
    return None

def validity(board, num, pos):
    # row validation
    for i in range(len(board[0])): # iteration through the first list as reference
        if board[pos[0]][i] == num and pos[1] != i: # check the whole row excluding current pos
            return False

    # column validation
    for i in range(len(board)): # iteration through the 2D list
        if board[i][pos[0]] == num and pos[0] != i: # check the column excluding current pos
            return False

    # box validator
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3): # iteration through all three vertical boxes
        for j in range(box_x * 3, box_x * 3 + 3): # iteration through all three horizontal boxes
            if board[i][j] == num and (i, j) != pos: # check the box for same number excluding the pos
                return False
    return True

def solve(board): #use of backtrack algorithm
    
    find = find_empty(board) #check for empty strings  
    if not find:
        return True  #we have found the solution
    else:
        row, col = find
    for i in  range (1, 10): #loop through values 1 to 9
        if validity(board, i, (row, col)): #check if the values are valid in the spcific (row,col)
            board[row][col] = i #if the values are valid then they will be insert here
            if solve(board): #solving board by calling the function recursively
                return True
                bo[row][col]= 0  #condition when false, will rest the lop values and try new values
    return False
        
print_board(board)
solve(board)
print("_______________________")
print()
print_board(board)
