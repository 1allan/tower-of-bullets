import pygame
import math

from items.bullet import Bullet
from entity import Entity

IMAGE = 'items/01.png'


class Weapon(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 damage: int, image_file: str = IMAGE):

        super().__init__(surface, position, size, image_file=image_file)
        self.damage = damage
        self.bullets = []
        self.last_tick = 0
        self.fire_rate_gap = 1000

    def shoot(self, coordinates):
        x_mouse, y_mouse = coordinates
        x_player, y_player = self.rect.left, self.rect.top

        if pygame.time.get_ticks() - self.last_tick >= self.fire_rate_gap:
            self.last_tick = pygame.time.get_ticks()
            bullet = Bullet(self.surface, (x_player, y_player), (6, 6),
                            self.damage, 5, (x_mouse, y_mouse))
            self.bullets.append(bullet)

    def update(self):
        for b in self.bullets:
            width, height = b.surface.get_size()
            x, y = b.rect.left, b.rect.top
            if y <= 40 or y >= height - 49 or x <= 14 or x >= width - 15:
                self.bullets.remove(b)
            else:
                b.draw()
