import math
import pygame

from util.functions import load_image
from character.character import Character
from items.weapon import Weapon
from items.bullet import Bullet

IMAGE = 'misc/placeholder.png'


class Player(Character):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed:int, hp: int, energy: int, sprite_group, gold: int=0,
                 weapon: Weapon=None, image_file: str=IMAGE):
                 
        super().__init__(surface, position, size, speed, hp, sprite_group, image_file)
        self.energy = energy
        self.gold = gold
        self.last_direction = [1, 0]
        
        if self.weapon is None:
            self.weapon = Weapon(self.surface, (self.x, self.y), 
                             (60, 30), 2, sprite_group)
            self.sprite_group.add(self.weapon)

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
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2

        self.weapon.rect.left = self.rect.left
        self.weapon.rect.top = self.rect.top
        self.weapon.draw()