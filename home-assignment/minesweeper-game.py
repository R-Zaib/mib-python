# minesweeper game home assignment

import random
import string

# asking the user to enter grid size
while True:
    try:    
        grid_size = int(input("Enter the board size in square to play: "))
        if grid_size > 0:
            break
        else:
            print("Error: Invalid input. Please enter a positive number (greater than zero).")  
    except ValueError:
        print("Error: Invalid input. Please enter a positive number instead of a string.")
    

# asking the user to input the number of mines to be placed in the board
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
board_grid_header = [" "] + board_grid_header
 
# board_grid_header = []
# for l in range(grid_size):
#     board_grid_header.append(l + 1)

# using the input to create a nested list, which serves as a 2D board.
board_grid = [["#" for i in range(grid_size + 1)] for j in range(grid_size + 1)]
board_grid[0] = " "

# using the input to create row alphabets till the length of input in ABC...
for row_chr in range(1, grid_size + 1):
    board_grid[row_chr][0] = string.ascii_uppercase[row_chr - 1]  # Using ASCII values to get A, B, C, ...

# print(board_grid_header)
print(" ".join([str(heading) for heading in board_grid_header]))

# print(' '.join(map(str, board_grid_header)))

# printing the board size in 2D shape with rows and columns as grid_size
for row in board_grid:
    print(' '.join(row))
    
# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#       for row in board_grid]))

# placing the mines using random
mine_location = []
while num_mines > len(mine_location):
    r_rand = random.randint(0, grid_size - 1)
    c_rand = random.randint(0, grid_size - 1)
    
    if (r_rand, c_rand) not in mine_location:
        mine_location.append((r_rand, c_rand))

# reveal = input("What field to reveal?")

# for cells in range(grid_size):
#    if board_grid != "mine_location":
#        mines_nearby = 0
""" 

hide it or have a completely separate data structure (recommended) - for the showing part
use slices to create new list, it produces slice from start to end-1   my_list[start:end]
"""


