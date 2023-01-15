import pygame
from settings import config


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        # self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        # self.collision('vertical')
        self.rect.center += self.direction * speed




