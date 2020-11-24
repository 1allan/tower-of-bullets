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

        self.start_x, self.start_y = position
        self.floating_point_x, self.floating_point_y = position
        self.dest_x, self.dest_y = ratio

        x_diff = self.dest_x - self.start_x
        y_diff = self.dest_y - self.start_y
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed

    def update(self):
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        self.rect.left = int(self.floating_point_x)
        self.rect.top = int(self.floating_point_y)