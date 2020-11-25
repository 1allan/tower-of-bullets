import pygame

from entity import Entity
from items.weapon import Weapon

IMAGE = 'characters/01.png'

class Enemy(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, hp: int, image_file: str=IMAGE):
                 
        super().__init__(surface, position, size, speed, image_file)
        self.weapon = None
        self.hp = hp

        if self.weapon is None:
            self.weapon = Weapon(self.surface, (self.rect.left, self.rect.top), 
                             (10, 10), 2)

    def chase(self, coordinates):
        pass

    def shoot(self, coordinates):
        self.weapon.shoot(coordinates)

    def update(self):
        self.weapon.draw()
        self.weapon.rect.left = self.rect.left
        self.weapon.rect.top = self.rect.top