import random
import string
import copy

random.seed(1) # to fix the random selection, remove it after testing

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

# determining the mines locations using random
def determine_mines_location(num_mines, grid_size):
    mine_location = []
    while len(mine_location) < num_mines:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        
        if (row, col) not in mine_location:
            mine_location.append((row, col))
    return mine_location

# mines are not restricted to grid array ---> Fix this
# num of mines are same as grid_size

def place_mines(board, mine_locations):
    grid_size = len(board)
    for location in mine_locations:
        x, y = location
        if 0 <= x < grid_size and 0 <= y < grid_size:
            board[x][y] = "X"

# creating an array with numbers and alphabets headings
def game_array(board_grid):
    grid_size = len(board_grid)
    board_grid_number_header = [list(range(1, grid_size + 1))]
    board_grid_representation = board_grid_number_header + copy.deepcopy(board_grid)

    aphabets_indices = " " + string.ascii_uppercase[:grid_size] # string/list/tuple slicing applicable to **ordered** data structure
    for row_index, row in enumerate(board_grid_representation):
        row.insert(0, aphabets_indices[row_index])
    return board_grid_representation

# printing the board size in 2D shape with rows and columns as grid_size
def display_board(board_grid):
    board_grid_representation = game_array(board_grid)
    for row in board_grid_representation:
        print(' '.join([str(cell) for cell in row]))

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

def convert_alphanumeric_input_to_grid_coordinate(reveal, row_alphabets):
    alphabet_row_character = reveal[0]
    row_index = row_alphabets.index(alphabet_row_character)
    col_index = reveal[1]
    col_index = int(col_index) - 1
    return (row_index, col_index)

# determining the neighbouring mines in board_grid
def determine_neighbours_location(x_coordinate, y_coordinate):
    neighbour_r_indices = [x_coordinate - 1, x_coordinate, x_coordinate + 1] 
    neighbour_c_indices = [y_coordinate - 1, y_coordinate, y_coordinate + 1]

    valid_neighbour_r_list = []
    for index in neighbour_r_indices:
        if MIN_INDEX_VALUE <= index <= MAX_INDEX_VALUE:
            valid_neighbour_r_list.append(index)
    
    valid_neighbour_c_list = []
    for index in neighbour_c_indices:
        if MIN_INDEX_VALUE <= index <= MAX_INDEX_VALUE:
            valid_neighbour_c_list.append(index)

    neighbour_location_pairs = []
    for row in valid_neighbour_r_list:
        for col in valid_neighbour_c_list:
            pair = (row, col)
            neighbour_location_pairs.append(pair)

    remove_pair = (x_coordinate, y_coordinate)
    neighbour_location_pairs.remove(remove_pair)
    return neighbour_location_pairs


def neighbouring_mines(row, col, mines_location, grid_size):
    mine_count = 0      # total number of mines nearby
    if (row, col) in mines_location:
        print("The game is over! You hit a mine!!")
    else:
        neighbours_locations = determine_neighbours_location(row, col)
        for location in neighbours_locations:
            if location in mines_location:
                mine_count += 1    

    return mine_count


# data structure

grid_size, num_mines = get_game_input_parameters()                          # call the function to get grid_size and num_mines
MIN_INDEX_VALUE = 0
MAX_INDEX_VALUE = grid_size - 1
board_grid = [["#" for i in range(grid_size)] for j in range(grid_size)]    # to create 2D array
mines_location = determine_mines_location(num_mines, grid_size)             # extracting mine locations
print(mines_location)
place_mines(board_grid, mines_location)                                     # call game_array function to extract grid representation
display_board(board_grid)

# creating a game loop
row_alphabets = string.ascii_uppercase[:grid_size]
while True:
    reveal = input("Which field to reveal?")            # asking the user to reveal a field
    if valid_reveal_input(reveal, row_alphabets, grid_size):
        print("Let's see if you hit a mine!")
        row, col = convert_alphanumeric_input_to_grid_coordinate(reveal, row_alphabets)
        mines_count = neighbouring_mines(row, col, mines_location, grid_size)
        board_grid[row][col] = mines_count
        display_board(board_grid)
        break
    else:
        print("Error! Invalid input: Please enter a valid field (A1, B2, C3...).")    

# can use this function as recursive function to check all the fields around
# convert ABC to integer value --> use function like ord to convert character to int using ascii character

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