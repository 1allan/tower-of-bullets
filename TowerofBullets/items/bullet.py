import math
import pygame

from entity import Entity
from util.functions import load_image

IMAGE = 'misc/projectiles/default/01.png'


class Bullet(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, 
                 size: tuple, damage: int, speed: int, ratio: tuple,
                 image_file: str=IMAGE):
                 
        super().__init__(surface, position, size, speed=speed,
                         image_file=image_file)
        self.damage = damage
        self.x_ratio, self.y_ratio = ratio

    def update(self):
        self.rect.left += round(self.speed * self.x_ratio)
        self.rect.top += round(self.speed * self.y_ratio)