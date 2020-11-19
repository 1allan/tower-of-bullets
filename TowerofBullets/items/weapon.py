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
        coordsBullet = []

        # ver trajetória
        x_final, y_final = pygame.mouse.get_pos()

        # angular coefficient
        m = (y_final - self.rect.top) / (x_final - self.rect.left)
        anguloRad = math.atan(m)
        anguloGraus = math.degrees(anguloRad)
        seno = math.sin(anguloRad)
        cosseno = math.cos(anguloRad)

        print(f'angulo graus = {anguloGraus}')
        # print(f'tangente = {m}')
        # print(f'seno = {seno}')
        # print(f'cosseno = {cosseno}')

        var = -1 if self.rect.top > y_final else 1

        i = self.rect.top
        while i < (y_final + (1000 * var)) if var == 1 else i > (y_final + (1000 * var)):
            y_next = i
            x_next = ((y_next - self.rect.top) / m) + self.rect.left

            coordsBullet.append((x_next, y_next))
            i += var / 10

        # for i in range(self.rect.top, y_final + (1000 * var), var):
            # y_next = i
            # x_next = ((y_next - self.rect.top) / m) + self.rect.left

            # coordsBullet.append((x_next, y_next))

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