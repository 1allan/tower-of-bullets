import math
import pygame

from entity import Entity
from utils import *


class Bullet(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, 
                 size: tuple, image_file: str, damage: int, speed: int, 
                 ratio: tuple):
                 
        super().__init__(surface, position, size, speed=speed,
                         image_file=image_file)
        self.damage = damage
        self.x_ratio, self.y_ratio = ratio

    def update(self):
        self.rect.left += round(self.speed * self.x_ratio)
        self.rect.top += round(self.speed * self.y_ratio)