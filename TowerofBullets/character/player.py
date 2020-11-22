import math
import pygame

from utils import load_image
from character.character import Character
from items.weapon import Weapon
from items.bullet import Bullet


class Player(Character):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed:int, image_file: str, hp: int, energy: int, gold: int=0,
                 weapon: Weapon=None):
                 
        super().__init__(surface, position, size, speed, image_file, hp)
        self.energy = energy
        self.gold = gold
        
        if self.weapon is None:
            self.weapon = Weapon(self.surface, (self.rect.left, self.rect.top), 
                             (30, 30), self.speed,
                             image_weapon='characters/player/weapons/main/01.png',
                             image_bullet='characters/player/bullets/plain/01.png',
                             damage=2)

    def shoot(self):
        self.weapon.shoot()
