import math
import pygame

from util.functions import load_image
from util.constants import WEAPONS_DB
from character.character import Character
from items.weapon import Weapon
from items.bullet import Bullet

IMAGE = 'misc/placeholder.png'


class Player(Character):

    def __init__(self, surface: pygame.Surface, 
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, speed: int, hp: int, energy: int, 
                 wall_sprites: pygame.sprite.Group, gold: int = 0,
                 score: int = 0, image_file: str=IMAGE):

        super().__init__(surface=surface, sprite_group=sprite_group, 
                         position=position, size=size, speed=speed, hp=hp,
                         image_file=image_file, wall_sprites=wall_sprites)
        
        self.energy = energy
        self.gold = gold
        self.score = score
        self.last_weapon_change = 0
        self.weapon2 = Weapon(self.surface, sprite_group, (self.x, self.y), 
                              (80, 80), WEAPONS_DB['CAULE'])

        self.weapon = Weapon(self.surface, sprite_group, (self.x, self.y), 
                             (80, 80), WEAPONS_DB['AK47'])
        

    def swap_weapons(self):
        current_tick = pygame.time.get_ticks()
        if current_tick - self.last_weapon_change > 300:
            self.last_weapon_change = current_tick
            self.weapon, self.weapon2 = self.weapon2, self.weapon