# minesweeper game home assignment

import random
import string
import copy


# def game_loop():


#this will be the main game loop , have to handle the guesses of the user here, 
# if it says its B18, it should check if it is within the game paramenters

# asking the user to enter the game parameters to play
def get_game_input_parameters():
    while True:         # asking user for grid size to play
        try:    
            grid_size = int(input("Enter the board to play: "))
            if grid_size > 0:
                break
            else:
                print("Error: Invalid input. Please enter a positive number. ")  
        except ValueError:
            print("Error: Invalid input. Please enter a positive number.")
        
    while True:         # asking for number of mines to be placed
        try:
            num_mines = int(input("Enter the number of mine to be placed in the board: "))
            max_mines = int(grid_size ** 2 * 0.8 // 1)
            if grid_size <= num_mines and num_mines <= max_mines:
                break
            else:
                print("Error: Invalid input. Please enter a number in range of ", grid_size, "and", max_mines)
        except ValueError:
            print("Error: Invalid input. Please enter a positive number.")    

    print("Let's begin the minesweeper game!")
    return grid_size, num_mines

def game_array(board_grid):
    grid_size = len(board_grid)
    board_grid_number_header = [list(range(1, grid_size + 1))]
    board_grid_representation = board_grid_number_header + copy.deepcopy(board_grid)

    aphabets_indices = " " + string.ascii_uppercase[:grid_size] # string/list/tuple slicing applicable to **ordered** data structure
    for row_index, row in enumerate(board_grid_representation):
        row.insert(0, aphabets_indices[row_index])
    return board_grid_representation

# printing the board size in 2D shape with rows and columns as grid_size
def displayBoard(grid):
    for row in grid:
        print(' '.join([str(cell) for cell in row]))

# determining the mines locations using random
def determine_mines_location(num_mines, grid_size):
    mine_location = []
    while num_mines > len(mine_location):
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        
        if (row, col) not in mine_location:
            mine_location.append((row, col))
    return mine_location
        
def place_mines(board, mine_locations):
    grid_size = len(board)
    for location in mine_locations:
        x, y = location
        if 0 <= x < grid_size and 0 <= y < grid_size:
            board[x][y] = "X"


# validating the input to reveal a field from the board
def valid_reveal_input(alpha_str, valid_alphabets, grid_size):
    if len(alpha_str) != 2:
        return False
    letter = alpha_str[0]
    number = alpha_str[1]
    if not letter.isalpha() or not letter.isupper() or not letter in valid_alphabets:
        return False
    if not number.isdigit() or int(number) < 1 or int(number) > grid_size:
        return False
    return True

# reference https://stackoverflow.com/questions/40209158/checking-if-an-input-is-formatted-correctly-in-python-3

# data structure

grid_size, num_mines = get_game_input_parameters()                          # call the function to get grid_size and num_mines
board_grid = [["#" for i in range(grid_size)] for j in range(grid_size)]    # to create 2D array
mines_location = determine_mines_location(grid_size, num_mines)             # extracting mine locations
place_mines(board_grid, mines_location)                                     # call game_array function to extract grid representation
board_grid_representation = game_array(board_grid)
displayBoard(board_grid_representation)


# creating a game loop


row_alphabets = string.ascii_uppercase[:grid_size]
while True:
    reveal = input("Which field to reveal?")            # asking the user to reveal a field
    if valid_reveal_input(reveal, row_alphabets,grid_size):
        print("Let's see if you hit a mine!")
    else:
        print("Error! Invalid input: Please enter a valid field (A1, B2, C3...).")    


# determining the neighbouring mines in board_grid

# def neighbouring_mines(row, col, grid_size, baord_grid):
#     mine_count = 0      # total number of mines nearby
#     for r in range(row - 1, row + 2):
#         for c in range(col - 1, col + 2):
#             if 0 <= r < grid_size and 0 <= c < grid_size:
#                 if board_grid[r][c] == "X":         # representing "X" here for a mine
#                     mine_count += 1
#     return mine_count

# previously tried this with both while and for loop, but apparently it has errors.
# then fine-tuned the code and asked ChatGPT to evaluate the final version
# it still had errors such range of c was not within range of r

# this is comment for testing purpose only

# def neighbouring_mines(row, col, grid_size):
#     mine_count = 0      # total number of mines nearby
#     r = row - 1
#     while r <= row + 1:      # to check in rows from a range between (row - 1, row + 1)
#         if r >= 0 and r < grid_size:
#             r += 1
#     c = col - 1
#     while c <= col + 1:
#         if c >= 0 and c < grid_size:
#             c += 1
#     return mine_count

# if __name__ == "__main__":
#     game_over = False
#     while not game_over:
#         game_loop()
#     quit()
    
#pass game over, work this game over on functionality 
#check within my function, whether it is over or not
#situations in which the game is over.

    # """ 
    # hide it or have a completely separate data structure (recommended) - for the showing part
    # use slices to create new list, it produces slice from start to end-1   my_list[start:end]
    # """

# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#       for row in board_grid]))

# can also create 3/4 different levels of game = Easy, Medium, Hard / Expert
# pygame or tkinter or pyqt5
