import os
import math
import pygame

from utils import load_image

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
        self.y = self.rect.top + self.width/2
        self.speed = speed

    def move(self, direction=None):
        speed = self.speed
        # Sets an equivalent speed for diagonals
        if 0 not in direction:
            speed = round(((speed**2 + speed**2)**0.5)/2, 1)
        
        self.rect.left += speed * direction[0]
        self.rect.top += speed * direction[1]

    def update(self):
        pass

    def draw(self):
        self.update()
        self.surface.blit(self.image, (self.rect.left, self.rect.top))