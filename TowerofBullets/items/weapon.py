import pygame
import math

from items.bullet import Bullet
from entity import Entity

IMAGE = 'items/01.png'


class Weapon(Entity):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 damage: int, image_file: str=IMAGE):

        super().__init__(surface, position, size, image_file=image_file)
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
                        self.damage, 5, (x_ratio, y_ratio))
        self.bullets.append(bullet)
 
    def update(self):
        print(len(self.bullets))
        for b in self.bullets:
            width, height = b.surface.get_size()
            x, y = b.rect.left, b.rect.top
            if y <= 40 or y >= height - 49 or x <= 14 or x >= width - 15:
                self.bullets.remove(b)
            else:
                b.draw()