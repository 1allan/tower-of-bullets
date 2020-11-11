import pygame

from entity import Entity


class Chest(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 image_file: str, speed=0):
        super().__init__(surface, position, size, speed=speed, 
                         image_file=image_file)
        self.items = []

    def get_items(self):
        pass

    def set_items(self):
        pass

    def update(self):
        self.surface.blit(self.image, (self.x, self.y))
