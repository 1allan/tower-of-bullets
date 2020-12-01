import pygame

from entity import Entity


class Character(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple,
                 speed: int, hp: int, sprite_group, image_file: str):
                 
        super().__init__(surface, position, size, speed, image_file)
        self.weapon = None
        self.hp = hp
        self.sprite_group = sprite_group
        self.last_direction = [1, 0]

    def move(self, direction=None):
        if direction[0] == self.last_direction[0] * -1:
            self.last_direction = direction
            self.image = pygame.transform.flip(self.image, True, False)
            self.weapon.image = pygame.transform.flip(self.weapon.image, True,
                                                      False)
        
        speed = self.speed
        # Sets an equivalent speed for diagonals
        if 0 not in direction:
            speed = round(((speed**2 + speed**2)**0.5)/2, 1)
        
        self.rect.left += speed * direction[0]
        self.rect.top += speed * direction[1]

    def shoot(self):
        pass

    def interact(self):
        pass

    def be_hit(self, damage):
        self.hp -= damage

    def die(self):
        self.kill()

    def update(self):
        if self.hp <= 0:
            self.weapon.kill()
            self.die()

        self.x = self.rect.left + self.width/2
        self.y = self.rect.top + self.height/2

        self.weapon.draw()
        
        if self.last_direction[0] == 1:
            self.weapon.rect.left = self.x
        elif self.last_direction[0] == -1:
            self.weapon.rect.left = self.x - 60
        self.weapon.rect.top = self.y
