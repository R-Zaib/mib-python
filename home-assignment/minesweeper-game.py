import random
import string
import copy
import time

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
            if 3 < grid_size < 10 :
                break
            else:
                slow_type("Error: Invalid input. Please enter a number between 4 to 9.")  
        except ValueError:
            slow_type("Error: Invalid input. Please enter a positive number.")
        
    while True:         # asking for number of mines to be placed
        try:
            num_mines = int(input("Enter the number of mine to be placed in the board: "))
            max_mines = int(grid_size ** 2 * 0.8 // 1)
            if grid_size <= num_mines and num_mines <= max_mines:
                break
            else:
                slow_type("Error: Invalid input. Please enter a number in range of ", grid_size, "and", max_mines)
        except ValueError:
            slow_type("Error: Invalid input. Please enter a positive number.")    

    slow_type("Let's begin the minesweeper game!")
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
    in order to add mines as 'X's on the game board
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

def display_board(board_grid):
    # reference https://stackoverflow.com/questions/69489264/i-need-to-print-the-two-dimensional-list-mult-table-by-row-and-column
    """ 
    to show/display/print the game board without spaces used the ' '.join 
    and displayed the game board grid with row and column indices.
    """
    board_grid_representation = game_array(board_grid)
    for row in board_grid_representation:
        print(' '.join([str(cell) for cell in row]))

def valid_reveal_input(alpha_str, valid_alphabets, grid_size):
    # reference https://stackoverflow.com/questions/40209158/checking-if-an-input-is-formatted-correctly-in-python-3
    """ 
    to make sure that the reveal input by user is as per indexes available on board
    restricted the reveal input and validated it individually by separating input[0] and input[1]
    used the reference to see hwo it is done and added additional condition for both letter and number
    """
    if len(alpha_str) != 2:
        return False
    letter = alpha_str[0]
    number = alpha_str[1]
    if not letter.isalpha() or not letter.isupper() or not letter in valid_alphabets:
        return False
    if not number.isdigit() or int(number) < 1 or int(number) > grid_size:
        return False
    return True

def convert_alphanumeric_input_to_grid_coordinate(reveal, row_alphabets):
    """ 
    the user input follows A1, B2, C3... but the grid data structure has different coordinates for each field/location
    this function converts alphanumeric input (e.g., 'A3') to grid coordinates and return (row_index, col_index)
    """
    alphabet_row_character = reveal[0]
    row_index = row_alphabets.index(alphabet_row_character)
    col_index = reveal[1]
    col_index = int(col_index) - 1
    return (row_index, col_index)

def determine_neighbours_location(x_coordinate, y_coordinate):
    """ 
    to find out the valid neighbours of a selected field, a multiple stages approach was taken
    stage 1: figure out the valid neighbour within the grid.
             to do so, created an empty list of valid_neighbour_r_list and valid_neighbour_c_list
             conditioned it to be within the MIN and MAX possible index value 
    stage 2: paired both valid_neighbour_r_list and valid_neighbour_c_list in a tuple and append it in neighbour_location_pairs
             the appending process is a cartesian product for each x and y coordinates          
    stage 3: removed the original paid of x and y coordinates (as they were not **neighbours**) from neighbour_location_pairs
    """
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
    mine_count = 0      
    if (row, col) in mines_location:
        print("You hit a mine!!")
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
    used the reference to create this effect
    """
    import sys
    typing_speed = 140 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    
    print()

def remove_duplicates(duplicate_list):
    # reference: https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
    """ 
    this function takes a list as input and removes duplicate elements,
    returning a new list with only unique elements
    the process is done with help of set, example taken from reference
    """ 
    unique_list = list(set(duplicate_list))

    return unique_list

def reveal_field(coordinates, mines_locations, revealed_locations, locations_to_reveal):
    """ 
    to reveal the hidden fields based on surrounding mines in the neighours, this function uses multiple stages approach
    - declares required variables within the function from input parameter and other functions
    - takes the coordinates (row, col) and add them in revealed_locations list so they are not repeatedly revealed
    - cascades the neighour fields checking process only if the mines_count is 0
    - adds the location for unrevealed coordinates/pairs to locations_to_reveal list 
    and returns an Updated locations_to_reveal list.

    """
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

def continue_playing_game(revealed_locations, num_mines, grid_size):
    """ 
    this function checks if the game should continue based on the revealed locations,
    the number of mines, and the grid size.
    """
    return len(revealed_locations) + num_mines != grid_size ** 2

minesweeper_welcome_art = """
   _   _   _   _   _   _   _   _   _   _   _   _     
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \  
 ( M | I | N | E | S | W | E | E | P | E | R | ! )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
"""

minesweeper_gameover_art = """
   _____          __  __ ______    ______       ________ _____  
  / ____|   /\   |  \./  |  ____|  / __ \ \     / /  ____|  __ \ 
 | |  __   /  \  |  \  / | |__    | |  | \ \   / /| |__  | |__) |
 | | |_ | / /\ \ | |\./| |  __|   | |  | |\ \./ / |  __| |  _  / 
 | |__| |/ ____ \| |  || | |____  | |__| | \   /  | |____| | \ \ 
  \_____/_/    \_\_|  |_ |______|  \____/   \./   |______|_|  \_\ 
"""

welcome_text = """
Welcome to Minesweeper Game!

Game Rules:
1. The game is played on a grid of squares.
2. Some squares contain mines, while others are safe.
3. You will be asked to enter a number for grid size and number of mines.
4. The grid size can range between 4 to 9.
5. The number of mines must be at least equal to the grid size.
6. The maximum number of mines cannot exceed grid size x 4 (for 5x5 grid, max mines can only be 20 mines).
7. Your goal is to uncover all safe squares without hitting a mine.
8. Numbers on uncovered squares indicate the count of mines in adjacent squares.
9. Use the heading combination as alphabet and number to reveal a mine (for example A1, B2, C3 etc).
10. If you win, you can play again by entering "y" upon winning, but if you lose, the game ends!

Be careful! Uncovering a mine ends the game.

Good luck, and enjoy the Minesweeper challenge!
"""

print(minesweeper_welcome_art)
time.sleep(2)
print(welcome_text)
time.sleep(4)


if __name__ == "__main__":

    play_again = True
    while play_again:
    # data structure
        grid_size, num_mines = get_game_input_parameters()                    # call the function to get grid_size and num_mines
        MIN_INDEX_VALUE = 0
        MAX_INDEX_VALUE = grid_size - 1
        board_grid = [["#" for i in range(grid_size)] for j in range(grid_size)] 
        mines_locations = determine_mines_location(num_mines, grid_size)             # extracting mine locations
        # print(mines_locations)                        # prints each location of mines separately (for debugging)
        # place_mines(board_grid, mines_locations)      # shows the mines as "X" on game (for debugging)                                  
        display_board(board_grid)

        row_alphabets = string.ascii_uppercase[:grid_size]
        revealed_locations = []
        locations_to_reveal = []


        while continue_playing_game(revealed_locations, num_mines, grid_size):
            reveal = input("Which field to reveal? ")            # asking the user to reveal a field
            if valid_reveal_input(reveal, row_alphabets, grid_size):
                slow_type("Let's see if you hit a mine!")
                time.sleep(1)
                coordinates  = convert_alphanumeric_input_to_grid_coordinate(reveal, row_alphabets)
                locations_to_reveal.append(coordinates)
                while locations_to_reveal:
                    coordinates = locations_to_reveal.pop(0)
                    if coordinates in revealed_locations:
                        slow_type("This field has been revealed already.")
                    elif coordinates in mines_locations:
                        slow_type("You hit a mine!!")
                        print(minesweeper_gameover_art)
                        quit()
                    else:
                        locations_to_reveal = reveal_field(coordinates, mines_locations, revealed_locations, locations_to_reveal)


                display_board(board_grid)
            else:
                slow_type("Error! Invalid input: Please enter a valid field (A1, B2, C3...).")    

        slow_type("Congratulations, you won!!")
        play_again_input = input("Press y to play again or any other key to exit: ")
        if play_again_input != 'y':
            play_again = False
    
    slow_type("Thank you for playing. Good bye!")
    


