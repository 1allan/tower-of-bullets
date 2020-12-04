import pygame

from entity import Entity


class Chest(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 image_file: str, speed: int=0):
                 
        super().__init__(surface, position, size, speed=speed, 
                         image_file=image_file)
        self.items = pygame.sprite.Group()

    def get_items(self, item: Item):
        self.items.remove(item)
        return item

    def set_items(self,item: Item):
        self.items.add(item)
        