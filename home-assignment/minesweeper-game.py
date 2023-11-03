# minesweeper game home assignment

import random
import string


# def game_loop():


#this will be the main game loop , have to handle the guesses of the user here, 
# if it says its B18, it should check if it is within the game paramenters

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
    
# 3 different = Easy, Medium, Hard, Expert
# pygame or tkinter or pyqt5

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
# board_grid_header = list(range(1, grid_size + 1))    
# board_grid_header = [" "] + board_grid_header

# using the input to create a nested list, which serves as a 2D board with its headings
board_grid = [["#" for i in range(grid_size + 1)] for j in range(grid_size + 1)]
board_grid[0] = [" "] + list(range(1, grid_size + 1))   # to add headings as 1, 2, 3, ...

for row_chr in range(1, grid_size + 1):
    board_grid[row_chr][0] = string.ascii_uppercase[row_chr - 1]  # using ASCII values to get A, B, C, ...

# placing the mines using random
mine_location = []
while num_mines > len(mine_location):
    r_rand = random.randint(0, grid_size - 1)
    c_rand = random.randint(0, grid_size - 1)
    
    if (r_rand, c_rand) not in mine_location:
        mine_location.append((r_rand, c_rand))
       

# print(board_grid_header)
# print(" ".join([str(heading) for heading in board_grid_header]))
# print(' '.join(map(str, board_grid_header)))

# printing the board size in 2D shape with rows and columns as grid_size
def displayBoard():
    for row in board_grid:
        print(' '.join([str(cell) for cell in row]))

# validating the input to reveal a field from the board
def valid_reveal_input(alpha_str):
    if len(alpha_str) != 2:
        return False
    letter = alpha_str[0]
    number = alpha_str[1]
    if not letter.isalpha() and not letter.isupper():
        return False
    if not number.isdigit() or int(number) < 1:
        return False
    return True

# reference https://stackoverflow.com/questions/40209158/checking-if-an-input-is-formatted-correctly-in-python-3

displayBoard()    

# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#       for row in board_grid]))

# creating a game loop

# asking the user to reveal a field
while True
    reveal = input("Which field to reveal?")
    if valid_reveal_input(reveal):
        print("Let's see if you hit a mine!")
    else:
        print("Error! Invalid input: Please enter a valid field (A1, B2, C3...).")
# the first one is a letter, but the others are numbers (but in this case the numbers may go outside)

# how to ensure the user only inputs A1, B2 , C3 . . . .

# if __name__ == "__main__":
#     game_over = False
#     while not game_over:
#         game_loop()
#     quit()
    
#pass game over, work this game over on functionality 
#check within my function, whether it is over or not
#situations in which the game is over.

""" 

hide it or have a completely separate data structure (recommended) - for the showing part
use slices to create new list, it produces slice from start to end-1   my_list[start:end]
"""

# board_grid_header = []
# for l in range(grid_size):
#     board_grid_header.append(l + 1)

