import pygame
from settings import config
from models.entity import Entity


class Player(Entity):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("./graphics/player.png")
        self.rect = self.image.get_rect(topleft=pos)

        self.speed = config.velocity

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center += self.direction * speed

    def collision(self, direction):
        if direction == "horizontal":
            if self.direction.x > 0 and self.rect.right >= config.width:  # moving right
                self.rect.right = config.width
            if self.direction.x < 0 and self.rect.left <= 0:
                self.rect.left = 0
        if direction == "vertical":
            if self.direction.y > 0 and self.rect.bottom >= config.height:
                self.rect.bottom = config.height
            if self.direction.y < 0 and self.rect.top <= 0:
                self.rect.top = 0
    def update(self):
        self.input()
        self.move(self.speed)
