import pygame
from random import randint

from character.enemy import Enemy
from scenery.scenario import Scenario

IMAGE = 'scenery/01.png'


class Room(Scenario):
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 traps: int, chest: bool, image_path: str=IMAGE):
        
        super().__init__(surface, position, size, traps, chest, image_path)
        self.enemies = []
        self.traps = traps
        self.chest = chest

    def lock_doors(self):
        pass

    def spawn_enemies(self, quantity):
        
        for _ in range(quantity):
            position = randint(0, self.width), randint(0, self.height)
            self.enemies.append(Enemy(self.surface, position, (30, 30), 0, 0))

    def check_enemies(self):
        pass

    def open_doors(self):
        pass

    def update(self, player_coordinates):
        if len(self.enemies) < 1:
            self.spawn_enemies(1)
        
        for enemy in self.enemies:
            enemy.shoot(player_coordinates)
            enemy.draw() 






