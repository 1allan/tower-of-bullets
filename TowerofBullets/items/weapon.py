import pygame
import math

from items.bullet import Bullet
from entity import Entity

IMAGE = 'items/weapon.png'


class Weapon(Entity):

    def __init__(self, surface: pygame.Surface, sprite_group, position: tuple, size: tuple,
                 damage: int, fire_rate: int=500, image_file: str = IMAGE):

        super().__init__(surface, position, size, image_file=image_file)
        self.damage = damage
        self.bullets = pygame.sprite.Group()
        self.last_tick = 0
        self.fire_rate = fire_rate
        self.sprite_group = sprite_group
        

    def shoot(self, coordinates):
        if pygame.time.get_ticks() - self.last_tick >= self.fire_rate:
            self.last_tick = pygame.time.get_ticks()

            position = (self.x, self.y)
            bullet = Bullet(self.surface, position, (6, 6), self.damage, 1,
                            coordinates)
            
            self.bullets.add(bullet)
            self.sprite_group.add(self.bullets)

    def update(self):
        for b in self.bullets:
            width, height = b.surface.get_size()
            x, y = b.rect.left, b.rect.top
            if y <= 40 or y >= height - 49 or x <= 14 or x >= width - 15:
                self.bullets.remove(b)
            else:
                b.draw()
