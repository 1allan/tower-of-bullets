import pygame

from entity import Entity
from utils import *


class Bullet(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 image_file: str, damage: int, speed: int = 0):
        super().__init__(surface, position, size, speed=speed, 
                         image_file=image_file)
        self.damage = damage

    def hit(self):
        pass

    def shoot(self):
        x_final, y_final = pygame.mouse.get_pos()

        # linear coefficient
        m = (y_final - self.rect.top) / (x_final - self.rect.left)

        var = -1 if self.rect.top > y_final else 1

        for i in range(self.rect.top, y_final + (1000 * var), var * self.speed):
            y_next = i
            x_next = ((y_next - self.rect.top) / m) + self.rect.left

            self.move((x_next, y_next))

    def move(self, direction=None):
        # keeps the same speed in diagonals
        # self.speed *= math.ceil((direction[0]**2 + direction[1]**2)**.5 / 2)
        self.rect.left = direction[0]
        self.rect.top = direction[1]
        self.draw()

        # self.rect.top += var * self.speed
        # self.rect.left = ((self.rect.top + 1 - self.rect.top) / m) + self.rect.left