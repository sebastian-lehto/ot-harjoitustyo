

class Ball:
    def __init__(self):
        self.X = 500
        self.Y = 250

        self.XSpeed = 10
        self.YSpeed = 10

    def move(self):
        self.X = self.X + self.XSpeed
        self.Y = self.Y + self.YSpeed

    def bounce(self):
        self.XSpeed = self.XSpeed * -1

    def __str__(self):
        return str(self.X) + "-" + str(self.Y)