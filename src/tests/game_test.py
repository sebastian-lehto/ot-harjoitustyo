import unittest
from entities.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_values_correct(self):
        self.assertEqual(str(self.game), "500250250.0250.0")
    
    def test_ticked_values_correct(self):
        self.game.tick()
        self.assertEqual(str(self.game), "505255250.0250.0")

    def test_ticked_values_correct_when_bounce(self):
        self.game.ball.y = 0
        self.game.tick()
        self.assertEqual(str(self.game), "5055250.0250.0")

    def test_ticked_values_correct_when_hit_once(self):
        for x in range(400):
            self.game.tick()
        self.assertEqual(str(self.game), "482.042.0250.0250.0")
    
    def test_ticked_values_correct_when_hit_twice(self):
        self.game.p1y = 450
        for x in range(400):
            self.game.tick()

        self.assertEqual(str(self.game), "670420250.0250.0")

    def test_resetted_values_correct(self):
        self.game.tick()
        self.game.reset()
        self.assertEqual(str(self.game), "500250250.0250.0")

    def test_game_over_when_10_scored(self):
        self.game.scores[0] = 10        
        self.game.tick()
        self.assertEqual(self.game.is_over, True)