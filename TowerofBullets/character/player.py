import pygame

from character.character import *
from items.weapon import *
from utils import *


class Player(Character):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed:int, image_file: str, hp: int, energy: int, gold: int=0,
                 weapon: Weapon=None):
        super().__init__(surface, position, size, speed, image_file, hp)
        self.energy = energy
        self.gold = gold
        self.weapon = None if weapon is None else weapon # arrumar Weapon depois => self.weapon = Weapon(bla.bla.bla)

    def change_weapon(self,weapon: Weapon):
        self.weapon = weapon

    def shoot(self):
        print('shoot')

        bullet = load_image('characters/player/bullets/plain/01.png', (6, 6))
        aim_x, aim_y = pygame.mouse.get_pos()
        bullet_x, bullet_y = (self.rect.left, self.rect.top)
        bullet_inclination = (aim_y - bullet_y) / (aim_x - bullet_x)
        
        
        print(f'aim_x = {aim_x} / aim_y = {aim_y}')
        print(f'bullet_inclination = {bullet_inclination}')

        self.surface.blit(bullet, (aim_x, aim_y))

        # while True:
        #     self.surface.blit(bullet, (bullet_x, bullet_y))
        #     bullet_x += 1
        #     bullet_y += 1
        #     if bullet_x == aim_x and bullet_y == aim_y:
        #         break