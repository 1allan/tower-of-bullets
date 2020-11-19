import pygame

from entity import Entity
from utils import *


class Bullet(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 image_file: str, damage: int, speed: int, coords: list):
        super().__init__(surface, position, size, speed=speed, 
                         image_file=image_file)
        self.damage = damage
        self.coords = coords
        self.count = 0

    def hit(self):
        pass

    def move(self, direction=None):
        self.rect.left = direction[0]
        self.rect.top = direction[1]

    def update(self):
        try:
            self.move(self.coords[self.count])
            self.count += 1
        except IndexError:
            pass