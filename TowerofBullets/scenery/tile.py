import pygame

from util.functions import load_image

class Tile(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position, size, collidable, image_file: str, convert=True):
        pygame.sprite.Sprite.__init__(self)

        self.surface = surface
        self.size = size
        self.width, self.height = self.size
        self.image = load_image('scenery/' + image_file, size, convert=convert)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.collidable = collidable

