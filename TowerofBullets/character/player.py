import pygame

from character import Character
from weapon import Weapon


class Player(Character):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed:int, hp: int, energy: int, gold: int=0,
                 weapon: Weapon=None):
        super().__init__(surface, position, size, speed, hp)
        self.hp = hp
        self.energy = energy
        self.gold = gold
        self.weapon = Weapon() if weapon is None else weapon

    def change_weapon(self,weapon: Weapon):
        self.weapon = weapon
    
    def update(self):
        pass

    def draw(self):
        self.update()
        self.surface.blit(self.image, (self.x, self.y))