
'''This Program is Created for DM Assignment
'''


import numpy as np 
# Skeletal Sudoku Matrix
S = np.zeros((9,9), dtype=np.int32)
#print(S)
#=====================================================
# To check if the entered sudoku problem is correct

def check_sudoku(A): 
  for x in range(9):
    for y in range(9):
       if A[x][y] != 0 and A[x][y] != 1 and A[x][y] != 2 and A[x][y] != 3 and A[x][y] != 4 and A[x][y] != 5 and A[x][y] != 6 and A[x][y] != 7 and A[x][y] != 8 and A[x][y] != 9:
         return False
       # To check if the entered number fits in its row
       if A[x][y]!=0:
        for i in range(9):
         if i != y:
           if A[x][i] == A[x][y]:
            return False
            break
       # To check if the entered number fits in its column
        for j in range(9):
         if j != x:
          if A[j][y] == A[x][y]:
            return False
            break
       # To check if the entered number fits in its 3*3 box
        x_leading = (x//3)*3
        y_leading = (y//3)*3
        for a in range(3):
          for b in range(3):
           if (x_leading + a) != x or (y_leading + b) != y:
            if A[x_leading + a][y_leading + b] == A[x][y]:
              return False
              break
  return True

#=====================================================
# Taking the puzzle from the user

def enter_sudoku(S):
  for i in range(9):
      S[i][0], S[i][1], S[i][2], S[i][3], S[i][4], S[i][5], S[i][6], S[i][7], S[i][8]= map(int, input().split())


#=====================================================
# Checking if the Entered puzzle is valid

def validate_sudoku(A):
 if check_sudoku(A)== True:
   print("\nThe Sudoku Puzzle You Entered is:")
   print(A)
 else:
   print("The Sudoku was invalid. Please follow the instructions to Enter the Sudoku again:")
   enter_sudoku(A)
   validate_sudoku(A)

#=====================================================
# DRIVER CODE TO TAKE SUDOKU PUZZLE

print("PLEASE INPUT THE SUDOKU PROBLEM WITH THE GIVEN INSTRUCTIONS! \n"
       "1. Seperate each element in a row by spacing, once a row has nine elements PRESS ENTER to switch to the next row. 
       "\n 2. Enter Zero in place of empty cell.\n"
       "3. Please mind the general sudoku rules.\n")

enter_sudoku(S)
validate_sudoku(S)

#=====================================================
# Function to check if a number n fits in the Sudoku at position S[x][y]

def select_number(A, x, y, n):

    # To check if a number n fits in its row
    for i in range(9):
        if A[x][i] == n:
            return False
    # To check if a number n fits in its column
    for j in range(9):
        if A[j][y] == n:
            return False
    #To check if a number n fits in its 3*3 box
    x_leading = (x//3) * 3
    y_leading = (y//3) * 3
    for a in range(3):
        for b in range(3):
            if A[x_leading + a][y_leading + b] == n:
              return False

    return True

# Test code
#print(select_number(S, 8, 7, 1))


#=====================================================
# Here we solve the sudoku and find all possible solutions
# We are using Recursion and Backtracking to solve the puzzle

def solve_sudoku(A):
     for i in range(9):
        for j in range(9):
            if A[i][j] == 0:
                #loop from 1 to 9 for n and checks if it fits in that certain place
                for n in range(1, 10): 
                    if select_number(A, i, j, n):
                        A[i][j]= n
                        #Recurssion to Solve for the following elements
                        solve_sudoku(A) 
                        # If algorithm stops at any point, backtracks the code and takes the next value of n for that step in recurssion.
                        A[i][j] = 0     
                return 
     
     #When no element is left equal to zero, the first solution will be printed
     #then the process will backtrack to the previous element and loop through the remaining values
     #if no new solution, then the process will follow to element before that one
     #once, all the possible values are looped through for the 1st zero detected
     #we will have all our possible solutions.
     
     print("One of the Sudoku solution is:") 
     print(A)


#=====================================================
# Calling the final solve_sudoku(S) to GET THE SOLUTION/S
solve_sudoku(S)
#=====================================================

# Suggested Sudoku Problem
# 5 3 0 0 7 0 0 0 0
# 6 0 0 1 0 5 0 0 0
# 0 9 8 0 0 0 0 6 0
# 8 0 0 0 6 0 0 0 3
# 4 0 0 8 0 3 0 0 1
# 7 0 0 0 2 0 0 0 6
# 0 6 0 0 0 0 2 8 0
# 0 0 0 4 1 9 0 0 5
# 0 0 0 0 8 0 0 0 0
