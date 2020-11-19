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
        coordsBullet = []

        # ver trajetória
        x_final, y_final = pygame.mouse.get_pos()

        # linear coefficient
        m = (y_final - self.rect.top) / (x_final - self.rect.left)

        var = -1 if self.rect.top > y_final else 1

        for i in range(self.rect.top, y_final + (1000 * var), var * self.speed):
            y_next = i
            x_next = ((y_next - self.rect.top) / m) + self.rect.left

            coordsBullet.append((x_next, y_next))

        bullet = Bullet(self.surface, (self.rect.left, self.rect.top), (6, 6), self.image_bullet, self.damage, 2, coordsBullet)
        self.bullets.append(bullet)

    def change_image_bullet(self, image_bullet: str):
        self.image_bullet = image_bullet

    def change_damage(self, damage: int):
        self.damage = damage
 
    def update(self):
        for k, bullet in enumerate(self.bullets):
            if bullet.rect.left == 0 or bullet.rect.top == 0 or bullet.rect.left == 800 or bullet.rect.top == 600:
                self.bullets.pop(k)
            else:
                bullet.draw()