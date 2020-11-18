import pygame

from items.bullet import Bullet
from entity import Entity

class Weapon(Entity):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, speed: int, image_weapon: str, image_bullet: str, damage: int):
        super().__init__(surface, position, size, speed, image_weapon)
        self.image_bullet = image_bullet
        self.damage = damage
        self.bullets = []

    def shoot(self):
        self.bullets.append(Bullet(self.surface, (self.rect.left, self.rect.top), (6, 6), self.image_bullet, self.damage, 2))

    def change_image_bullet(self, image_bullet: str):
        self.image_bullet = image_bullet

    def change_damage(self, damage: int):
        self.damage = damage
 
    def update(self):
        for b in self.bullets:
            b.shoot()