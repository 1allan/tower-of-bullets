import os
import math
import pygame

from util.functions import load_image

class Entity(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int=0, image_file: str='misc/placeholder.png',  animated=False, animation_duration=1000):

        pygame.sprite.Sprite.__init__(self)

        self.surface = surface

        self.size = size
        self.width, self.height = self.size
        self.animated = animated
        self.image = None
        self.imageset = None
        if self.animated:
            self.imageset = self.__load_imageset(image_file)
            self.image = self.imageset[0]
            self.image_count = 0
            self.image_time = animation_duration / len(self.imageset)
            self.image_last_change = pygame.time.get_ticks()
        else:
            self.image = load_image(image_file, self.size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.speed = speed
    
    def __load_imageset(self, path):
        output = []
        a = os.path.dirname(__file__)
        for image in os.listdir(f'{os.path.dirname(__file__)}/assets/{path}'):
            output.append(load_image(path + image, self.size))
        return output
    
    def animate(self):
        tick = pygame.time.get_ticks()
        if tick - self.image_last_change >= self.image_time:
            self.image_count += 1
            if self.image_count >= len(self.imageset):
                self.image_count = 0
            self.image_last_change = tick

        self.image = self.imageset[self.image_count]

    def update(self):
        pass

    def draw(self):
        if self.animated:
            self.animate()

        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.surface.blit(self.image, (self.rect.left, self.rect.top))
        self.update()