import math
import pygame

from entity import Entity

# Checks if sprite1 minus an offset is colliding with sprite2
def walls_collide(sprite1, sprite2):
    offset = sprite1.width * 0.1, sprite1.height * 0.1
    coord = sprite1.rect.left + offset[0], sprite1.rect.top + offset[1]
    size = sprite1.width - offset[0], sprite1.height - offset[1]
    return pygame.Rect(coord, size).colliderect(sprite2)

class Character(Entity):

    def __init__(self, surface: pygame.Surface, 
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, speed: int, hp: int, 
                 wall_sprites: pygame.sprite.Group, image_file: str):

        super().__init__(surface, position, size, speed, image_file)

        self.weapon = None
        self.hp = hp
        self.bullets = pygame.sprite.Group()
        self.sprite_group = sprite_group
        self.wall_sprites = wall_sprites
        self.last_direction = [1, 0]

    def move(self, direction: tuple=None):
        if direction[0] == self.last_direction[0] * -1:
            self.last_direction = direction
            self.image = pygame.transform.flip(self.image, True, False)
            self.weapon.image = pygame.transform.flip(self.weapon.image, True,
                                                      False)
        # Sets an equivalent speed for diagonals
        speed = self.speed
        if 0 not in direction:
            speed = round(((speed**2 + speed**2)**0.5)/2, 1)

        positionBefore = (self.rect.left, self.rect.top)

        self.rect.left += speed * direction[0]
        collision = pygame.sprite.spritecollideany(self, self.wall_sprites, 
                                                   collided=walls_collide)
        if collision:
            self.rect.left = positionBefore[0]
        
        self.rect.top += speed * direction[1]
        collision = pygame.sprite.spritecollideany(self, self.wall_sprites, 
                                                   collided=walls_collide)
        if collision:
            self.rect.top = positionBefore[1]

    def attack(self, coordinates: tuple=None):
        if coordinates is not None:
            bullet = self.weapon.shoot(coordinates)
            if bullet is not None:
                self.bullets.add(bullet)
                return bullet

    def be_hit(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.weapon.kill()
            self.kill()

    def update(self):
        if self.last_direction[0] == 1:
            self.weapon.rect.left = self.x
        elif self.last_direction[0] == -1:
            self.weapon.rect.left = self.x - 60
        self.weapon.rect.top = self.y
        
        self.weapon.draw()
