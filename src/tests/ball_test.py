import unittest
from ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()

    def test_ball_starting_position_correct(self):
        self.assertEqual(str(self.ball), "500-250")

    def test_starting_xspeed_correct(self):
        self.assertEqual(self.ball.XSpeed, 10)

    def test_starting_xspeed_correct_after_bounce(self):
        self.ball.bounce()
        self.assertEqual(self.ball.XSpeed, -10)
    
    def test_starting_yspeed_correct(self):
        self.assertEqual(self.ball.YSpeed, 10)
    