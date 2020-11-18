import os
import pygame

def load_image(path, size, convert=False):
        image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets/' + path))
        if convert:
            image = image.convert()
        
        return pygame.transform.scale(image, size)