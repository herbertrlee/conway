from unittest import TestCase

import numpy as np

from conway.game import Game


class GameTests(TestCase):

    def setUp(self) -> None:
        self.game = Game(3, 3)

    def test_initial_board(self):
        expected_board = np.zeros([3, 3], dtype=np.bool)

        np.testing.assert_array_equal(expected_board, self.game.board)

    def test_turn_on_cell(self):
        self.game.turn_on(1, 0)

        expected_board = np.array(
            [
                [False, False, False],
                [True, False, False],
                [False, False, False]
            ],
            dtype=np.bool
        )

        np.testing.assert_array_equal(expected_board, self.game.board)

    def test_turn_off_cell(self):
        for i in range(3):
            for j in range(3):
                self.game.turn_on(i, j)

        self.game.turn_off(0, 1)

        expected_board = np.array(
            [
                [True, False, True],
                [True, True, True],
                [True, True, True]
            ],
            dtype=np.bool
        )
        np.testing.assert_array_equal(expected_board, self.game.board)
