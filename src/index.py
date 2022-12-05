import pygame
from game import Game

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

def main():
    pygame.init() # pylint: disable=no-member
    game = Game()
    screen_size = (1000, 500)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("PONG")

    while not game.is_over:
        ## did player quit

        #move game forward
        game.tick()

        # fill screen with black
        screen.fill(BLACK)
        # draw line in the middle of the screen
        pygame.draw.line(screen, WHITE, [500, 0], [500, 500], 3)
        # draw ball
        pygame.draw.circle(screen, WHITE, (game.ball.x, game.ball.y), 10)
        # draw players
        pygame.draw.rect(screen, RED, (100, game.p1y, 20, 80))
        pygame.draw.rect(screen, GREEN, (900, game.p2y, 20, 80))

        pygame.display.update()
        if game.ball.x > 1000:
            game.is_over = True

        clock.tick(30)

    pygame.quit() # pylint: disable=no-member


if __name__ == "__main__":
    main()
