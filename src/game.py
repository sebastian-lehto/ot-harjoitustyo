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
        if self.ball.y >= 490 or self.ball.y <= 10:
            self.ball.flip_y()
        if self.ball.x >= 890 and self.ball.x <= 900:
            if self.ball.y >= self.p2y and self.ball.y <= self.p2y + 80 and self.ball.x_speed > 0:
                self.ball.flip_x()
        elif self.ball.x <= 130 and self.ball.x >= 110:
            if self.ball.y >= self.p1y and self.ball.y <= self.p1y + 80 and self.ball.x_speed < 0:
                self.ball.flip_x()
        
        if self.ball.x <= 0:
            self.p2score += 1
            self.reset()
        elif self.ball.x >= 1000:
            self.p1score += 1
            self.reset()
        
        self.p1y = self.p1y + self.p1y_speed
        self.p2y = self.p2y + self.p2y_speed

    def reset(self):
        self.ball = Ball()
        self.p1y = 250
        self.p2y = 250

    def __str__(self):
        return str(self.ball.x)+ str(self.ball.y) + str(self.p1y) + str(self.p2y)
