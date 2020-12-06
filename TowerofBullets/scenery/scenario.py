import os
import pygame

from abc import ABC, abstractmethod
from random import randint, choice
from util.functions import load_image
from character.enemy import Enemy


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


class Scenario(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 sprite_group: pygame.sprite.Group, args):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_group = sprite_group
        self.structure = args['STRUCTURE']
        self.waves = args['WAVES']
        self.wave_now = 0
        self.amount_enemies = self.waves[self.wave_now]["AMOUNT"]
        self.enemies = pygame.sprite.Group()

        self.width, self.height = size
        self.surface = surface
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.rect.left, self.rect.top = position
        # self.layout = self.__load_layout(self.structure['LAYOUT'])

        layer1, layer2 = self.__load_layout('fazov.txt')
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.overlay = pygame.sprite.Group()
        self.__generate_layout(layer2, overlay=True, offset=(0, -15))
        self.__generate_layout(layer1)
        self.start_wave()

    def __load_layout(self, path):
        file_ = open(os.path.join(os.path.dirname(__file__),
                                  '../assets/scenery/layouts/' + path), 'r')
        layout = file_.read()
        file_.close()
        output = []
        for i, matrix in enumerate(layout.split('\n=overlay=\n')):
            output.append([])
            for line in matrix.split('\n'):
                output[i].append(line.split(' '))

        return output

    def __generate_layout(self, matrix, overlay=False, offset=None):
        offset = (0, 0) if offset is None else offset
        w = round(self.width/len(matrix[0]))
        h = round(self.height/len(matrix))

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                group = self.walls
                collidable = False
                convert = True
                image = ''

                if matrix[i][j].startswith('wall'):
                    collidable = True
                    image = 'walls/' + matrix[i][j]
                else:
                    image = 'floors/' + matrix[i][j]
                    group = self.floors

                if overlay:
                    group = self.overlay
                    convert = False
                group.add(Tile(self.surface, 
                              (w * i + offset[0], h * j + offset[1]), (w, h), 
                               collidable, image_file=image, convert=convert))

    def start_wave(self):
        for i in range(self.waves[self.wave_now]['AMOUNT']):
            enemy_type = choice(self.waves[self.wave_now]['ENEMIES'])
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.enemies.add(Enemy(self.surface, self.sprite_group, position, 
                            (70, 70), self.walls, enemy_type))
        self.wave_now += 1
    
    def draw(self):
        self.floors.draw(self.surface)
        self.walls.draw(self.surface)
        self.update()
