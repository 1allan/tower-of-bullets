from scenario import Scenario
import pygame


class Room(Scenario):
    def __init__(self, position: tuple, size: tuple, structure: str,
                     enemies: int, traps: int, chest: bool):
        super().__init__(position, size, structure)
        self.enemies = enemies
        self.traps = traps
        self.chest = chest

    def lock_doors(self):
        pass

    def spawn_enemies(self):
        pass

    def check_enemies(self):
        pass

    def open_doors(self):
        pass

    def update(self):
        self.surface.blit(self.image, (self.x, self.y))
