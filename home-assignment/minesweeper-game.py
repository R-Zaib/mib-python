import random
import string
import copy
import time

random.seed(1) # to fix the random selection, remove it after testing

# def game_loop():
#this will be the main game loop , have to handle the guesses of the user here, 
# if it says its B18, it should check if it is within the game paramenters

def get_game_input_parameters():
    """ 
    to start the game, i ask the user about grid size and number of mines to be placed
    function gets user input for game parameters: grid size and number of mines
    the function accepts both parameters as int and returns integar value
    for both the grid size and number of mines
    """
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

def determine_mines_location(num_mines, grid_size):
    """ 
    to scatter the mines randomly on game baord, using the random function to determine locations 
    for placing mines
    the function takes in num_mines and grid_size as input as integers
    it returns a pair of (row, col) coordinates representing mine locations to place mines
    """
    mine_location = []
    while len(mine_location) < num_mines:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        
        if (row, col) not in mine_location:
            mine_location.append((row, col))
    return mine_location

def place_mines(board, mine_locations):
    """ 
    in order to drop mines as 'X's on the game board
    the function marks the board with mines based on the provided mine locations
    """
    grid_size = len(board)
    for location in mine_locations:
        x, y = location
        if 0 <= x < grid_size and 0 <= y < grid_size:
            board[x][y] = "X"

def game_array(board_grid):
    """ 
    to turn the game board into an indexed grid, the function takes in board_grid (list of list) and
    adds row and column indices to the game board as 1 2 3 4... and A B C D...
    it also imports and use deepcopy to combine the header (as a separate list) and board grid
    """
    grid_size = len(board_grid)
    board_grid_number_header = [list(range(1, grid_size + 1))]      # header is created as a separate list
    board_grid_representation = board_grid_number_header + copy.deepcopy(board_grid)

    aphabets_indices = " " + string.ascii_uppercase[:grid_size]     # slicing acsii characters till grid_size
    for row_index, row in enumerate(board_grid_representation):     
        row.insert(0, aphabets_indices[row_index])
    return board_grid_representation

# printing the board size in 2D shape with rows and columns as grid_size
def display_board(board_grid):
# reference https://stackoverflow.com/questions/69489264/i-need-to-print-the-two-dimensional-list-mult-table-by-row-and-column
    """ 
    to show/display/print the game board without spaces used the ' '.join 
    and displayed the game board grid with row and column indices.
    """
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


def neighbouring_mines(row, col, mines_location):
    """
    Given row, col as coordinates of a position on board, the function calculates the 
    count of mines in its neighbourhood. For this it requires the list of mines_location, where each entry
    is a pair representing location where mine is placed
    """
    mine_count = 0      # total number of mines nearby
    if (row, col) in mines_location:
        print("The game is over! You hit a mine!!")
    else:
        neighbours_locations = determine_neighbours_location(row, col)
        for location in neighbours_locations:
            if location in mines_location:
                mine_count += 1    

    return mine_count


def slow_type(t):
# https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    """ 
    i wanted to add a time delay in my response for the user to make the game
    look visually appealing. 
    i used the link shared above to learn how I could do it and added the function
    """
    import sys
    typing_speed = 80 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    
    print()


# data structure

grid_size, num_mines = get_game_input_parameters()                          # call the function to get grid_size and num_mines
MIN_INDEX_VALUE = 0
MAX_INDEX_VALUE = grid_size - 1
board_grid = [["#" for i in range(grid_size)] for j in range(grid_size)]    # to create 2D array
mines_locations = determine_mines_location(num_mines, grid_size)             # extracting mine locations
print(mines_locations)
place_mines(board_grid, mines_locations)                                     # call game_array function to extract grid representation
display_board(board_grid)

def remove_duplicates(duplicate_list):
    unique_list = list(set(duplicate_list))

    return unique_list

def reveal_field(coordinates, mines_locations, revealed_locations, locations_to_reveal):
    row, col = coordinates
    mines_count = neighbouring_mines(row, col, mines_locations)
    board_grid[row][col] = str(mines_count)
    revealed_locations.append(coordinates)

    if mines_count == 0:
        neighbours_locations_pairs = determine_neighbours_location(row, col)
        for location in neighbours_locations_pairs:
            if location not in revealed_locations:
                locations_to_reveal.append(location)
        locations_to_reveal = remove_duplicates(locations_to_reveal)

    return locations_to_reveal

row_alphabets = string.ascii_uppercase[:grid_size]
revealed_locations = []
locations_to_reveal = []

while len(revealed_locations) + num_mines != grid_size ** 2:
    reveal = input("Which field to reveal?")            # asking the user to reveal a field
    if valid_reveal_input(reveal, row_alphabets, grid_size):
        # slow_type("Let's see if you hit a mine!")
        # time.sleep(1)
        coordinates  = convert_alphanumeric_input_to_grid_coordinate(reveal, row_alphabets)
        locations_to_reveal.append(coordinates)
        while locations_to_reveal:
            coordinates = locations_to_reveal.pop(0)
            if coordinates in revealed_locations:
                print("This field has been revealed already.")
                display_board(board_grid)
            elif coordinates in mines_locations:
                print("You hit a mine.")
                print("Game Over!")
                break
            else:
                locations_to_reveal = reveal_field(coordinates, mines_locations, revealed_locations, locations_to_reveal)


        display_board(board_grid)
    else:
        print("Error! Invalid input: Please enter a valid field (A1, B2, C3...).")    

print("Congratulations, you won!!")

# can use this function as recursive function to check all the fields around

# if __name__ == "__main__":
#     game_over = False
#     while not game_over:
#         game_loop()
#     quit()
    
# creating a game loop