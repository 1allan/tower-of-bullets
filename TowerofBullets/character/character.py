import pygame

from entity import Entity


class Character(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, image_file: str, hp: int):
        super().__init__(surface, position, size, speed, image_file)
        self.hp = hp
    
    def move(self,x,y):
        pass

    def shoot(self):
        pass

    def interact(self):
        pass

    def get_hit(self): #be_hit
        pass
    
    def die(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.update()
        self.surface.blit(self.image, (self.x, self.y))