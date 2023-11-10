# Minesweeper CLI Game

## How to Install
1. Clone the repository from: https://github.com/R-Zaib/mib-python.git
2. Make sure you have Python 3 installed.
3. Open your terminal in the project directory, navigate to mib-python/home-assignment.

## How to Run the Game
- Run `python minesweeper-game.py` in your terminal.

## How to Play
1. Enter grid size between 4 to 9.
2. The number of mines must be at least equal to the grid size and maximum of (grid size x 4).
3. Goal: Uncover all safe squares without hitting a mine.
4. Numbers on uncovered squares indicate adjacent mine count.
5. Use the format "A1," "B2," "C3," etc., to reveal a mine.
6. If you win, you can play again by entering "y" upon winning.
7. If you lose, the game ends.

## Limitations of the Game
- No graphical interface, the game supports CLI (Command Line Interface) only.
- Limited to a fixed grid size between 4x4 and 9x9 grid.

## Known Issues
**Input Validation:**
- Limited input validation; entering non-numeric values for grid size or mines may cause unexpected behavior.
**Restart Prompt:**
- The restart prompt is not available for situation when a mine is hit.

## Important
- Read the game rules carefully.

## Version 1.0.0 (2023-11-10)
**Initial Release:**
- Minesweeper CLI game with basic functionality.
- Supports grid sizes from 4x4 to 9x9.
- Allows customization of the number of mines.

## Contributing
- If you'd like to contribute to the project, please follow me on Github and reach out.

## License
- This Minesweeper CLI game is an open licensed free to use (for educational purposes only).
