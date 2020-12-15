import math
import pygame

from entity import Entity

# Checks if sprite1 minus an offset is colliding with sprite2
def walls_collide(sprite1, sprite2):
    offset = sprite1.width * 0.0, sprite1.height * 0.1
    coord = sprite1.rect.left + offset[0], sprite1.rect.top + offset[1]
    size = sprite1.width - offset[0], sprite1.height - offset[1]
    return pygame.Rect(coord, size).colliderect(sprite2)

class Character(Entity):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 speed: int, max_hp: int, wall_sprites: pygame.sprite.Group, 
                 image_file: str, animated=False):
        
        super().__init__(surface, position, size, speed, animated=animated, image_file=image_file)

        self.weapon = None
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.inv_time = 1000
        self.last_hit = pygame.time.get_ticks()
        self.bullets = pygame.sprite.Group()
        self.wall_sprites = wall_sprites
        self.last_direction = [1, 0]

    def move(self, direction: tuple=None):        
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
        tick = pygame.time.get_ticks()
        if tick - self.last_hit > self.inv_time:
            self.last_hit = tick
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                self.weapon.kill()
                self.kill()

    def update(self):
        if pygame.time.get_ticks() - self.last_hit < self.inv_time:
            self.image.set_alpha(155)
        else:
            self.image.set_alpha(255)
            
        self.weapon.rect.left = self.x
        self.weapon.rect.top = self.y
        
        self.weapon.draw()
