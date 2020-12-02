import pygame
from random import randint

from character.enemy import Enemy
from scenery.scenario import Scenario
from items.item import Item

IMAGE = 'scenery/01.png'


class Room(Scenario):

    def __init__(self, surface: pygame.Surface, sprite_group, position: tuple, size: tuple,
                 traps: int, chest: bool, player, image_path: str=IMAGE):
        
        super().__init__(surface, position, size, traps, chest, image_path)
        self.enemies = pygame.sprite.Group()
        self.traps = traps
        self.chest = chest
        self.player = player
        self.sprite_group = sprite_group
        self.coins = pygame.sprite.Group()

    def lock_doors(self):
        pass

    def spawn_enemies(self, quantity):
        for _ in range(quantity):
            position = randint(15, self.width - 20), randint(30, self.height - 50)
            self.enemies.add(Enemy(self.surface, self.sprite_group, position, (70, 70), 1, 100))
            self.sprite_group.add(self.enemies)
    
    def spawn_coins(self, quantity):
        image_file = "items/coin.png"

        for _ in range(quantity):
            position = randint(15, self.width - 20), randint(30, self.height - 50)
            self.coins.add(Item(self.surface, position, (20, 20), image_file, 0)) 
            self.sprite_group.add(self.coins)

    def check_enemies(self):
        pass

    def open_doors(self):
        pass

    def update(self):
        if len(self.enemies) == 0:
            self.spawn_enemies(1)

        for enemy in self.enemies:
            enemy.shoot((self.player.x, self.player.y))
            enemy.draw()
        if len(self.coins) == 0:
            self.spawn_coins(1)