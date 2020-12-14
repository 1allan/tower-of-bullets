import pygame
import math

from items.bullet import Bullet, BulletFactory
from entity import Entity


class Weapon(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, args):

        super().__init__(surface, position, args['SIZE'], 
                         image_file='weapons/' + args['IMAGE_FILE'])
        
        self.fire_rate = args['FIRE_RATE']
        self.cost = args['COST']
        self.bullet_args = args['BULLET']
        self.last_tick = 0
        self.rotated_image = None
        
    def shoot(self, coordinates: tuple):
        if pygame.time.get_ticks() - self.last_tick >= self.fire_rate:
            self.last_tick = pygame.time.get_ticks()

            position = (self.rect.left, self.rect.top)
            b_type = BulletFactory.get_bullet_type(self.bullet_args)
            bullet = Bullet(self.surface, position, coordinates, b_type)
            return bullet
    
    def update(self, coordinates):
        radians = math.atan2((coordinates[1] - self.rect.top), 
                             (coordinates[0] - self.rect.left))
        degs = radians * (180 / math.pi)
        image = None
        if coordinates[0] < self.rect.left:
            image = pygame.transform.flip(self.image, False, True)
        else:
            image = self.image

        self.rotated_image = pygame.transform.rotate(image, -degs)

    def draw(self):
        if self.rotated_image is not None:
            new_rect = self.rotated_image.get_rect(center=(self.rect.left, self.rect.top + 20))
            self.surface.blit(self.rotated_image, new_rect)
        else:
            self.surface.blit(self.image, (self.rect.left, self.rect.top))