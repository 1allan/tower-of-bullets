from scenery.scenario import Scenario
import pygame

class Room(Scenario):
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, image_path: str,
                     enemies: int, traps: int, chest: bool):
        super().__init__(surface, position, size, image_path)
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
        pass
    
    def draw(self):
        self.update()
        self.surface.blit(self.background, (self.x, self.y))





