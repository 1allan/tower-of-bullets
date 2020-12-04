import os
import pygame

from abc import ABC, abstractmethod
from util.functions import load_image


class Tile(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position, size, collidable, image_file: str):
        pygame.sprite.Sprite.__init__(self)

        self.surface = surface
        self.size = size
        self.width, self.height = self.size
        self.image = load_image(image_file, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.collidable = collidable

    def draw(self):
        self.surface.blit(self.image, (self.rect.left, self.rect.top))

class Scenario(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 traps: int, chest: bool, image_path: str, layout_path='1.txt'):
        pygame.sprite.Sprite.__init__(self)

        self.width, self.height = size
        self.surface = surface
        self.image = load_image(image_path, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.layout = self.__load_layout(layout_path)
        self.floor_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.generate_layout()

    def __load_layout(self, path):
        file_ = open(os.path.join(os.path.dirname(__file__),
                                  '../assets/scenery/layouts/' + path), 'r')
        layout = file_.read()
        file_.close()
        matrix = []
        for line in layout.split('\n'):
            matrix.append(line.split(' '))

        return matrix

    def generate_layout(self):
        w = round(self.width/len(self.layout[0]))
        h = round(self.height/len(self.layout))

        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                image = 'scenery/01.png'
                collidable = False

                if self.layout[i][j] == '1':
                    img_wall = 'scenery/wall.png'
                    collidable = True
                    self.wall_sprites.add(Tile(self.surface, (w * i, h * j), (w, h),
                                                 collidable,image_file=img_wall))
                else:
                    img_floor = 'scenery/floor.png'
                    self.floor_sprites.add(Tile(self.surface, (w * i, h * j), (w, h),
                                                 collidable, image_file=img_floor))
                    
    def update(self):
        pass

    def draw(self):
        self.wall_sprites.draw(self.surface)
        self.floor_sprites.draw(self.surface)
        self.update()
