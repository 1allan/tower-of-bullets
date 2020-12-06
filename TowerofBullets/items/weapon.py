import pygame
import math

from items.bullet import Bullet
from entity import Entity


class Weapon(Entity):

    def __init__(self, surface: pygame.Surface, 
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, args):

        super().__init__(surface, position, size, 
                         image_file=args['IMAGE_FILE'])
        
        self.damage = args['DAMAGE']
        self.fire_rate = args['FIRE_RATE']
        self.bullet_speed = args['BULLET_SPEED']
        self.cost = args['COST']
        self.last_tick = 0
        self.sprite_group = sprite_group
        
    def shoot(self, coordinates: tuple):
        if pygame.time.get_ticks() - self.last_tick >= self.fire_rate:
            self.last_tick = pygame.time.get_ticks()

            position = (self.x - 5, self.y - 10)
            bullet = Bullet(self.surface, position, (8, 8), self.damage, 
                            self.bullet_speed, coordinates)
            
            return bullet
