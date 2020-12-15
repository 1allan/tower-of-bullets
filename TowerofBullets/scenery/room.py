import os
import pygame

from random import randint, choice

from util.functions import load_image

from .tile import Tile
from character.enemy import Enemy
from items.item import Item


class Room(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 args):

        pygame.sprite.Sprite.__init__(self)

        self.width, self.height = size
        self.surface = surface
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        self.player = None
        self.spawn_point = args['SPAWN_POINT']
        self.portal = None

        layer1, layer2 = self.__load_layout(args['STRUCTURE']['LAYOUT'])
        self.overlay = self.__generate_layout(layer2, overlay=True,
                                              offset=(0, -15))
        self.floors, self.walls = self.__generate_layout(layer1)

        self.wave_now = 0
        self.last_wave = pygame.time.get_ticks()
        self.waves = args['WAVES']
        self.started = False
        self.rewarded = False

        self.coins = pygame.sprite.Group()
        self.energy_orbs = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemies_bullets = pygame.sprite.Group()

        self.start_wave()

    def __load_layout(self, path):
        file_ = open(os.path.join(os.path.dirname(__file__),
                                  '../assets/scenery/layouts/' + path), 'r')
        layout = file_.read()
        file_.close()
        output = []
        for i, matrix in enumerate(layout.split('\n\n')):
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
        for i in range(self.waves[self.wave_now]['ENEMY_QUANTITY']):
            enemy_type = choice(self.waves[self.wave_now]['ENEMIES'])
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.enemies.add(Enemy(self.surface, position, (70, 70), 
                                   self.walls, enemy_type, animated=True))
        self.wave_now += 1

    def spawn_portal(self):
        image_file = 'misc/portal.png'

        self.portal = Item(self.surface, self.spawn_point,
                           (32, 64), image_file, 0)

    def spawn_coins(self, quantity: int):
        image_file = "misc/coin.png"

        for _ in range(quantity):
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.coins.add(Item(self.surface, position, (20, 20), image_file,
                                0))

    def spawn_energy_orbs(self, quantity: int):
        image_file = "misc/energy_orb.png"

        for _ in range(quantity):
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.energy_orbs.add(Item(self.surface, position, (20, 20), image_file,
                                      0))

    def spawn_hearts(self, quantity: int):
        image_file = "misc/heart.png"

        for _ in range(quantity):
            chosen = choice(list(self.floors))
            position = (chosen.rect.left, chosen.rect.top)

            self.hearts.add(Item(self.surface, position, (30, 30), image_file,
                                 0))

    def spawn_player(self, player):
        player.rect.left, player.rect.top = self.spawn_point
        self.player = player

    def update(self):
        tick = pygame.time.get_ticks()
        if tick - self.last_wave < 3000 and not self.started:
            return
        else:
            self.started = True
        self.enemies_bullets.update()

        if len(self.enemies) == 0:
            if not self.rewarded:
                self.spawn_hearts(2)
                self.spawn_coins(5)
                self.spawn_energy_orbs(3)
                self.rewarded = True

            if self.wave_now < len(self.waves) and tick - self.last_wave > 3000:
                self.last_wave = tick
                self.rewarded = False
                self.start_wave()
            elif self.wave_now >= len(self.waves) and tick - self.last_wave > 2000:
                self.last_wave = tick
                self.spawn_portal()

        else:
            self.last_wave = pygame.time.get_ticks()

        for enemy in self.enemies:
            bullet = enemy.attack((self.player.x, self.player.y))
            if bullet is not None:
                self.enemies_bullets.add(bullet)
            enemy.chase((self.player.x, self.player.y))
            enemy.weapon.update((self.player.x, self.player.y))
            enemy.draw()

    def draw(self):
        self.floors.draw(self.surface)
        self.hearts.draw(self.surface)
        self.energy_orbs.draw(self.surface)
        self.coins.draw(self.surface)
        if self.portal is not None:
            self.portal.draw()
        self.enemies_bullets.draw(self.surface)
        self.walls.draw(self.surface)
        self.player.draw()
        self.update()
