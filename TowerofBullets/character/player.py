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
                 size: tuple, speed: int, max_hp: int, max_energy: int, 
                 wall_sprites: pygame.sprite.Group, gold: int = 0, image_file: str=IMAGE):

        super().__init__(surface, sprite_group, position, size, speed, max_hp, 
                         wall_sprites, image_file)
        
        self.max_energy = max_energy
        self.energy = self.max_energy
        self.gold = gold
        self.last_weapon_change = 0
        self.weapon2 = Weapon(self.surface, sprite_group, (self.x, self.y),
                              WEAPONS_DB['CAULE'])

        self.weapon = Weapon(self.surface, sprite_group, (self.x, self.y), 
                             WEAPONS_DB['AK47'])
        
    def attack(self, coordinates: tuple=None):
        if coordinates is not None and self.energy - self.weapon.cost >= 0:
            bullet = self.weapon.shoot(coordinates)
            if bullet is not None:
                self.bullets.add(bullet)
                self.energy -= self.weapon.cost
                return bullet

    def swap_weapons(self):
        current_tick = pygame.time.get_ticks()
        if current_tick - self.last_weapon_change > 300:
            self.last_weapon_change = current_tick
            self.weapon, self.weapon2 = self.weapon2, self.weapon