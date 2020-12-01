import pygame


class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple):
        pygame.sprite.Sprite.__init__(self)
