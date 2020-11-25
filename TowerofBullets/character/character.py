import pygame

from entity import Entity


class Character(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, hp: int, sprite_group, image_file: str):
                 
        super().__init__(surface, position, size, speed, image_file)
        self.weapon = None
        self.hp = hp
        self.sprite_group = sprite_group

    def shoot(self):
        pass

    def interact(self):
        pass

    def be_hit(self, bullet):
        self.hp -= bullet.damage
    
    def die(self):
        pass

    def update(self):
        self.weapon.draw()
        self.weapon.rect.left = self.rect.left
        self.weapon.rect.top = self.rect.top