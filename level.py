import pygame
from models.player import Player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()
        self.create_map()
        self.player = None

    def create_map(self):
        self.player = Player((0, 0), [self.visible_sprite])

    def run(self):
        self.visible_sprite.draw(self.display_surface)
        self.visible_sprite.update()
