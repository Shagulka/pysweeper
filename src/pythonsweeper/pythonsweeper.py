from enum import Enum
import random


class GameStatus(Enum):
    RUNNING = 1
    WIN = 2
    LOSE = 3


class Game:
    # mine is 9
    # empty is 0
    # 1-8 is the number of mines around the cell
    # unrevealed is -1
    #flag is -2
    #question is -3
    # return status of the game after each move
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[0 for x in range(width)] for y in range(height)]
        self.player_board = [[-1 for x in range(width)] for y in range(height)]
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        for i in range(self.mines):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.board[y][x] == 0:
                    self.board[y][x] = 9
                    break

    def _calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != 9:
                    self.board[y][x] = self._count_mines_around(x, y)

    def _count_mines_around(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (x + i >= 0 and x + i < self.width) and (y + j >= 0 and y + j < self.height):
                    if self.board[y + j][x + i] == 9:
                        count += 1
        return count

    # board generation is done

    # avoid out of bounds and infinite recursion

    def _reveal(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        if self.player_board[y][x] != -1:
            return
        self.player_board[y][x] = self.board[y][x]
        if self.board[y][x] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not (x < 0 or x >= self.width or y < 0 or y >= self.height):
                        if self.board[y+i][x+j] != 9:
                            self._reveal(x+i, y+j)

    def _flag(self, x, y):
        if self.player_board[y][x] == -1:
            self.player_board[y][x] = -2
        elif self.player_board[y][x] == -2:
            self.player_board[y][x] = -3
        elif self.player_board[y][x] == -3:
            self.player_board[y][x] = -1

    def _check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.player_board[y][x] == -1 and self.board[y][x] != 9:
                    return False
        return True

    def _check_lose(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.player_board[y][x] == 9:
                    return True
        return False

    def reveal(self, x, y):
        if self.player_board[y][x] == -1:
            self._reveal(x, y)
        if self._check_win():
            return GameStatus.WIN
        if self._check_lose():
            return GameStatus.LOSE
        return GameStatus.RUNNING

    def flag(self, x, y):
        self._flag(x, y)
        if self._check_win():
            return GameStatus.WIN
        return GameStatus.RUNNING

    def get_board(self):
        return self.player_board

    def get_mines(self):
        return self.board
