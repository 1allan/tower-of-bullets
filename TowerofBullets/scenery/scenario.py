import pygame

from abc import ABC, abstractmethod
from util.functions import load_image


class Scenario(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 traps: int, chest: bool, image_path: str):
        pygame.sprite.Sprite.__init__(self)

        self.width, self.height = size
        self.surface = surface
        self.image = load_image(image_path, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

        self.walkablePad = [14, 14, 780, 553] # pode andar
        self.pads = [
            pygame.Rect(0, 0, 14, 600),
            pygame.Rect(0, 30, 800, 14),
            pygame.Rect(786, 0, 14, 600),
            pygame.Rect(0, 560, 800, 42)
        ]

    def update(self):
        pass
        
    def draw(self):
        self.surface.blit(self.image, (self.rect.left, self.rect.top))
        self.update()
