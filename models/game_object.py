import pygame
from pygame import Surface
from settings import config
from models.entity import Entity
from random import randint


class GameObject(Entity):
    def __init__(self, object_name, pos, groups):
        super().__init__(groups)
        self.object_name = object_name
        self.object_params = config.game_object[object_name]

        self.image = pygame.image.load(self.object_params['img'])
        self.rect = self.image.get_rect(topleft=pos)
        pass

    def update(self):
        # self.move(config.game_object[self.object_name]['speed'])
        self.direction.x = -1
        self.move(self.object_params['speed'])
#
# def create_object(object_name: str, **game_object) -> dict:
#     properties = {
#         "type": object_name,
#         "surface": Surface(game_object['size']).fill((0, 255, 0)),
#         "rect": pygame.Rect(game_object['rect'], (game_object['size'])),
#         "speed": (-(randint(config.velocity - 2, config.velocity + 3)), 0),
#     }
#     return properties
