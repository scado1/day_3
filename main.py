import pygame
from config import config


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption('day 3')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.fill('cyan')
            pygame.display.update()
            self.clock.tick(config.fps)


if __name__ == '__main__':
    game = Game()
    game.run()
