# minesweeper game home assignment

import random
import string

# asking the user to enter grid size and number of mines to be placed in the grid
while True:
    try:    
        grid_size = int(input("Enter the board size in square to play: "))
        if grid_size > 0:
            break
        else:
            print("Error: Invalid input. Please enter a positive number (greater than zero).")  
    except ValueError:
        print("Error: Invalid input. Please enter a positive number instead of a string.")
    

# asking the user to input the number of mines to be placed in the game
while True:
    try:
        num_mines = int(input("Enter the number of mine to be placed in the board: "))
        if 0 < num_mines and num_mines < (((grid_size ** 2) * 0.8) // 1):
            break
        else:
            print("Error: Invalid input. Please enter a number in range of ", grid_size, "and", grid_size**2)
    except ValueError:
        print("Error: Invalid input. Please enter a positive number instead of a string.")

print("Let's begin the minesweeper game!")

# using the input to create header of the board_grid
board_grid_header = list(range(1, grid_size + 1)) 

# using the input to create row alphabets till the length of input in ABC...
# row_alphabet 
# string.ascii_uppercase (study this for alphabetic order in list)

# using the input to create a nested list, which serves as a 2D board.
board_grid = [["#" for i in range(grid_size)] for j in range(grid_size)]

# print(board_grid_header)
print(" ".join([str(heading) for heading in board_grid_header]))

# print(' '.join(map(str, board_grid_header)))

# printing the board size in 2D shape with rows and columns as grid_size
for row in board_grid:
    print(' '.join(row))
    

# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#       for row in board_grid]))

# placing the mines using random
mine_location = random.sample(range(grid_size ** 2), num_mines)
# how to represent a mine with "X" or "*"


# reveal = input("What field to reveal?")

# for cells in range(grid_size):
#    if board_grid != "mine_location":
#        mines_nearby = 0
""" 
try except for python
for row in board_grid: print row      for the column name ASCII_
hide it or have a completely separate data structure (recommended) - for the showing part
sentdex python
use random.randit

"""


