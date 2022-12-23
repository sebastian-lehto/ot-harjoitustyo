

class Ball:
    """
    Luokka, jonka avulla seurataan ja muutetaan pallon liikettä ja sijaintia.

    Atributes:
        x: Pallon x-koordinaatti
        y: Pallon y-koordinaatti
        x_speed: Pallon vauhti x-akselilla
        y_speed: Pallon vauhti y-akselilla
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden pallon.

        """

        self.x = 500 # pylint: disable=invalid-name
        self.y = 250 # pylint: disable=invalid-name

        self.x_speed = 5
        self.y_speed = 5

    def move(self):
        """
        Kasvattaa x-koordinaattia x_speed:n arvolla, eli liikuttaa palloa x-akselilla.
        Kasvattaa y-koordinaattia y_speed:n arvolla, eli liikuttaa palloa y-akselilla.
        """
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def flip_x(self):
        """
        Kääntää pallon suunnan x-akselilla.
        """
        self.x_speed = self.x_speed * -1.1

    def flip_y(self):
        """
        Kääntää pallon suunnan x-akselilla.
        """
        self.y_speed = self.y_speed * -1

    def __str__(self):
        """
        Muodostaa pallosta merkkijonomuotoisen esityksen.

        Returns:
            Merkkijono, joka kertoo pallon x- ja y-koordinaatit.
        """
        return str(self.x) + "-" + str(self.y)
