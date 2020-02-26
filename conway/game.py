import numpy as np


class Game:

    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
        self._board = np.zeros([height, width], dtype=np.bool)

    @property
    def board(self) -> np.array:
        return self._board

    def is_alive(self, row: int, col: int) -> bool:
        try:
            return self._board[row][col]
        except IndexError:
            return False

    def turn_on(self, row: int, col: int):
        self._set_cell(row, col, True)

    def _set_cell(self, row: int, col: int, value: bool):
        self.board[row][col] = value

    def turn_off(self, row: int, col: int):
        self._set_cell(row, col, False)

    def step(self):
        next_board = np.zeros(self._board.shape)

        for i in range(self._height):
            for j in range(self._width):
                next_board[i][j] = self._get_next_step_cell(i, j)

        self._board = next_board

    def _get_next_step_cell(self, i: int, j: int) -> bool:
        neighbor_count = self._get_neighbor_count(i, j)

        if self.is_alive(i, j) and neighbor_count in (2, 3):
            return True
        elif not self.is_alive(i, j) and neighbor_count == 3:
            return True

        return False

    def _get_neighbor_count(self, i: int, j: int) -> int:
        neighbor_indices = [
            (i - 1, j - 1), (i, j - 1), (i + 1, j - 1),
            (i - 1, j), (i + 1, j),
            (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)
        ]
        return sum(1 for row, col in neighbor_indices if self.is_alive(row, col))
