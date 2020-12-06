import os
import pygame

from random import randint, choice

from util.functions import load_image

from .tile import Tile
from character.enemy import Enemy
from items.item import Item


class Room(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface,
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, args):

        pygame.sprite.Sprite.__init__(self)

        self.sprite_group = sprite_group
        self.width, self.height = size
        self.surface = surface
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.rect.left, self.rect.top = position

        self.player = None
        self.spawn_point = args['SPAWN_POINT']

        layer1, layer2 = self.__load_layout(args['STRUCTURE']['LAYOUT'])
        self.overlay = self.__generate_layout(layer2, overlay=True, 
                                              offset=(0, -15))
        self.floors, self.walls = self.__generate_layout(layer1)
    
        self.wave_now = 0
        self.last_wave = 0
        self.wave_break = False
        self.waves = args['WAVES']
        self.enemies_quantity = self.waves[self.wave_now]['QUANTITY']

        self.coins = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemies_bullets = pygame.sprite.Group()

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
        walls = pygame.sprite.Group()
        floors = pygame.sprite.Group()
        offset = (0, 0) if offset is None else offset
        w = round(self.width/len(matrix[0]))
        h = round(self.height/len(matrix))

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                group = walls
                collidable = False
                convert = not overlay
                image = ''

                if matrix[i][j].startswith('wall'):
                    collidable = True
                    image = 'walls/' + matrix[i][j]
                else:
                    group = floors
                    image = 'floors/' + matrix[i][j]

                group.add(Tile(self.surface, 
                              (w * i + offset[0], h * j + offset[1]), (w, h), 
                               collidable, image_file=image, convert=convert))
        if overlay:
            group = pygame.sprite.Group()
            group.add(floors)
            group.add(walls)
            return group
        else:
            return floors, walls

    def start_wave(self):
        for i in range(self.waves[self.wave_now]['QUANTITY']):
            enemy_type = choice(self.waves[self.wave_now]['ENEMIES'])
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.enemies.add(Enemy(self.surface, self.sprite_group, position, 
                            (70, 70), self.walls, enemy_type))
        self.wave_now += 1

    def spawn_portal(self):
        image_file = 'misc/portal.png'

        chosen = choice(list(self.floors))
        position = (chosen.rect.left, chosen.rect.top)

        self.portal.add(Item(self.surface, position, (32, 64), image_file, 0))

        self.sprite_group.add(self.portal)

    def spawn_coins(self, quantity: int):
        image_file = "items/coin.png"

        for _ in range(quantity):
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.coins.add(Item(self.surface, position, (20, 20), image_file,
                                0))
            self.sprite_group.add(self.coins)

    def spawn_hearts(self, quantity: int):
        image_file = "items/ui_heart_full.png"

        for _ in range(quantity):
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.hearts.add(Item(self.surface, position, (30, 30), image_file,
                                 0))
            self.sprite_group.add(self.hearts)
    
    def spawn_player(self, player):
        player.rect.left, player.rect.top = self.spawn_point
        self.player = player

    def update(self):

        self.enemies_bullets.update()
        if (len(self.enemies) == 0 and 
            self.wave_now <= self.waves[self.wave_now]['QUANTITY'] and 
            not self.wave_break):

            self.wave_break = True
            self.last_wave = pygame.time.get_ticks()
            self.spawn_coins(2)
            self.spawn_hearts(1)

        elif len(self.enemies) == 0 and self.wave_now > self.waves[self.wave_now]["QUANTITY"]:
            if not self.is_portal_spawned:
                self.spawn_portal()
                self.is_portal_spawned = True

        # wave_break between waves
        if (self.wave_break and 
            pygame.time.get_ticks() - self.last_wave > 3000):

            self.wave_break = False
            self.last_wave = pygame.time.get_ticks()
            self.start_wave()

        for enemy in self.enemies:
            bullet = enemy.attack((self.player.x, self.player.y))
            if bullet is not None:
                self.enemies_bullets.add(bullet)
            enemy.chase((self.player.x, self.player.y))
            enemy.draw()
        

    def draw(self):
        self.floors.draw(self.surface)
        self.enemies_bullets.draw(self.surface)
        self.walls.draw(self.surface)
        self.player.draw()
        self.update()