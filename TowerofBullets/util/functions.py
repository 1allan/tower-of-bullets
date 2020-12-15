import os
import pygame


def load_image(path, size, convert=False):
    path = os.path.join(os.path.dirname(__file__), '../assets/' + path)
    image = pygame.image.load(path)
    if convert:
        image = image.convert()
    else: 
        image = image.convert_alpha() 

    return pygame.transform.scale(image, size)
