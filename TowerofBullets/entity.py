import os
import math
import pygame

from util.functions import load_image

class Entity:

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int=0, image_file: str='placeholder.png'):

        self.surface = surface
        self.size = size
        self.width, self.height = self.size
        self.image = load_image(image_file, self.size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.speed = speed


    def update(self):
        pass

    def draw(self):
        self.surface.blit(self.image, (self.rect.left, self.rect.top))
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.update()