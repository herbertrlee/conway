from unittest import TestCase


class GameTests(TestCase):

    def test_initial_game_state(self):
        game = Game(3, 3)

        expected_game_state = np.