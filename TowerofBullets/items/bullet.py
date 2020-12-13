import math
import pygame

from entity import Entity
from util.functions import load_image


class BulletType:

    def __init__(self, immutable_state):
        self.immutable_state = immutable_state
    
    def __getitem__(self, key):
        return self.immutable_state[key]


class BulletFactory:

    bulletTypes = []

    def get_bullet_type(immutable_state):
        bulletTypes = BulletFactory.bulletTypes
        cached_types = [t.immutable_state for t in bulletTypes]

        if immutable_state not in cached_types:
            b_type = BulletType(immutable_state)
            bulletTypes.append(b_type)
            return b_type
        else:
            return bulletTypes[cached_types.index(immutable_state)]


class Bullet(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, destination, b_type):
                 
        super().__init__(surface, position, b_type['SIZE'], speed=b_type['SPEED'],
                         image_file='projectiles/' + b_type['IMAGE_FILE'])

        self.damage = b_type['DAMAGE']
        self.__floating_point_x, self.__floating_point_y = position
        self.__dest_x, self.__dest_y = destination

        x_diff = self.__dest_x - self.rect.left
        y_diff = self.__dest_y - self.rect.top
        angle = math.atan2(y_diff, x_diff)

        self.__change_x = math.cos(angle) * int(self.speed)
        self.__change_y = math.sin(angle) * int(self.speed)

    def update(self):
        self.__floating_point_y += self.__change_y
        self.__floating_point_x += self.__change_x
        
        self.rect.left = int(self.__floating_point_x)
        self.rect.top = int(self.__floating_point_y)

        