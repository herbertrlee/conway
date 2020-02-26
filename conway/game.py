import numpy as np


class Game:

    def __init__(self, width: int, height: int):
        self._board = np.zeros([width, height], dtype=np.bool)

    @property
    def board(self) -> np.array:
        return self._board

    def turn_on(self, row: int, col: int):
        self._set_cell(row, col, True)

    def _set_cell(self, row: int, col: int, value: bool):
        self.board[row][col] = value

    def turn_off(self, row: int, col: int):
        self._set_cell(row, col, False)
