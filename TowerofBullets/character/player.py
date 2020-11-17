import pygame

from character.character import *
from items.weapon import *


class Player(Character):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed:int, image_file: str, hp: int, energy: int, gold: int=0,
                 weapon: Weapon=None):
        super().__init__(surface, position, size, speed, image_file, hp)
        self.energy = energy
        self.gold = gold
        self.weapon = None if weapon is None else weapon # arrumar Weapon depois => self.weapon = Weapon(bla.bla.bla)

    def change_weapon(self,weapon: Weapon):
        self.weapon = weapon
    
    def update(self):
        pass

    def draw(self):
        self.update()
        self.surface.blit(self.image, (self.x, self.y))