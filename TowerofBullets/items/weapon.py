import pygame
import math

from items.bullet import Bullet
from entity import Entity

class Weapon(Entity):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, image_weapon: str, image_bullet: str,
                 damage: int):

        super().__init__(surface, position, size, speed, image_weapon)
        self.image_bullet = image_bullet
        self.damage = damage
        self.bullets = []

    def shoot(self):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        x_player, y_player = self.rect.left, self.rect.top
        distance = ((y_mouse - y_player)**2 + (x_mouse - x_player)**2) ** 0.5
        
        x_ratio = abs(x_mouse - x_player) / distance
        y_ratio = abs(y_mouse - y_player) / distance

        y_ratio *= -1 if y_mouse < y_player else 1
        x_ratio *= -1 if x_mouse < x_player else 1

        bullet = Bullet(self.surface, (x_player, y_player), (6, 6), 
                        self.image_bullet, self.damage, 5, (x_ratio, y_ratio))
        self.bullets.append(bullet)

    def change_image_bullet(self, image_bullet: str):
        self.image_bullet = image_bullet

    def change_damage(self, damage: int):
        self.damage = damage
 
    def update(self):
        for b in self.bullets:
            width, height = b.surface.get_size()
            x, y = b.rect.left, b.rect.top
            if y < 0 or y > height or x < 0 or x > width:
                self.bullets.remove(b)
            else:
                b.draw()