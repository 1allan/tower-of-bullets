import pygame

from entity import Entity
from items.weapon import Weapon
from character.character import Character
from character.player import Player

IMAGE = 'characters/01.png'

class Enemy(Character):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, hp: int, sprite_group, image_file: str=IMAGE):
                 
        super().__init__(surface, position, size, speed, hp, sprite_group, image_file)

        if self.weapon is None:
            self.weapon = Weapon(self.surface, (self.rect.left, self.rect.top), 
                             (10, 10), 2, sprite_group)
            self.sprite_group.add(self.weapon)

    def chase(self, coordinates):
        pass

    def shoot(self, coordinates):
        self.weapon.shoot(coordinates)