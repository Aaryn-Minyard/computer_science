import unittest
from rock import RockPaperScissors
from unittest.mock import patch

class TestRockPaperScissors(unittest.TestCase):

    def setUp(self):
        self.game = RockPaperScissors()

    def test_initial_health(self):
        self.assertEqual(self.game.get_player1_health(), 40)
        self.assertEqual(self.game.get_player2_health(), 40)

    def test_initial_rounds(self):
        self.assertEqual(self.game.get_rounds(), 0)

    def test_initial_wins(self):
        self.assertEqual(self.game.get_player1_wins(), 0)
        self.assertEqual(self.game.get_player2_wins(), 0)

    @patch('builtins.input', side_effect=[0])
    @patch('random.randint', return_value=1)
    def test_play_round_player2_wins(self, mock_randint, mock_input):
        self.game.play_round()
        self.assertEqual(self.game.get_player1_health(), 20)
        self.assertEqual(self.game.get_player2_health(), 40)
        self.assertEqual(self.game.get_player1_wins(), 0)
        self.assertEqual(self.game.get_player2_wins(), 1)
        self.assertEqual(self.game.get_rounds(), 1)

    @patch('builtins.input', side_effect=[0])
    @patch('random.randint', return_value=2)
    def test_play_round_player1_wins(self, mock_randint, mock_input):
        self.game.play_round()
        self.assertEqual(self.game.get_player1_health(), 40)
        self.assertEqual(self.game.get_player2_health(), 20)
        self.assertEqual(self.game.get_player1_wins(), 1)
        self.assertEqual(self.game.get_player2_wins(), 0)
        self.assertEqual(self.game.get_rounds(), 1)

    @patch('builtins.input', side_effect=[0])
    @patch('random.randint', return_value=0)
    def test_play_round_tie(self, mock_randint, mock_input):
        self.game.play_round()
        self.assertEqual(self.game.get_player1_health(), 40)
        self.assertEqual(self.game.get_player2_health(), 40)
        self.assertEqual(self.game.get_player1_wins(), 0)
        self.assertEqual(self.game.get_player2_wins(), 0)
        self.assertEqual(self.game.get_rounds(), 1)

    @patch('builtins.input', side_effect=['invalid'])
    def test_play_round_invalid_input(self, mock_input):
        self.game.play_round()
        self.assertEqual(self.game.get_rounds(), 0)

if __name__ == '__main__':
    unittest.main()