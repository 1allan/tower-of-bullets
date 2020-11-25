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

    def be_hit(self, damage):
        self.hp -= damage
        print(self.hp)

    def die(self):
        print('chamou o die de character')
        self.kill()

    def update(self):
        if self.hp <= 0:
            self.weapon.kill()
            self.die()

        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2

        self.weapon.draw()
        self.weapon.rect.left = self.rect.left
        self.weapon.rect.top = self.rect.top