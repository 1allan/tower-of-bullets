import pygame
import math

from entity import Entity
from items.weapon import Weapon
from character.character import Character
from character.player import Player

IMAGE = 'characters/01.png'

class Enemy(Character):

    def __init__(self, surface: pygame.Surface, 
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, wall_sprites, args):

        # speed, hp, weapon, image_file
        super().__init__(surface, sprite_group, position, size, args["SPEED"], args["HP"], args["IMAGE_FILE"], wall_sprites=wall_sprites)

        self.weapon = Weapon(self.surface, sprite_group, (self.rect.left, self.rect.top), (20, 10), args["WEAPON"]["DAMAGE"], args["WEAPON"]["IMAGE_FILE"])
        self.sprite_group.add(self.weapon)
        
        # if self.weapon is None:
        #     self.weapon = Weapon(self.surface, sprite_group, 
        #                         (self.rect.left, self.rect.top), (20, 10), self.damage)
        #     self.sprite_group.add(self.weapon)

    def chase(self, destination: tuple, flag = False):
        self.floating_point_x, self.floating_point_y = [self.rect.left, self.rect.top]
        self.dest_x, self.dest_y = destination

        x_diff = self.dest_x - self.rect.left
        y_diff = self.dest_y - self.rect.top
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed

        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        positionBefore = (self.rect.left, self.rect.top)
        collision = pygame.sprite.spritecollideany(self, self.wall_sprites)

        # colisao com parede
        if collision:
            self.rect.left = positionBefore[0] - 1
            self.rect.top = positionBefore[1] - 1
        else:
            self.rect.left = int(self.floating_point_x)
            self.rect.top = int(self.floating_point_y)

    def shoot(self, coordinates: tuple):
        self.weapon.shoot(coordinates)
        