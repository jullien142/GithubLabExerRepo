import unittest
from PostLabSolution_ticTacToeCLI import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board_empty(self):
        self.assertEqual(self.game.board, [" " for _ in range(9)])

    def test_make_valid_move(self):
        result = self.game.make_move(0)
        self.assertTrue(result)
        self.assertEqual(self.game.board[0], "X")

    def test_make_invalid_move(self):
        self.game.make_move(0)
        result = self.game.make_move(0)
        self.assertFalse(result)
        self.assertEqual(self.game.board[0], "X")

    def test_switch_player(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "O")
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "X")

    def test_check_winner_row(self):
        self.game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertEqual(self.game.check_winner(), "X")

    def test_check_winner_column(self):
        self.game.board = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
        self.assertEqual(self.game.check_winner(), "O")

    def test_check_winner_diagonal(self):
        self.game.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        self.assertEqual(self.game.check_winner(), "X")

    def test_draw_condition(self):
        self.game.board = ["X", "O", "X",
                           "X", "O", "O",
                           "O", "X", "X"]
        self.assertTrue(self.game.is_draw())
        self.assertIsNone(self.game.check_winner())

    def test_reset_game(self):
        self.game.board = ["X"] * 9
        self.game.current_player = "O"
        self.game.reset()
        self.assertEqual(self.game.board, [" " for _ in range(9)])
        self.assertEqual(self.game.current_player, "X")


if __name__ == '__main__':
    unittest.main()
