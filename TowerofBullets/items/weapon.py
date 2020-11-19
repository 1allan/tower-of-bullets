import pygame
import math

from items.bullet import Bullet
from entity import Entity

class Weapon(Entity):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, speed: int, image_weapon: str, image_bullet: str, damage: int):
        super().__init__(surface, position, size, speed, image_weapon)
        self.image_bullet = image_bullet
        self.damage = damage
        self.bullets = []

    def shoot(self):
        x_final, y_final = pygame.mouse.get_pos()
        hip = ((y_final - self.rect.top)**2 + (x_final - self.rect.left)**2)**.5
        
        x_ratio = (max(x_final, self.rect.left) - min(x_final, self.rect.left))/hip
        y_ratio = (max(y_final, self.rect.top) - min(y_final, self.rect.top))/hip

        y_ratio = -y_ratio if y_final < self.rect.top else y_ratio
        x_ratio = -x_ratio if x_final < self.rect.left else x_ratio

        bullet = Bullet(self.surface, (x_ratio, y_ratio), (self.rect.left, self.rect.top), (6, 6), self.image_bullet, self.damage, 5)
        self.bullets.append(bullet)

    def change_image_bullet(self, image_bullet: str):
        self.image_bullet = image_bullet

    def change_damage(self, damage: int):
        self.damage = damage
 
    def update(self):
        for b in self.bullets:
            width, height = b.surface.get_size()
            if b.rect.top < 0 or b.rect.top > height or b.rect.left < 0 or b.rect.left > width:
                self.bullets.remove(b)
            else:
                b.draw()