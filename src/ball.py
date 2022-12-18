

class Ball:
    def __init__(self):
        self.x = 500 # pylint: disable=invalid-name
        self.y = 250 # pylint: disable=invalid-name

        self.x_speed = 5
        self.y_speed = 5

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def flip_x(self):
        self.x_speed = self.x_speed * -1.1
    def flip_y(self):
        self.y_speed = self.y_speed * -1

    def __str__(self):
        return str(self.x) + "-" + str(self.y)
