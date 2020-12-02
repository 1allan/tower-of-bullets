import os
import pygame

from abc import ABC, abstractmethod
from util.functions import load_image


class Tile(pygame.sprite.Sprite):

    def __init__(self, position, size, collidable=False, image_file=''):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.width, self.height = self.size
        self.image = load_image(image_file, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.collidable = collidable


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
        

        self.walkablePad = [14, 14, 780, 553]  # pode andar
        self.pads = [
            pygame.Rect(0, 0, 14, 600),
            pygame.Rect(0, 30, 800, 14),
            pygame.Rect(786, 0, 14, 600),
            pygame.Rect(0, 560, 800, 42)
        ]


    def __load_layout(self, path):
        file_ = open(os.path.join(os.path.dirname(__file__),
                                  '../assets/scenery/layouts/' + path), 'r')
        layout = file_.read()
        file_.close()
        matrix = []
        for line in layout.split('\n'):
            matrix.append(line.split(' '))
            print(line.split(' '))

        return matrix

    def generate_layout(self):
        w = round(self.width/len(self.layout[0]))
        h = round(self.height/len(self.layout))

        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                image = 'scenery/'
                if self.layout[i][j] == '1':
                    image += 'wall.png'
                else:
                    image += 'floor.png'

                self.tiles.add(Tile((w * i, h * j), (w, h), image_file=image))

    def update(self):
        pass

    def draw(self):
        # self.surface.blit(self.image, (self.rect.left, self.rect.top))
        self.tiles.draw()
        self.update()
