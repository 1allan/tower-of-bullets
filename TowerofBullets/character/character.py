import pygame

from entity import Entity


class Character(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, hp: int, image_file: str):
                 
        super().__init__(surface, position, size, speed, image_file)
        self.weapon = None
        self.hp = hp

    def shoot(self):
        pass

    def interact(self):
        pass

    def get_hit(self): #be_hit
        pass
    
    def die(self):
        pass

    def update(self):
        self.weapon.draw()
        self.weapon.rect.left = self.x
        self.weapon.rect.top = self.y