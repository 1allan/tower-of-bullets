import math
import pygame

from util.functions import load_image
from character.character import Character
from items.weapon import Weapon
from items.bullet import Bullet

IMAGE = 'misc/placeholder.png'


class Player(Character):

    def __init__(self, surface: pygame.Surface, 
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, speed: int, hp: int, energy: int, 
                 wall_sprites: pygame.sprite.Group, gold: int = 0,
                 score: int = 0, weapon: Weapon = None, image_file: str=IMAGE):

        super().__init__(surface=surface, sprite_group=sprite_group, 
                         position=position, size=size, speed=speed, hp=hp,
                         image_file=image_file, wall_sprites=wall_sprites)
        
        self.energy = energy
        self.gold = gold
        self.score = score

        if self.weapon is None:
            self.weapon = Weapon(self.surface, sprite_group, (self.x, self.y),
                                 (60, 30), 5, bullet_speed=5, fire_rate=150)
