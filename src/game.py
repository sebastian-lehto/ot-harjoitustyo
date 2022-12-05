from ball import Ball

class Game:
    def __init__(self):
        self.p1score = 0
        self.p2score = 0
        self.p1y = 250
        self.p2y = 250
        self.p1y_speed = 0
        self.p2y_speed = 0
        self.ball = Ball()
        self.is_over = False

    def tick(self):
        self.ball.move()
        self.p1y = self.p1y + self.p1y_speed
        self.p2y = self.p2y + self.p2y_speed

    def reset(self):
        self.ball = Ball()
        self.p1y = 250
        self.p2y = 250

    def __str__(self):
        return str(self.ball.x)+ str(self.ball.y) + str(self.p1y) + str(self.p2y)
