import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

class UI:

    def __init__(self, game, screen):
        """
        Luokan konstruktori, joka luo uuden käyttöliittymän
        """
        self.game = game
        self.screen = screen
        self.width = game.dimensions[0]
        self.height = game.dimensions[1]

    def update(self):
        """
        Päivittää käyttöliittymän pelin tilan mukaan.
        """
        # fill screen with black
        self.screen.fill(BLACK)

        font = pygame.font.SysFont(None, 48)

        # draw game over screen
        if self.game.is_over:
            winner = "PLAYER 1" if self.game.scores[0] > self.game.scores[1] else "PLAYER 2"
            over_text = font.render((winner + " WINS!"), True, WHITE)
            restart_text = font.render("PRESS R TO RESTART", True, WHITE)
            self.screen.blit(over_text, ((self.width / 3), 200))
            self.screen.blit(restart_text, ((self.width / 3), 350))
            pygame.display.update()

        else:
            # draw net
            middle = (self.width / 2)
            pygame.draw.line(self.screen, WHITE, [middle, 0], [middle, self.height], 3)
            # draw ball
            pygame.draw.circle(self.screen, WHITE, (self.game.ball.x, self.game.ball.y), 10)
            # draw players
            pygame.draw.rect(self.screen, RED, (100, self.game.p1y, 20, 80))
            pygame.draw.rect(self.screen, GREEN, ((self.width - 100), self.game.p2y, 20, 80))
            # draw scores
            score1 = font.render(str(self.game.scores[0]), True, WHITE)
            score2 = font.render(str(self.game.scores[1]), True, WHITE)
            self.screen.blit(score1, ((self.width / 4), 100))
            self.screen.blit(score2, ((self.width - (self.width / 4)), 100))
