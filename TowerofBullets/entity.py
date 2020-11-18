import os
import math

import pygame
from utils import *

class Entity:

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, speed=0, image_file='placeholder.png'):
        self.surface = surface
        self.size = size
        self.width, self.height = self.size
        self.image = load_image(image_file, self.size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = self.rect.left - self.width/2 # meio do personagem
        self.y = self.rect.top - self.width/2 # meio do personagem
        self.rect.center = (self.x + self.width/2, self.y + self.height/2)
        self.speed = speed

    def move(self, direction=None):
        self.speed *= math.ceil((direction[0]**2 + direction[1]**2)**.5 / 2)
        self.rect.left += self.speed * direction[0]
        self.rect.top += self.speed * direction[1]

    def update(self):
        pass

    def draw(self):
        self.update()
        self.surface.blit(self.image, (self.rect.left, self.rect.top))