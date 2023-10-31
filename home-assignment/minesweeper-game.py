# minesweeper game home assignment

import random

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
    

# except ValueError:
#     print("Error: Invalid input. Please enter a positive number instead of a string.")
# except ZeroDivisionError:
#     print("Error: Invalid input. Please enter a positive number (greater than zero).")
# else:
#     print("Let's begin minesweeper game!")


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

# using the input to create a nested list, which serves as a 2D board.
board_grid = [["#"for i in range(grid_size)] for j in range(grid_size)]

# placing the mines using random
# mine_location = random.sample(range(grid_size ** 2), num_mines)
# how to represent a mine with "X" or "*"

# how to display the grid in 2D instead of a single line?
# how to present it in columns as 1, 2, 3, 4 and rows as A, B, C, D etc

# assuming it is done, asking the user to reveal a number

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


