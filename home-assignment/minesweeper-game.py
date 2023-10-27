# minesweeper game home assignment

import random

# asking the user to enter grid size and number of mines to be placed in the grid
grid_size = int(input("Enter the board size in square to play: "))
num_mines = int(input("Enter the number of mine to be placed in the board: "))

# how to re-prompt in case the value entered is not a positive integer?
# what if the number of mines the user entered exceeds the total number of placeholders in the board?

# using the input to create a nested list, which serves as a 2D board.
board_grid = [["#"for i in range(grid_size)] for j in range(grid_size)]

# placing the mines using random
mine_location = random.sample(range(grid_size ** 2), num_mines)
# how to represent a mine with "X" or "*"

# how to display the grid in 2D instead of a single line?
# how to present it in columns as 1, 2, 3, 4 and rows as A, B, C, D etc

# assuming it is done, asking the user to reveal a number

reveal = input("What field to reveal?")

# for cells in range(grid_size):
#    if board_grid != "mine_location":
#        mines_nearby = 0



