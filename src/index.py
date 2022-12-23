import pygame
from entities.game import Game
from ui.ui import UI

def main():
    pygame.init() # pylint: disable=no-member
    game = Game()
    WIDTH = game.dimensions[0] # pylint: disable=invalid-name
    HEIGHT = game.dimensions[1] # pylint: disable=invalid-name
    screen_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    interface = UI(game, screen)
    clock = pygame.time.Clock()
    pygame.display.set_caption("PONG")
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                running = False
            if not event.type in (pygame.KEYDOWN, pygame.KEYUP): # pylint: disable=no-member
                continue
            if event.key == pygame.K_w: # pylint: disable=no-member
                game.p1y_speed = -10 if event.type == pygame.KEYDOWN else 0 # pylint: disable=no-member
            elif event.key == pygame.K_s: # pylint: disable=no-member
                game.p1y_speed = 10 if event.type == pygame.KEYDOWN else 0 # pylint: disable=no-member
            elif event.key == pygame.K_UP: # pylint: disable=no-member
                game.p2y_speed = -10 if event.type == pygame.KEYDOWN else 0 # pylint: disable=no-member
            elif event.key == pygame.K_DOWN: # pylint: disable=no-member
                game.p2y_speed = 10 if event.type == pygame.KEYDOWN else 0 # pylint: disable=no-member
            elif event.key == pygame.K_r: # pylint: disable=no-member
                game = Game()

        if game.is_over:
            continue
        #move game forward
        game.tick()
        interface.update()
        pygame.display.update()
        clock.tick(60)


    pygame.quit() # pylint: disable=no-member


if __name__ == "__main__":
    main()
