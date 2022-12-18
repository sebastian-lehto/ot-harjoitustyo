from ball import Ball

class Game:

    def __init__(self):
        self.width = 1000 # pylint: disable=invalid-name
        self.height = 500 # pylint: disable=invalid-name
        self.p1score = 0
        self.p2score = 0
        self.p1y = self.height / 2
        self.p2y = self.height / 2
        self.p1y_speed = 0
        self.p2y_speed = 0
        self.ball = Ball()
        self.is_over = False

    def tick(self):
        self.ball.move()
        if self.ball.y >= (self.height - 10) or self.ball.y <= 10:
            self.ball.flip_y()
        if self.ball.x + self.ball.x_speed >= self.width - 100 >= self.ball.x:
            if self.ball.y >= self.p2y and self.ball.y <= self.p2y + 80 and self.ball.x_speed > 0:
                self.ball.flip_x()
        elif self.ball.x  + self.ball.x_speed <= 120 <= self.ball.x:
            if self.ball.y >= self.p1y and self.ball.y <= self.p1y + 80 and self.ball.x_speed < 0:
                self.ball.flip_x()

        if self.ball.x <= 0:
            self.p2score += 1
            self.reset()
        elif self.ball.x >= self.width:
            self.p1score += 1
            self.reset()

        self.p1y = self.p1y + self.p1y_speed
        self.p2y = self.p2y + self.p2y_speed

        if self.p1score >= 10 or self.p2score >= 10:
            self.is_over = True

    def reset(self):
        self.ball = Ball()
        self.p1y = self.height / 2
        self.p2y = self.height / 2

    def __str__(self):
        return str(self.ball.x)+ str(self.ball.y) + str(self.p1y) + str(self.p2y)
