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
                 args, layout_file='2.txt'):
        pygame.sprite.Sprite.__init__(self)

        self.structure = args['STRUCTURE']
        self.waves = args['WAVES']

        self.width, self.height = size
        self.surface = surface
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.rect.left, self.rect.top = position
        self.layout = self.__load_layout(layout_file)
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
                group = self.wall_sprites

                if self.layout[i][j] == '1':
                    image = 'scenery/wall.png'
                    collidable = True
                else:
                    image = 'scenery/floor.png'
                    group = self.floor_sprites
                
                group.add(Tile(self.surface, (w * i, h * j), (w, h), 
                               collidable, image_file=image))
                    
    def update(self):
        pass

    def draw(self):
        self.wall_sprites.draw(self.surface)
        self.floor_sprites.draw(self.surface)
        self.update()
