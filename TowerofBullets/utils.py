import os
import pygame

def load_image(path, size, convert=False):
    relative_path = os.path.join(os.path.dirname(__file__)
    image = pygame.image.load(relative_path, 'assets/' + path))
    if convert:
        image = image.convert()
    
    return pygame.transform.scale(image, size)