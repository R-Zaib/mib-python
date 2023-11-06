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

# using the input to create a nested list, which serves as a 2D board with its headings
board_grid = [["#" for i in range(grid_size + 1)] for j in range(grid_size + 1)]
board_grid[0] = [" "] + list(range(1, grid_size + 1))   # to add headings as 1, 2, 3, ...
# should I convert the board_grid[0] to "str" so they don't count 
# when mines nearby are being calculated

for row_chr in range(1, grid_size + 1):
    board_grid[row_chr][0] = string.ascii_uppercase[row_chr - 1]  # using ASCII values to get A, B, C, ...


# placing the mines using random
mine_location = []
while num_mines > len(mine_location):
    r_rand = random.randint(0, grid_size - 1)
    c_rand = random.randint(0, grid_size - 1)
    
    if (r_rand, c_rand) not in mine_location:
        mine_location.append((r_rand, c_rand))
       

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
    if not letter.isalpha() or not letter.isupper():
        return False
    if not number.isdigit() or int(number) < 1:
        return False
    return True

# reference https://stackoverflow.com/questions/40209158/checking-if-an-input-is-formatted-correctly-in-python-3

displayBoard()    


# creating a game loop

# asking the user to reveal a field
while True:
    reveal = input("Which field to reveal?")
    if valid_reveal_input(reveal):
        print("Let's see if you hit a mine!")
    else:
        print("Error! Invalid input: Please enter a valid field (A1, B2, C3...).")

# determining the neighbouring mines in board_grid
def neighbouring_mines(row, col, grid_size, baord_grid):
    mine_count = 0      # total number of mines nearby
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < grid_size and 0 <= c < grid_size:
                if board_grid[r][c] == "X":         # representing "X" here for a mine
                    mine_count += 1
    return mine_count

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

    """ 
    hide it or have a completely separate data structure (recommended) - for the showing part
    use slices to create new list, it produces slice from start to end-1   my_list[start:end]
    """

# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#       for row in board_grid]))

# can also create 3/4 different levels of game = Easy, Medium, Hard / Expert
# pygame or tkinter or pyqt5
