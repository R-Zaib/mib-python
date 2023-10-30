# Developing Minesweeper game as the project for the first semester. 

Requirements are as follows: Minesweeper

Create a command line minesweeper.

The application on start should ask for two numbers: the size of the board that will be a square, as well as the number of mines to be placed on it.

Both of them should be positive integers, the application should alert the user if the values are not, and reprompt.

After getting the initial values the application should render the board, and ask the user for a field to reveal.

Example:

How big the board should be?

> 5

How many mines are to be placed?

> 7

    1 2 3 4 5

A # # # # #

B # # # # #

C # # # # #

D # # # # #

E # # # # #

What field to reveal?

>

When the user enters the field to reveal (eg: B3) the field gets revealed:

if it's a mine, the game is over, the user lost, the application exits

if it's not a mine, but has mine as neighbours, the field changes to the number showing the number of the neighboring mines discovery: if it has no neighbouring mines, it reveals all fields until there are.

What field to reveal?

> B3

    1 2 3 4 5

A # 1 0 0 0

B # 1 0 0 0

C # 2 1 1 0

D # # # 2 1

E # # # # #

What field to reveal?

> E1

etc.

The game is over and the application prompts the result. The user reveals a mine, and the user loses.

The user reveals each field that is not a mine, the user wins. then prompts to replay or exit.
