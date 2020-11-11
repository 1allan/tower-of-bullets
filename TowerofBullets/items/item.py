import pygame

from entity import Entity


class Item(Entity):
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 image_file, speed=0):
        super().__init__(surface, position, size, speed, image_file)
        self.function = None

    def update(self):
        self.surface.blit(self.image, (self.x, self.y))
