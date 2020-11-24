import math
import pygame

from util.functions import load_image
from character.character import Character
from items.weapon import Weapon
from items.bullet import Bullet

# IMAGE = 'characters/01.png'
IMAGE = 'misc/placeholder.png'


class Player(Character):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed:int, hp: int, energy: int, gold: int=0, 
                 weapon: Weapon=None, image_file: str=IMAGE):
                 
        super().__init__(surface, position, size, speed, hp, image_file)
        self.energy = energy
        self.gold = gold
        self.last_direction = [1, 0]
        
        if self.weapon is None:
            self.weapon = Weapon(self.surface, (self.rect.left, self.rect.top), 
                             (30, 30), 2)

    def move(self, direction=None):
        if direction[0] == self.last_direction[0] * -1:
            self.last_direction = direction
            self.image = pygame.transform.flip(self.image, True, False)
            self.weapon.image = pygame.transform.flip(self.weapon.image, True,
                                                      False)
        
        speed = self.speed
        # Sets an equivalent speed for diagonals
        if 0 not in direction:
            speed = round(((speed**2 + speed**2)**0.5)/2, 1)
        
        self.rect.left += speed * direction[0]
        self.rect.top += speed * direction[1]

    def shoot(self):
        self.weapon.shoot(pygame.mouse.get_pos())

    def update(self):
        self.weapon.rect.left = self.rect.left
        self.weapon.rect.top = self.rect.top
        self.weapon.draw()