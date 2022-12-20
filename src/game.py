from ball import Ball

class Game:
    """
    Luokka, jonka avulla ylläpidetään peliin liittyviä tietoja.

    Attributes:
        dimensions: tuple, joka edustaa pelialueen leveyttä ja korkeutta.
        scores: lista, joka sisältää pelaajien pisteet.
        p1y: pelaajan 1 y-koordinaatti.
        p2y: pelaajan 2 y-koordinaatti.
        p1speed: pelaajan 1 nopeus y-akselilla.
        p2speed: pelaajan 2 nopeus y-akselilla.
        ball: palloa edustava Ball-luokan olio
        is_over: pelin tilaa edustava boolean muuttuja.
    """
    def __init__(self):
        """
        Luokan konstruktori, joka luo uuden pelin.

        """
        self.dimensions = (1000, 500)
        self.scores = list((0, 0))
        self.p1y = self.dimensions[1] / 2
        self.p2y = self.dimensions[1] / 2
        self.p1y_speed = 0
        self.p2y_speed = 0
        self.ball = Ball()
        self.is_over = False

    def tick(self):
        """
        Luokan keskeisin metodi, joka liikuttaa peliä eteenpäin. Metodi tarkastaa osuuko pallo johonkin,
        onko pallo pelialueen ulkopuolella (maali), tai onko peli loppunut.
        """
        self.ball.move()
        if self.ball.y >= (self.dimensions[1] - 10) or self.ball.y <= 10:
            self.ball.flip_y()
        if self.ball.x + self.ball.x_speed >= self.dimensions[0] - 100 >= self.ball.x:
            if self.ball.y >= self.p2y - 10 and self.ball.y <= self.p2y + 80 and self.ball.x_speed > 0:
                self.ball.y_speed = -8 * (((self.p2y + 80) - (self.ball.y) - 45) / 45)
                self.ball.flip_x()
        elif self.ball.x  + self.ball.x_speed <= 120 <= self.ball.x:
            if self.ball.y >= self.p1y - 10 and self.ball.y <= self.p1y + 80 and self.ball.x_speed < 0:
                self.ball.y_speed = -8 * (((self.p1y + 80) - (self.ball.y) - 45) / 45)
                self.ball.flip_x()

        if self.ball.x <= 0:
            self.scores[1] += 1
            self.reset()
        elif self.ball.x >= self.dimensions[0]:
            self.scores[0] += 1
            self.reset()

        self.p1y = self.p1y if not -6  <= self.p1y + self.p1y_speed <= self.dimensions[1] - 80 else self.p1y + self.p1y_speed
        self.p2y = self.p2y if not -6  <= self.p2y + self.p2y_speed <= self.dimensions[1] - 80 else self.p2y + self.p2y_speed

        if self.scores[0] >= 10 or self.scores[1] >= 10:
            self.is_over = True

    def reset(self):
        """
        Palauttaa pelin alkutilaan maalin jälkeen.
        """
        self.ball = Ball()
        self.p1y = self.dimensions[1] / 2
        self.p2y = self.dimensions[1] / 2

    def __str__(self):
        """
        Muodostaa pelistä merkkijonomuotoisen esityksen.

        Returns:
            Merkkijono, joka kertoo pallon ja pelaajien x- ja y-koordinaatit
        """
        return str(self.ball.x)+ str(self.ball.y) + str(self.p1y) + str(self.p2y)
