# PYTHONSWEEPER
Pysweeper is a Python implementation of the classic Minesweeper game. It is a simple game where the player has to find all the mines in a grid without detonating any of them. The player can mark a cell as a mine by right-clicking on it. The game ends when the player detonates a mine or when all the cells that are not mines are revealed. The libraty focuses on the game logic and does not provide any graphical interface. The game can be played in the terminal or in a graphical interface using the Pygame library.

## Installation
The library can be installed using pip:

```
pip install pythonsweeper
```

## Usage

```python
import pythonsweeper as ms

# Create a game with 10 rows, 10 columns and 10 mines

game = ms.Game(10, 10, 10)

# Reveal a cell

game.reveal(0, 0)

# Mark a cell as a mine

game.mark(0, 0)

# Get the player's board

game.get_player_board()

# Get the game's board

game.get_board()

#etc.
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors and acknowledgment
The library was created by Boris Khesin (aka Shagulka) and is maintained by him.

## Project status
The library is still in development and is not yet ready for production use.