import numpy as np


class Game:

    def __init__(self, width: int, height: int):
        self._board = np.zeros([width, height], dtype=np.bool)

    @property
    def board(self) -> np.array:
        return self._board
