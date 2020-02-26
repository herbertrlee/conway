from unittest import TestCase

import numpy as np

from conway.game import Game


class GameTests(TestCase):

    def test_initial_board(self):
        self.game = Game(3, 3)

        expected_board = np.zeros([3, 3], dtype=np.bool)

        np.testing.assert_array_equal(expected_board, self.game.board)
