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
    WIDTH = game.width # pylint: disable=invalid-name
    HEIGHT = game.height # pylint: disable=invalid-name
    screen_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("PONG")
    running = True

    while running:

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # pylint: disable=no-member
                running = False
            elif event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_w: # pylint: disable=no-member
                    game.p1y_speed = -10
                elif event.key == pygame.K_s: # pylint: disable=no-member
                    game.p1y_speed = 10
                elif event.key == pygame.K_UP: # pylint: disable=no-member
                    game.p2y_speed = -10
                elif event.key == pygame.K_DOWN: # pylint: disable=no-member
                    game.p2y_speed = 10
                elif event.key == pygame.K_r: # pylint: disable=no-member
                    game = Game()
            elif event.type == pygame.KEYUP: # pylint: disable=no-member
                if event.key in (pygame.K_w, pygame.K_s): # pylint: disable=no-member
                    game.p1y_speed = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN): # pylint: disable=no-member
                    game.p2y_speed = 0


        #move game forward
        game.tick()

        # fill screen with black
        screen.fill(BLACK)

        font = pygame.font.SysFont(None, 48)
        if game.is_over:
            winner = "PLAYER 1" if game.p1score > game.p2score else "PLAYER 2"
            over_text = font.render((winner + " WINS!"), True, WHITE)
            restart_text = font.render("PRESS R TO RESTART", True, WHITE)
            screen.blit(over_text, ((WIDTH / 3), 200))
            screen.blit(restart_text, ((WIDTH / 3), 350))
            pygame.display.update()
        else:
            # draw net
            pygame.draw.line(screen, WHITE, [(WIDTH / 2), 0], [(WIDTH / 2), HEIGHT], 3)
            # draw ball
            pygame.draw.circle(screen, WHITE, (game.ball.x, game.ball.y), 10)
            # draw players
            pygame.draw.rect(screen, RED, (100, game.p1y, 20, 80))
            pygame.draw.rect(screen, GREEN, ((WIDTH - 100), game.p2y, 20, 80))
            # draw scores
            score1 = font.render(str(game.p1score), True, WHITE)
            score2 = font.render(str(game.p2score), True, WHITE)
            screen.blit(score1, ((WIDTH / 4), 100))
            screen.blit(score2, ((WIDTH - (WIDTH / 4)), 100))

            pygame.display.update()

            clock.tick(60)

    pygame.quit() # pylint: disable=no-member


if __name__ == "__main__":
    main()
