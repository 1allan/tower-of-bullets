import pygame

from entity import Entity


class Chest(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 image_file: str, speed=0):
        super().__init__(surface, position, size, speed=speed, 
                         image_file=image_file)
        self.items = []

    def get_items(self, item: Items): #confere ai
        self.items.pop(item)
        return item

    def set_items(self,item: Items): #confere ai
        self.items.append(item)

    def update(self):
        self.surface.blit(self.image, (self.x, self.y))
