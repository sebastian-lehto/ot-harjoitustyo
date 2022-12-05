import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_values_correct(self):
        self.assertEqual(str(self.game), "500250250250")
    
    def test_ticked_values_correct(self):
        self.game.tick()
        self.assertEqual(str(self.game), "510260250250")

    def test_resetted_values_correct(self):
        self.game.tick()
        self.game.reset()
        self.assertEqual(str(self.game), "500250250250")