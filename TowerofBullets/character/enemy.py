import pygame

from character import Character
from items.weapon import Weapon


class Enemy(Character):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, image_file: str, hp: int, weapon: Weapon):
                 
        super().__init__(surface, position, size, speed, image_file, hp)
        self.damage = damage
        self.weapon = weapon

    def update(self):
        pass

    def draw(self):
        self.update()
        self.surface.blit(self.image, (self.x, self.y))
