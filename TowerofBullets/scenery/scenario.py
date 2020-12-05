import os
import pygame

from abc import ABC, abstractmethod
from random import randint, choice
from util.functions import load_image
from character.enemy import Enemy


class Tile(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position, size, collidable, image_file: str):
        pygame.sprite.Sprite.__init__(self)

        self.surface = surface
        self.size = size
        self.width, self.height = self.size
        self.image = load_image('scenery/' + image_file, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2
        self.collidable = collidable

    def draw(self):
        self.surface.blit(self.image, (self.rect.left, self.rect.top))

class Scenario(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, sprite_group: pygame.sprite.Group,
                 args):
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
        self.layout = self.__load_layout(self.structure['LAYOUT'])
        self.floor_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.generate_layout()
        self.start_wave()

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
            for j in range(len(self.layout[i]) - 1):
                collidable = False
                group = self.wall_sprites

                image = ''
                if self.layout[i][j].startswith('wall'):
                    collidable = True
                    image = 'walls/' + self.layout[i][j]
                else:
                    image = 'floors/' + self.layout[i][j]
                    group = self.floor_sprites

                group.add(Tile(self.surface, (w * i, h * j), (w, h), 
                               collidable, image_file=image))

    def start_wave(self):
        for i in range(self.waves[self.wave_now]['AMOUNT']):
            enemy_type = choice(self.waves[self.wave_now]['ENEMIES'])
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.enemies.add(Enemy(self.surface, self.sprite_group, position, (70, 70), self.wall_sprites, enemy_type))
        self.wave_now += 1
    
    def draw(self):
        self.wall_sprites.draw(self.surface)
        self.floor_sprites.draw(self.surface)
        self.update()
