import unittest
from entities.ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()

    def test_ball_starting_position_correct(self):
        self.assertEqual(str(self.ball), "500-250")
    
    def test_ball_position_correct_after_move(self):
        self.ball.move()
        self.assertEqual(str(self.ball), "505-255")

    def test_starting_xspeed_correct(self):
        self.assertEqual(self.ball.x_speed, 5)

    def test_starting_xspeed_correct_after_bounce(self):
        self.ball.flip_x()
        self.assertEqual(self.ball.x_speed, -5.5)
    def test_starting_yspeed_correct_after_bounce(self):
        self.ball.flip_y()
        self.assertEqual(self.ball.y_speed, -5)
    
    def test_starting_yspeed_correct(self):
        self.assertEqual(self.ball.y_speed, 5)
    