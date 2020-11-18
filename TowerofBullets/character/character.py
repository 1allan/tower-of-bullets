import pygame

from entity import Entity

RED = pygame.Color(255, 0, 0)

class Character(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, image_file: str, hp: int):
        super().__init__(surface, position, size, speed, image_file)
        self.hp = hp

    def shoot(self):
        pass


    def interact(self):
        pass

    def get_hit(self): #be_hit
        pass
    
    def die(self):
        pass