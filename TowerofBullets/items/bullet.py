import pygame

from entity import Entity


class Bullet(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 image_file: str, count: int, damage: int, speed: int = 0):
        super().__init__(surface, position, size, speed=speed, 
                         image_file=image_file)
        self.count = count
        self.damage = damage

    def travel(self):
        pass

    def hit(self):
        pass

    def update(self):
        self.surface.blit(self.image, (self.x, self.y))