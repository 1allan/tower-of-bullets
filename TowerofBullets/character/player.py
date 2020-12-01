import math
import pygame

from util.functions import load_image
from character.character import Character
from items.weapon import Weapon
from items.bullet import Bullet

IMAGE = 'misc/placeholder.png'


class Player(Character):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, hp: int, energy: int, sprite_group, gold: int = 0, score: int = 0,
                 weapon: Weapon = None, image_file: str = IMAGE):

        super().__init__(surface, position, size, speed, hp, sprite_group, image_file)
        self.energy = energy
        self.gold = gold
        self.score = score

        if self.weapon is None:
            self.weapon = Weapon(self.surface, (self.x, self.y),
                                 (60, 30), 50, sprite_group)
            self.sprite_group.add(self.weapon)

    def shoot(self):
        self.weapon.shoot(pygame.mouse.get_pos())
