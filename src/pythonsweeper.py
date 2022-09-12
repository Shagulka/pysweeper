from enum import Enum
import random

class Cell(Enum):
    EMPTY = 0
    MINE = 1
    FLAG = 2
    QUESTION = 3
    EXPLODED = 4

class Game:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[Cell.EMPTY for x in range(width)] for y in range(height)]
        self.player_board = [[Cell.EMPTY for x in range(width)] for y in range(height)]
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        for i in range(self.mines):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            while self.board[y][x] == Cell.MINE:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
            self.board[y][x] = Cell.MINE
    
    def _calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == Cell.MINE:
                    continue
                self.board[y][x] = self._get_number(x, y)
    
    def _get_number(self, x, y):
        count = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i < 0 or i >= self.height or j < 0 or j >= self.width:
                    continue
                if self.board[i][j] == Cell.MINE:
                    count += 1
        return count
    
    def _get_cell(self, x, y):
        return self.board[y][x]
    
    def _get_player_cell(self, x, y):
        return self.player_board[y][x]  
    
    def reveal(self, x, y):
        if self._get_cell(x, y) == Cell.MINE:
            self.player_board[y][x] = Cell.EXPLODED
            return False
        self._reveal(x, y)
        return True
    
    def _reveal(self, x, y):
        if self._get_cell(x, y) == Cell.EMPTY:
            self.player_board[y][x] = Cell.EMPTY
            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if i < 0 or i >= self.height or j < 0 or j >= self.width:
                        continue
                    if self._get_player_cell(j, i) == Cell.EMPTY:
                        self._reveal(j, i)
        else:
            self.player_board[y][x] = self._get_cell(x, y)

    def mark(self, x, y):
        if self._get_player_cell(x, y) == Cell.EMPTY:
            self.player_board[y][x] = Cell.FLAG
        elif self._get_player_cell(x, y) == Cell.FLAG:
            self.player_board[y][x] = Cell.QUESTION
        elif self._get_player_cell(x, y) == Cell.QUESTION:
            self.player_board[y][x] = Cell.EMPTY

    def is_won(self):
        for y in range(self.height):
            for x in range(self.width):
                if self._get_cell(x, y) != Cell.MINE and self._get_player_cell(x, y) == Cell.EMPTY:
                    return False
        return True
    
    def is_lost(self):
        for y in range(self.height):
            for x in range(self.width):
                if self._get_cell(x, y) == Cell.MINE and self._get_player_cell(x, y) == Cell.EXPLODED:
                    return True
        return False

    def get_player_cell(self, x, y):
        return self.player_board[y][x]
    
    def get_player_board(self):
        return self.player_board

    def get_board(self):
        return self.board
