from unittest import TestCase

import numpy as np

from conway.game import Game


class GameTests(TestCase):

    def setUp(self) -> None:
        self.game = Game(4, 3)

    def test_initial_board(self):
        expected_board = np.zeros([4, 3], dtype=np.bool)

        np.testing.assert_array_equal(expected_board, self.game.board)

    def test_turn_on_cell(self):
        self.game.turn_on(1, 0)

        self.assertTrue(self.game.is_alive(1, 0))

    def test_turn_off_cell(self):
        self.game.turn_on(0, 1)
        self.game.turn_off(0, 1)

        self.assertFalse(self.game.is_alive(0, 1))

    def test_step_empty(self):
        self.game.step()

        expected_board = np.zeros([4, 3], dtype=np.bool)

        np.testing.assert_array_equal(expected_board, self.game.board)

    def test_step_underpopulated_0(self):
        self.game.turn_on(1, 1)

        self.game.step()

        self.assertFalse(self.game.is_alive(1, 1))

    def test_step_underpopulated_1(self):
        self.game.turn_on(0, 1)
        self.game.turn_on(1, 1)

        self.game.step()

        self.assertFalse(self.game.is_alive(0, 1))
        self.assertFalse(self.game.is_alive(1, 1))

    def test_step_keep_alive_2(self):
        self.game.turn_on(0, 1)
        self.game.turn_on(1, 1)
        self.game.turn_on(2, 1)

        self.game.step()

        self.assertTrue(self.game.is_alive(1, 1))

    def test_step_keep_alive_3(self):
        self.game.turn_on(0, 1)
        self.game.turn_on(1, 1)
        self.game.turn_on(2, 1)
        self.game.turn_on(1, 2)

        self.game.step()

        self.assertTrue(self.game.is_alive(1, 1))

    def test_step_overpopulation(self):
        self.game.turn_on(0, 0)
        self.game.turn_on(0, 1)
        self.game.turn_on(1, 1)
        self.game.turn_on(2, 1)
        self.game.turn_on(1, 2)

        self.game.step()

        self.assertFalse(self.game.is_alive(1, 1))

    def test_step_procreation(self):
        self.game.turn_on(0, 0)
        self.game.turn_on(0, 1)
        self.game.turn_on(2, 1)

        self.game.step()

        self.assertTrue(self.game.is_alive(1, 1))
