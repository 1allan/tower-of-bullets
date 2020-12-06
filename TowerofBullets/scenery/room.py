import pygame

from random import randint, choice

from character.enemy import Enemy
from character.player import Player
from scenery.scenario import Scenario
from items.item import Item


class Room(Scenario):

    def __init__(self, surface: pygame.Surface,
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, args):

        super().__init__(surface, position, size, sprite_group, args)

        # self.enemies = pygame.sprite.Group()
        self.wave_timeout = False
        self.coins = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.last_wave = 0
        self.player = Player(self.surface, self.sprite_group, 
                            (size[0]/2, size[1]/2-10), (70, 70), 3, 20, 200, 
                             self.walls, gold=0)

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

    def update(self):

        self.enemy_bullets.update()
        if (len(self.enemies) == 0 and 
            self.wave_now <= self.waves[self.wave_now]["AMOUNT"] and 
            not self.wave_timeout):

            self.wave_timeout = True
            self.last_wave = pygame.time.get_ticks()
            self.spawn_coins(2)
            self.spawn_hearts(1)

        elif (len(self.enemies) == 0 and 
            self.wave_now > self.waves[self.wave_now]["AMOUNT"]):
            
            # handle carinha passou de nível
            print('carinha passou de nível')
            self.spawn_portal()

        # wave_timeout between waves
        if (self.wave_timeout and 
            pygame.time.get_ticks() - self.last_wave > 3000):

            self.wave_timeout = False
            self.last_wave = pygame.time.get_ticks()
            self.start_wave()

        for enemy in self.enemies:
            bullet = enemy.attack((self.player.x, self.player.y))
            if bullet is not None:
                self.enemy_bullets.add(bullet)
            enemy.chase((self.player.x, self.player.y))
            enemy.draw()
        

    def draw(self):
        self.floors.draw(self.surface)
        self.enemy_bullets.draw(self.surface)
        self.walls.draw(self.surface)
        self.player.draw()
        self.update()