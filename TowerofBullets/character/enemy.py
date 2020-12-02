import pygame

from entity import Entity
from items.weapon import Weapon
from character.character import Character
from character.player import Player

IMAGE = 'characters/01.png'

class Enemy(Character):

    def __init__(self, surface: pygame.Surface, 
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, speed: int, hp: int, image_file: str=IMAGE):
                 
        super().__init__(surface, sprite_group, position, size, speed, hp, image_file)

        if self.weapon is None:
            self.weapon = Weapon(self.surface, sprite_group, 
                                (self.rect.left, self.rect.top), (20, 10), 2)
            self.sprite_group.add(self.weapon)

    def chase(self, coordinates: tuple):
        pass

    def shoot(self, coordinates: tuple):
        self.weapon.shoot(coordinates)