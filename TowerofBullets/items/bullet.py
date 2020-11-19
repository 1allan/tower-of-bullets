import math
import pygame

from entity import Entity
from utils import *


class Bullet(Entity):

    def __init__(self, surface: pygame.Surface, ratio, position: tuple, size: tuple,
                 image_file: str, damage: int, speed: int):
        super().__init__(surface, position, size, speed=speed, 
                         image_file=image_file)
        self.damage = damage
        self.x_ratio, self.y_ratio = ratio

    def update(self):
        self.rect.left += round(5 * self.x_ratio)
        self.rect.top += round(5 * self.y_ratio)