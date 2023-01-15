import pygame
from models.player import Player
# from models.game_object import create_object
from settings import config
from models.game_object import GameObject


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprite = pygame.sprite.Group()
        self.game_objects_sprite = pygame.sprite.Group()

        self.create_map()
        self.player = None

    def create_map(self):
        self.player = Player((0, 0), [self.visible_sprite])

    def run(self):
        GameObject('enemy', (1000, 500), [self.game_objects_sprite])
        # for event in pygame.event.get():
        #     if event.type == create_enemy_event:
        #         self.game_objects_sprite.add(create_object('enemy', **config.game_object['enemy']))
        # enemy = create_object('enemy', **config.game_object['enemy'])
        self.visible_sprite.draw(self.display_surface)
        self.visible_sprite.update()
        self.game_objects_sprite.draw(self.display_surface)
        self.game_objects_sprite.update()
