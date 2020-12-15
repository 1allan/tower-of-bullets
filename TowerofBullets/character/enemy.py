import pygame
import math

from entity import Entity
from items.weapon import Weapon
from character.character import Character
from character.player import Player


class Enemy(Character):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 wall_sprites, args, animated=False):

        super().__init__(surface, position, size,
                         args["SPEED"], args["HP"], wall_sprites, 
                         'characters/enemies/' + args["IMAGE_FILE"], animated)

        self.weapon = Weapon(self.surface, (self.rect.left, self.rect.top), 
                             args["WEAPON"])
        self.weapon.cost = 0
        self.inv_time = 0

    def chase(self, destination: tuple, flag=False):
        self.floating_point_x, self.floating_point_y = [
            self.rect.left, self.rect.top]
        self.dest_x, self.dest_y = destination

        x_diff = self.dest_x - self.rect.left
        y_diff = self.dest_y - self.rect.top
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * int(self.speed)
        self.change_y = math.sin(angle) * int(self.speed)

        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        positionBefore = (self.rect.left, self.rect.top)
        collision = pygame.sprite.spritecollideany(self, self.wall_sprites)

        # colisao com parede
        if collision:
            self.rect.left = positionBefore[0] - 2
            self.rect.top = positionBefore[1] - 2
        else:
            self.rect.left = int(self.floating_point_x)
            self.rect.top = int(self.floating_point_y)

