import pygame

from bullet import Bullet
from entity import Entity


class Weapon:
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, speed: int, bullet: Bullet):
        super().__init__(surface, position, size, speed)
        self.bullet = bullet

    def update(self):
        self.surface.blit(self.image, (self.x, self.y))
